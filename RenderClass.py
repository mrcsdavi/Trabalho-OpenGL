from LightClass import LightClass 
from ObjetosClass import ObjetosClass
from SombraClass import SombraClass
from AmbienteClass import AmbienteClass
from ModeloClass import ModeloClass

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

        # ambiente
        AmbienteClass.desenharChao()
        AmbienteClass.Teto()
        # parede da direita
        AmbienteClass.Parede()

        # parede da esquerda
        glPushMatrix()
        glTranslatef(0,3,0)
        glRotatef(180,1,0,0)
        AmbienteClass.Parede()
        glPopMatrix()

        # parede das costas da camera
        glPushMatrix()
        glTranslatef(7, 0, 0)
        glRotatef(270, 0, 9, 0)
        AmbienteClass.Parede()
        glPopMatrix()

        # parede da frente da camera
        glPushMatrix()
        glTranslatef(0, 0, 0)
        glRotatef(450, 0, 9, 0)
        AmbienteClass.Parede()
        glPopMatrix()

        #porta
        glPushMatrix()
        glTranslate(-5, 0.99, -5.99)
        ObjetosClass.desenharPorta()
        glPopMatrix()
        
        #lixeira
        glPushMatrix()
        glTranslate(-4, 0.15 , -5.5)
        ObjetosClass.desenharLixeira()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(-3.5, 0, -5)
        glScalef(0.25, 0.25,0.25)
        glRotate(90, 0, 1, 0.0)
        ObjetosClass.diego()
        glPopMatrix()


        glPushMatrix()
        glTranslatef(10, 0.8, 4)
        glScalef(0.013, 0.013,0.013)
        glRotate(90, 0, 1, 0.0)
        ObjetosClass.mesa()
        glPopMatrix()
   

        # Desenha o modelo importado
        
   


        # glPushMatrix()
        # glTranslate(0.0, 0.5, 0.0)
        # ObjetosClass.desenharCubo()
        # glPopMatrix()


        SombraClass.desenharSombra(lightClass.light_pos)