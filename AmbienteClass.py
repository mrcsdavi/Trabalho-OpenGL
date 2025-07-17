# AQUI VEM AS PAREDES, TETO, CHÃO 

from OpenGL.GL import *
from OpenGL.GLU import *

class AmbienteClass:
    def Parede():
        pass

    def Teto():
        pass

    def desenharChao():
        glColor3f(0,1,0)
        chao = [
            [-10, 0, 10],
            [10, 0, 10],
            [10, 0, -10],
            [-10, 0, -10]
        ]

        glNormal3f(0, 1, 0)
        glBegin(GL_QUADS)
        for v in chao:
            glVertex3fv(v)
        glEnd()


    def Laje():
        pass