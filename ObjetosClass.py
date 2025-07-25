from ModeloClass import ModeloClass
from LightClass import LightClass
from TextureClass import textureClass

import math
from OpenGL.GL import *
from OpenGL.GLU import *


class ObjetosClass:
    #O QUE ESTA COMENTADO É DO CUBO PARA TESTES !!

    texturaCubo = None
    texturaPorta = None
    texturaLixeira = None
    modeloDiego = None
    modeloMesa = None

    # def desenharCubo():
    #     light = LightClass() 
    #     light.iluminacao()

    #     if ObjetosClass.texturaCubo is None:
    #        ObjetosClass.texturaCubo = textureClass("Parede.jpg")

    #     glEnable(GL_TEXTURE_2D)
    #     glBindTexture(GL_TEXTURE_2D, ObjetosClass.texturaCubo.texId)
        

    #     glColor3f(1.0, 0.0, 0.0)
        
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

    #     texCoords = [
    #         (0, 0),
    #         (1, 0),
    #         (1, 1),
    #         (0, 1),
    #     ]

    #     normais = [
    #     [0, 0, -1], [0, 0, 1], [-1, 0, 0],
    #     [1, 0, 0], [0, 1, 0], [0, -1, 0]
    #     ]
    #     glGenerateMipmap(GL_TEXTURE_2D)

    #     glBegin(GL_QUADS)
    #     for i, face in enumerate(faces):
    #         glNormal3fv(normais[i])
    #         for j, vert in enumerate(face):
    #             glTexCoord2fv(texCoords[j])
    #             glVertex3fv(vertices[vert])
    #     glEnd()

    def mesa():
        def mesa1():
            if ObjetosClass.modeloMesa is None:
                ObjetosClass.modeloMesa = ModeloClass(
                    "Mesa.obj",
                    "TexturaMesa.jpg"
                )
            ObjetosClass.modeloMesa.desenhar()
        
        # Mesas da esquerda - do fundão
        glPushMatrix()
        glTranslatef(10, -0.01, 5)
        glScalef(0.8, 0.8, 0.5)
        glRotate(90, 0, 1, 0.0)
        mesa1()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(10, -0.01, 3.5)
        glScalef(0.8, 0.8, 0.5)
        glRotate(90, 0, 1, 0.0)
        mesa1()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(10, -0.01, 2)
        glScalef(0.8, 0.8, 0.5)
        glRotate(90, 0, 1, 0.0)
        mesa1()
        glPopMatrix()
        
        # Mesas da esquerda - do meio

        glPushMatrix()
        glTranslatef(7, -0.01, 5)
        glScalef(0.8, 0.8, 0.5)
        glRotate(90, 0, 1, 0.0)
        mesa1()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(7, -0.01, 3.5)
        glScalef(0.8, 0.8, 0.5)
        glRotate(90, 0, 1, 0.0)
        mesa1()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(7, -0.01, 2)
        glScalef(0.8, 0.8, 0.5)
        glRotate(90, 0, 1, 0.0)
        mesa1()
        glPopMatrix()

        # Mesas da esquerda - do meio acima do meio

        glPushMatrix()
        glTranslatef(4, -0.01, 5)
        glScalef(0.8, 0.8, 0.5)
        glRotate(90, 0, 1, 0.0)
        mesa1()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(4, -0.01, 3.5)
        glScalef(0.8, 0.8, 0.5)
        glRotate(90, 0, 1, 0.0)
        mesa1()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(4, -0.01, 2)
        glScalef(0.8, 0.8, 0.5)
        glRotate(90, 0, 1, 0.0)
        mesa1()
        glPopMatrix()

        # mesas da esquerda - lá da frente

        glPushMatrix()
        glTranslatef(1, -0.01, 5)
        glScalef(0.8, 0.8, 0.5)
        glRotate(90, 0, 1, 0.0)
        mesa1()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(1, -0.01, 3.5)
        glScalef(0.8, 0.8, 0.5)
        glRotate(90, 0, 1, 0.0)
        mesa1()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(1, -0.01, 2)
        glScalef(0.8, 0.8, 0.5)
        glRotate(90, 0, 1, 0.0)
        mesa1()
        glPopMatrix()

        # MESAS DA DIREITA - do fundão

        glPushMatrix()
        glTranslatef(10, -0.01, -5)
        glScalef(0.8, 0.8, 0.5)
        glRotate(90, 0, 1, 0.0)
        mesa1()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(10, -0.01, -3.5)
        glScalef(0.8, 0.8, 0.5)
        glRotate(90, 0, 1, 0.0)
        mesa1()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(10, -0.01, -2)
        glScalef(0.8, 0.8, 0.5)
        glRotate(90, 0, 1, 0.0)
        mesa1()
        glPopMatrix()

        # MESAS DA DIREITA - do meio

        glPushMatrix()
        glTranslatef(7, -0.01, -5)
        glScalef(0.8, 0.8, 0.5)
        glRotate(90, 0, 1, 0.0)
        mesa1()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(7, -0.01, -3.5)
        glScalef(0.8, 0.8, 0.5)
        glRotate(90, 0, 1, 0.0)
        mesa1()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(7, -0.01, -2)
        glScalef(0.8, 0.8, 0.5)
        glRotate(90, 0, 1, 0.0)
        mesa1()
        glPopMatrix()

        # MESAS DA DIREITA - do meio

        glPushMatrix()
        glTranslatef(4, -0.01, -5)
        glScalef(0.8, 0.8, 0.5)
        glRotate(90, 0, 1, 0.0)
        mesa1()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(4, -0.01, -3.5)
        glScalef(0.8, 0.8, 0.5)
        glRotate(90, 0, 1, 0.0)
        mesa1()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(4, -0.01, -2)
        glScalef(0.8, 0.8, 0.5)
        glRotate(90, 0, 1, 0.0)
        mesa1()
        glPopMatrix()

        # MESAS DA DIREITA - da frente

        glPushMatrix()
        glTranslatef(4, -0.01, -5)
        glScalef(0.8, 0.8, 0.5)
        glRotate(90, 0, 1, 0.0)
        mesa1()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(4, -0.01, -3.5)
        glScalef(0.8, 0.8, 0.5)
        glRotate(90, 0, 1, 0.0)
        mesa1()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(4, -0.01, -2)
        glScalef(0.8, 0.8, 0.5)
        glRotate(90, 0, 1, 0.0)
        mesa1()
        glPopMatrix()


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

    def desenharPorta():
        # Configurações básicas (sem iluminação para simplificar)
        if ObjetosClass.texturaPorta is None:
           ObjetosClass.texturaPorta = textureClass("Porta.png")

        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, ObjetosClass.texturaPorta.texId)
        glColor3f(1, 1, 1)  # Cor branca para não alterar a textura

        # Dimensões da porta (largura, altura)
        largura = 1.0
        altura = 2.0

        # Define os vértices (apenas face frontal, sem profundidade)
        vertices = [
            [-largura/2, -altura/2, 0],  # Canto inferior esquerdo
            [largura/2, -altura/2, 0],   # Canto inferior direito
            [largura/2, altura/2, 0],     # Canto superior direito
            [-largura/2, altura/2, 0]     # Canto superior esquerdo
        ]

        # Coordenadas de textura (mapeamento simples)
        texCoords = [
            (0, 0),  # Inferior esquerdo
            (1, 0),  # Inferior direito
            (1, 1),  # Superior direito
            (0, 1)   # Superior esquerdo
        ]

        # Desenha a porta (um único quad)
        glBegin(GL_QUADS)
        glNormal3f(0, 0, 1)  # Normal apontando para frente
        for i in range(4):
            glTexCoord2fv(texCoords[i])
            glVertex3fv(vertices[i])
        glEnd()

        glDisable(GL_TEXTURE_2D)

    def desenharLixeira():
        pass
        
    def diego():
        def diegoModelo():
            if ObjetosClass.modeloDiego is None:
                ObjetosClass.modeloDiego = ModeloClass(
                    "Diego.obj",
                    "DiegoCorpo.png"
                )
            ObjetosClass.modeloDiego.desenhar()
        
        glPushMatrix()
        glTranslatef(-3.5, 0, -5)
        glScalef(0.25, 0.25,0.25)
        glRotate(90, 0, 1, 0.0)
        diegoModelo()
        glPopMatrix()

    
      

        
    # Posiciona o modelo corretamente na cena
        
        