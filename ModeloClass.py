from OpenGL.GL import *
from TextureClass import textureClass
import os
import numpy as np

class ModeloClass:
    def __init__(self, filename, textureFile=None, 
                folderPath=r"C:\GAMES\CODIGOS\COMPUTACAO GRAFICA\Trabalho OpenGL\Modelos", 
                textureFolderPath=r"C:\GAMES\CODIGOS\COMPUTACAO GRAFICA\Trabalho OpenGL\Texturas"):
        self.vertices = []
        self.textures = []
        self.normals = []
        self.faces = []
        self.textureId = None
        self.compiled = False
        self.display_list = None
        self.vertex_vbo = None
        self.tex_vbo = None
        self.normal_vbo = None
        self.num_vertices = 0
        
        fullPath = os.path.join(folderPath, filename)
        if not os.path.exists(fullPath):
            print(f"Erro: Arquivo {fullPath} não encontrado.")
            return

        self._carregar_obj(fullPath)
        
        if textureFile:
            self._carregar_textura(textureFile, textureFolderPath)
        
        # Pré-processamento para triangulação
        self._preprocessar_faces()

    def _carregar_obj(self, path):
        with open(path, "r") as file:
            for line in file:
                if not line.strip(): 
                    continue
                    
                prefix = line.split()[0]
                data = line.split()[1:]
                
                if prefix == "v":
                    self.vertices.append(tuple(map(float, data[:3])))
                elif prefix == "vt":
                    self.textures.append(tuple(map(float, data[:2])))
                elif prefix == "vn":
                    self.normals.append(tuple(map(float, data[:3])))
                elif prefix == "f":
                    face = []
                    for vert in data:
                        indices = vert.split('/')
                        v_idx = int(indices[0]) - 1
                        vt_idx = int(indices[1]) - 1 if len(indices) > 1 and indices[1] else -1
                        vn_idx = int(indices[2]) - 1 if len(indices) > 2 and indices[2] else -1
                        face.append((v_idx, vt_idx, vn_idx))
                    self.faces.append(face)

    def _preprocessar_faces(self):
        """Converte todas as faces em triângulos durante o carregamento."""
        triangulated_faces = []
        for face in self.faces:
            for i in range(1, len(face) - 1):
                triangulated_faces.append([face[0], face[i], face[i + 1]])
        self.faces = triangulated_faces

    def _carregar_textura(self, textureFile, textureFolderPath):
        texture_path = os.path.join(textureFolderPath, textureFile)
        if os.path.exists(texture_path):
            texture = textureClass(textureFile, textureFolderPath)
            self.textureId = texture.texId
        else:
            print(f"Aviso: Arquivo de textura não encontrado em {texture_path}")

    def _gerar_arrays(self):
        """Gera arrays otimizados para renderização."""
        vertex_data = []
        tex_data = [] 
        normal_data = [] 
        
        tem_textura = (self.textureId is not None and len(self.textures) > 0)
        tem_normais = (len(self.normals) > 0)
        
        for face in self.faces:
            for v_idx, vt_idx, vn_idx in face:
                # Vértices
                vertex_data.extend(self.vertices[v_idx])
                
                # Texturas
                if tem_textura and 0 <= vt_idx < len(self.textures):
                    tex_data.extend(self.textures[vt_idx])
                else:
                    tex_data.extend([0.0, 0.0])  # Valor padrão se não houver textura
                
                # Normais
                if tem_normais and 0 <= vn_idx < len(self.normals):
                    normal_data.extend(self.normals[vn_idx])
                else:
                    normal_data.extend([0.0, 1.0, 0.0])  # Normal padrão (apontando para cima)
        
        # Convertendo para arrays numpy para melhor performance
        self.vertex_array = np.array(vertex_data, dtype=np.float32)
        self.tex_array = np.array(tex_data, dtype=np.float32)
        self.normal_array = np.array(normal_data, dtype=np.float32)
        self.num_vertices = len(vertex_data) // 3

    def _setup_vbos(self):
        """Configura VBOs separados para cada tipo de dado"""
        # Vértices
        self.vertex_vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.vertex_vbo)
        glBufferData(GL_ARRAY_BUFFER, self.vertex_array.nbytes, self.vertex_array, GL_STATIC_DRAW)
        
        # Texturas
        self.tex_vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.tex_vbo)
        glBufferData(GL_ARRAY_BUFFER, self.tex_array.nbytes, self.tex_array, GL_STATIC_DRAW)
        
        # Normais
        self.normal_vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.normal_vbo)
        glBufferData(GL_ARRAY_BUFFER, self.normal_array.nbytes, self.normal_array, GL_STATIC_DRAW)
        
        glBindBuffer(GL_ARRAY_BUFFER, 0)

    def compilar(self):
        if self.compiled:
            return
            
        self._gerar_arrays()
        self._setup_vbos()
        self.compiled = True

    def desenhar(self):
        if not self.compiled:
            self.compilar()
            
        # Ativar textura se disponível
        if self.textureId:
            glEnable(GL_TEXTURE_2D)
            glBindTexture(GL_TEXTURE_2D, self.textureId)
        
        # Habilita estados de array
        glEnableClientState(GL_VERTEX_ARRAY)
        
        # Configurar ponteiros para vértices
        glBindBuffer(GL_ARRAY_BUFFER, self.vertex_vbo)
        glVertexPointer(3, GL_FLOAT, 0, None)
        
        # Configurar ponteiros para texturas
        glEnableClientState(GL_TEXTURE_COORD_ARRAY)
        glBindBuffer(GL_ARRAY_BUFFER, self.tex_vbo)
        glTexCoordPointer(2, GL_FLOAT, 0, None)
        
        # Configurar ponteiros para normais
        glEnableClientState(GL_NORMAL_ARRAY)
        glBindBuffer(GL_ARRAY_BUFFER, self.normal_vbo)
        glNormalPointer(GL_FLOAT, 0, None)
        
        # Desenhar os triângulos
        glDrawArrays(GL_TRIANGLES, 0, self.num_vertices)
        
        # Desabilitar estados
        glDisableClientState(GL_VERTEX_ARRAY)
        glDisableClientState(GL_TEXTURE_COORD_ARRAY)
        glDisableClientState(GL_NORMAL_ARRAY)
        glBindBuffer(GL_ARRAY_BUFFER, 0)
        
        # Desativar textura
        if self.textureId:
            glBindTexture(GL_TEXTURE_2D, 0)
            glDisable(GL_TEXTURE_2D)