from LightClass import LightClass ## classe de iluminação importada

from OpenGL.GL import *
from OpenGL.GLU import *


class IniciarClass:
    # ==================== OPENGL SETUP ====================
    def iniciar():        
        light = LightClass() # CLASSE INSTANCIADA ILUMINAÇÃO
        light.iluminacao() # função de iluminação instanciada

        glEnable(GL_DEPTH_TEST) 
        glShadeModel(GL_FLAT)
        glEnable(GL_CULL_FACE) # não renderiza o que ta dentro
        glFrontFace(GL_CCW) # ajeita a face dos poligonos que podem estar pra dentro
    
        ## INICIAR ILUMINAÇÃO
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)

        glLightModeli(GL_LIGHT_MODEL_TWO_SIDE, GL_TRUE)
        
        glLightfv(GL_LIGHT0, GL_POSITION, light.light_pos)
        glLightfv(GL_LIGHT0, GL_AMBIENT, light.ambientLight)
        glLightfv(GL_LIGHT0, GL_DIFFUSE, light.diffuseLight)
        glLightfv(GL_LIGHT0, GL_SPECULAR, light.specular)  
        
        glEnable(GL_COLOR_MATERIAL) # cor dos materiais
        glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE) 
        glMaterialfv(GL_FRONT, GL_SPECULAR, light.specref)
        glMaterialf(GL_FRONT, GL_SHININESS, 64)
        
        # ativando o blending (deixou as sombras mais transparentes)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA) 
        glEnable(GL_BLEND)

        glClearColor(0.5, 0.8, 1.0, 1.0)

        glEnable(GL_NORMALIZE)