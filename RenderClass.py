from LightClass import LightClass 
from ObjetosClass import ObjetosClass
from SombraClass import SombraClass
from AmbienteClass import AmbienteClass

from OpenGL.GL import *
from OpenGL.GLU import *


class RenderClass:
    def render(cam):
        lightClass = LightClass() # instancia a classe iluminação
  
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        pos = cam["pos"]
        front = cam["front"]
        up = cam["up"]

        gluLookAt(
            pos[0], pos[1], pos[2],
            pos[0] + front[0], pos[1] + front[1], pos[2] + front[2],
            up[0], up[1], up[2]
        )

        glLightfv(GL_LIGHT0, GL_POSITION, lightClass.light_pos) # faz o brilho especular, deixar renderizando sempre. Nao mexa

        AmbienteClass.desenharChao()
       # ObjetosClass.desenharCubo()
        SombraClass.desenharSombra(lightClass.light_pos) 