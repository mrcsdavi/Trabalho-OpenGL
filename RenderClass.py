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
    
        #porta
        glPushMatrix()
        glTranslate(-4, 0.99, -5.95)
        ObjetosClass.desenharPorta()
        glPopMatrix()

        #Diego
        ObjetosClass.diego()
        ObjetosClass.mesa()
        ObjetosClass.mesaProf()
        ObjetosClass.laptopProf()

        AmbienteClass.Parede()
        AmbienteClass.ParedeJanela()
        AmbienteClass.ParedeDir()

        AmbienteClass.janela()
        AmbienteClass.janela2()
        AmbienteClass.desenharLuz()
        AmbienteClass.interruptor()
        AmbienteClass.ArCondi()

        ObjetosClass.telaProjetor()
        ObjetosClass.quadro()
        ObjetosClass.computador()
        ObjetosClass.projetor()
        ObjetosClass.cadeira()
        ObjetosClass.lixeira()



        # desenhar skybox
        glDisable(GL_CULL_FACE) 
        AmbienteClass.desenharSkybox()
        glEnable(GL_CULL_FACE)

        SombraClass.desenharSombra(lightClass.light_pos)


        