from OpenGL.GL import *
from TextureClass import textureClass
import os

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
        
        fullPath = os.path.join(folderPath, filename)
        if not os.path.exists(fullPath):
            print(f"Erro: Arquivo {fullPath} não encontrado.")
            return

        self._carregar_obj(fullPath)
        
        if textureFile:
            self._carregar_textura(textureFile, textureFolderPath)

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

    def _carregar_textura(self, textureFile, textureFolderPath):
        texture_path = os.path.join(textureFolderPath, textureFile)
        if os.path.exists(texture_path):
            texture = textureClass(textureFile, textureFolderPath)
            self.textureId = texture.texId
        else:
            print(f"Aviso: Arquivo de textura não encontrado em {texture_path}")

    def compilar(self):
        if self.compiled:
            return
            
        self.display_list = glGenLists(1)
        glNewList(self.display_list, GL_COMPILE)
        
        if self.textureId:
            glEnable(GL_TEXTURE_2D)
            glBindTexture(GL_TEXTURE_2D, self.textureId)

        glBegin(GL_TRIANGLES)
        for face in self.faces:
            # Triangulação para faces com mais de 3 vértices
            for i in range(1, len(face) - 1):
                indices = [face[0], face[i], face[i + 1]]
                for v_idx, vt_idx, vn_idx in indices:
                    if 0 <= vt_idx < len(self.textures):
                        glTexCoord2f(*self.textures[vt_idx])
                    if 0 <= vn_idx < len(self.normals):
                        glNormal3f(*self.normals[vn_idx])
                    if 0 <= v_idx < len(self.vertices):
                        glVertex3f(*self.vertices[v_idx])
        glEnd()
        
        if self.textureId:
            glBindTexture(GL_TEXTURE_2D, 0)
            glDisable(GL_TEXTURE_2D)
            
        glEndList()
        self.compiled = True

    def desenhar(self):
        if not self.compiled:
            self.compilar()
            
        if self.display_list:
            glCallList(self.display_list)
            