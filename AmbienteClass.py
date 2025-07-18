from TextureClass import textureClass

from OpenGL.GL import *
from OpenGL.GLU import *

class AmbienteClass:
    textura_chao = None  # textura é da classe, para ser reutilizada

    

    def desenharChao():
   
        if AmbienteClass.textura_chao is None:
            AmbienteClass.textura_chao = textureClass("Packet.png")

        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, AmbienteClass.textura_chao.texId)
        glColor3f(1, 1, 1)

        chao = [
            [-10, 0, 10],
            [10, 0, 10],
            [10, 0, -10],
            [-10, 0, -10]
        ]

        texCoords = [
            (0, 0),
            (1, 0),
            (1, 1),
            (0, 1)
        ]

        glNormal3f(0, 1, 0)
        glBegin(GL_QUADS)
        for i in range(4):
            glTexCoord2f(*texCoords[i])  # Desempacota a tupla (u, v)
            glVertex3fv(chao[i])
        glEnd()

        glBindTexture(GL_TEXTURE_2D, 0)
        glDisable(GL_TEXTURE_2D)


    def Parede():
        pass

    def Teto():
        pass


    def Laje():
        pass
