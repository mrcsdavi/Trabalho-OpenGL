# Aqui vem todos os objetos sem material


from OpenGL.GL import *
from OpenGL.GLU import *


class ObjSemMatClass:
    # O QUE ESTÁ COMENTADO É DO CUBO PARA TESTES !!!

    # def desenharCuboSemMaterial(): ## segundo cubo para sombreamento
    #     metade = 0.5
    #     vertices = [
    #         [-metade, -metade, -metade], [metade, -metade, -metade],
    #         [metade, metade, -metade], [-metade, metade, -metade],
    #         [-metade, -metade, metade], [metade, -metade, metade],
    #         [metade, metade, metade], [-metade, metade, metade]
    #     ]
    #     faces = [
    #         [0, 3, 2, 1], [7, 4, 5, 6],
    #         [1, 5, 4, 0], [3, 7, 6, 2],
    #         [1, 2, 6, 5], [4, 7, 3, 0]
    #     ]
    #     glTranslatef(0.0, 0.5, 0.0) 
    #     glBegin(GL_QUADS)
    #     for face in faces:
    #         for vert in face:
    #             glVertex3fv(vertices[vert])
    #     glEnd()

    def mesas():
        pass

    def cadeiras():
        pass
    
    # tentar fazer o projetor ligar e apresentar imagem, 
    # pode ser com o glQuads bem no quadro, e usar blending pra deixar transparente
    def projetor(): 
        pass

    def quadro(): # Tentar fazer o quadro produzir um reflexo
        pass

    def monitores(): # tentar incluir reflexo bem fraco 
        pass

    def computadores():
        pass

    def janelas(): 
        pass

    def porta():
        pass

    def luzes(): # Colocar um botão para ligar a iluminação?
        pass

    def diego(): # colocar ele so pra frescar
        pass
        
        # mais ...
