from TextureClass import textureClass

from OpenGL.GL import *


class Skybox:
    def __init__(self):
        self.textures = [
            "skybox_right.jpg", "skybox_left.jpg",
            "skybox_top.jpg", "skybox_bottom.jpg",
            "skybox_front.jpg", "skybox_back.jpg"
        ]
        self.texture_ids = [None] * 6
        self.size = 50.0  # Tamanho da skybox

    def carregar_texturas(self):
        for i in range(6):
            self.texture_ids[i] = textureClass(self.textures[i]).texId

    def desenhar(self):
        glEnable(GL_TEXTURE_2D)
        glColor3f(1, 1, 1)
        
        s = self.size / 2
        vertices = [
            # Face frontal
            [-s, -s, s], [s, -s, s], [s, s, s], [-s, s, s],
            # Face traseira
            [s, -s, -s], [-s, -s, -s], [-s, s, -s], [s, s, -s],
            # Face superior
            [-s, s, s], [s, s, s], [s, s, -s], [-s, s, -s],
            # Face inferior
            [-s, -s, -s], [s, -s, -s], [s, -s, s], [-s, -s, s],
            # Face direita
            [s, -s, s], [s, -s, -s], [s, s, -s], [s, s, s],
            # Face esquerda
            [-s, -s, -s], [-s, -s, s], [-s, s, s], [-s, s, -s]
        ]

        tex_coords = [
            (0, 0), (1, 0), (1, 1), (0, 1)
        ]

        faces = [
            (0, 1, 2, 3),   # Frontal
            (4, 5, 6, 7),   # Traseira
            (8, 9, 10, 11), # Superior
            (12, 13, 14, 15), # Inferior
            (16, 17, 18, 19), # Direita
            (20, 21, 22, 23)  # Esquerda
        ]

        glBegin(GL_QUADS)
        for i, face in enumerate(faces):
            glBindTexture(GL_TEXTURE_2D, self.texture_ids[i])
            for j, vert in enumerate(face):
                glTexCoord2fv(tex_coords[j])
                glVertex3fv(vertices[vert])
        glEnd()
        
        glDisable(GL_TEXTURE_2D)