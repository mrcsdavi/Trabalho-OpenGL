import numpy as np
from OpenGL.GL import *
from OpenGL.arrays import vbo

class SombraClass:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SombraClass, cls).__new__(cls)
            cls._instance.initialized = False
        return cls._instance
    
    def init(self, objetos):
        """Inicializa com os objetos que podem projetar sombras"""
        self.objetos = objetos
        self.shadow_volumes = {}
        self.initialized = True
        
    def atualizar_luz(self, light_pos):
        """Atualiza a posição da luz para todos os volumes de sombra"""
        self.light_pos = np.array(light_pos + [1.0]) if len(light_pos) == 3 else np.array(light_pos)
        
    def _criar_shadow_volume(self, objeto):
        """Cria um volume de sombra para um objeto específico"""
        vertices = objeto.get_vertices()
        faces = objeto.get_faces()
        
        if not vertices or not faces:
            return None
            
        # Encontra todas as arestas
        edges = set()
        for face in faces:
            for i in range(len(face)):
                v1 = face[i]
                v2 = face[(i+1)%len(face)]
                edges.add(frozenset((v1, v2)))
        edges = [tuple(e) for e in edges]
        
        # Cria estrutura para o volume de sombra
        return {
            'vertices': vertices,
            'faces': faces,
            'edges': edges,
            'vbo': None,
            'indices_vbo': None
        }
        
    def _atualizar_silhueta(self, volume):
        """Atualiza as arestas de silhueta para um volume de sombra"""
        silhouette_edges = []
        vertices = volume['vertices']
        faces = volume['faces']
        edges = volume['edges']
        
        # Verifica visibilidade das faces
        face_visibility = []
        for face in faces:
            v0 = vertices[face[0]]
            v1 = vertices[face[1]]
            v2 = vertices[face[2]]
            
            edge1 = np.array(v1) - np.array(v0)
            edge2 = np.array(v2) - np.array(v0)
            normal = np.cross(edge1, edge2)
            normal = normal / np.linalg.norm(normal)
            
            to_light = np.array(self.light_pos[:3]) - np.array(v0)
            
            face_visibility.append(np.dot(normal, to_light) > 0)
            
        # Mapeia arestas para faces
        edge_faces = {}
        for i, face in enumerate(faces):
            for j in range(len(face)):
                v1 = face[j]
                v2 = face[(j+1)%len(face)]
                edge = tuple(sorted((v1, v2)))
                if edge not in edge_faces:
                    edge_faces[edge] = []
                edge_faces[edge].append(i)
                
        # Encontra arestas de silhueta
        for edge, faces_indices in edge_faces.items():
            if len(faces_indices) == 1:
                if face_visibility[faces_indices[0]]:
                    silhouette_edges.append(edge)
            else:
                if face_visibility[faces_indices[0]] != face_visibility[faces_indices[1]]:
                    silhouette_edges.append(edge)
                    
        return silhouette_edges
        
    def _extrudir_silhueta(self, volume, silhouette_edges, extrusion_length=100.0):
        """Cria a geometria extrudada para o volume de sombra"""
        if not silhouette_edges:
            return None, None
            
        vertices = volume['vertices']
        extruded_verts = []
        indices = []
        
        for edge in silhouette_edges:
            v1 = vertices[edge[0]]
            v2 = vertices[edge[1]]
            
            dir1 = np.array(v1) - self.light_pos[:3]
            dir1 = dir1 / np.linalg.norm(dir1)
            extruded_v1 = np.array(v1) + dir1 * extrusion_length
            
            dir2 = np.array(v2) - self.light_pos[:3]
            dir2 = dir2 / np.linalg.norm(dir2)
            extruded_v2 = np.array(v2) + dir2 * extrusion_length
            
            extruded_verts.extend([v1, v2, extruded_v1, extruded_v2])
            
            base_idx = len(extruded_verts)//4 - 1
            indices.extend([
                base_idx*4, base_idx*4+1, base_idx*4+2,
                base_idx*4+1, base_idx*4+3, base_idx*4+2
            ])
            
        return np.array(extruded_verts, dtype='f'), np.array(indices, dtype='uint32')
        
    def desenharSombra(self, light_pos):
        """Renderiza as sombras usando a técnica de stencil"""
        if not self.initialized:
            return
            
        self.atualizar_luz(light_pos)
        
        # Passo 1: Configuração inicial do stencil
        glEnable(GL_STENCIL_TEST)
        glStencilFunc(GL_ALWAYS, 0, 0xFF)
        glStencilOp(GL_KEEP, GL_KEEP, GL_KEEP)
        
        # Passo 2: Renderiza a cena normalmente (o seu código atual faz isso)
        
        # Passo 3: Configura para desenhar os volumes de sombra no stencil buffer
        glStencilFunc(GL_ALWAYS, 0, 0xFF)
        glStencilOpSeparate(GL_BACK, GL_KEEP, GL_INCR_WRAP, GL_KEEP)
        glStencilOpSeparate(GL_FRONT, GL_KEEP, GL_DECR_WRAP, GL_KEEP)
        glColorMask(GL_FALSE, GL_FALSE, GL_FALSE, GL_FALSE)
        glDepthMask(GL_FALSE)
        
        # Renderiza todos os volumes de sombra
        for obj in self.objetos:
            if obj.cast_shadow:
                if obj not in self.shadow_volumes:
                    self.shadow_volumes[obj] = self._criar_shadow_volume(obj)
                
                volume = self.shadow_volumes[obj]
                silhouette = self._atualizar_silhueta(volume)
                extruded_verts, indices = self._extrudir_silhueta(volume, silhouette)
                
                if extruded_verts is not None and indices is not None:
                    # Usa VBOs para renderização eficiente
                    if volume['vbo'] is None:
                        volume['vbo'] = vbo.VBO(extruded_verts)
                        volume['indices_vbo'] = vbo.VBO(
                            indices,
                            target=GL_ELEMENT_ARRAY_BUFFER
                        )
                    else:
                        volume['vbo'].set_array(extruded_verts)
                        volume['indices_vbo'].set_array(indices)
                    
                    volume['vbo'].bind()
                    glVertexPointer(3, GL_FLOAT, 0, None)
                    glEnableClientState(GL_VERTEX_ARRAY)
                    
                    volume['indices_vbo'].bind()
                    glDrawElements(GL_TRIANGLES, len(indices), GL_UNSIGNED_INT, None)
                    
                    volume['indices_vbo'].unbind()
                    volume['vbo'].unbind()
                    glDisableClientState(GL_VERTEX_ARRAY)
        
        # Passo 4: Restaura configurações e renderiza apenas áreas não sombreadas
        glColorMask(GL_TRUE, GL_TRUE, GL_TRUE, GL_TRUE)
        glDepthMask(GL_TRUE)
        glStencilFunc(GL_EQUAL, 0, 0xFF)
        glStencilOp(GL_KEEP, GL_KEEP, GL_KEEP)
        
        # A renderização das áreas escuras será feita naturalmente pelo seu render loop
        # pois o stencil buffer já está configurado
        
        glDisable(GL_STENCIL_TEST)