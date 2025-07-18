from ObjetosClass import ObjetosClass
from ObjSemMaterialClass import ObjSemMatClass

from OpenGL.GL import *
from OpenGL.GLU import *

class SombraClass:
    def calcularShadowMatrix(ground_plane, light_pos):
        a, b, c, d = ground_plane
        x, y, z, w = light_pos
        
        dot = a*x + b*y + c*z + d*w
        mat = [
            dot - a*x,   -a*y,     -a*z,     -a*w,
            -b*x,     dot - b*y,   -b*z,     -b*w,
            -c*x,     -c*y,     dot - c*z,   -c*w,
            -d*x,     -d*y,     -d*z,     dot - d*w
        ]
        return mat  

    def desenharSombra(light_pos):
        chao_plano = [0.0, 0.5, 0.0, -0.001]  # plano y = 0
        sombra_mat = SombraClass.calcularShadowMatrix(chao_plano, light_pos)

        # Converter para o tipo aceito por glMultMatrixf (coluna-major)
        sombra_mat_gl = (GLfloat * 16)(*sombra_mat)

        glDisable(GL_LIGHTING)
        glColor4f(0.1, 0.1, 0.1, 0.7)

        # matriz pra redesenhar o mesmo objeto mas sem o material dele, para desenhar sua sombra
        glPushMatrix()
        glMultMatrixf(sombra_mat_gl)  
        #ObjSemMatClass.desenharCuboSemMaterial() # DO CUBO PARA TESTES !!
        glPopMatrix()

        glEnable(GL_LIGHTING)
    