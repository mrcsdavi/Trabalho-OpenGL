# Aqui vem todos os objetos
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
    modeloImportado = None

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
        light = LightClass() 
        light.iluminacao()

        if ObjetosClass.texturaLixeira is None:
            ObjetosClass.texturaLixeira = textureClass("Chao.png")  # Use sua textura de lixeira

        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, ObjetosClass.texturaLixeira.texId)
        
        glColor3f(1.0, 1.0, 1.0)  # Branco para não interferir na textura
        
        # Dimensões da lixeira (mais alta que larga)
        largura = 0.1
        altura = 0.15
        profundidade = 0.1
        
        vertices = [
            [-largura, -altura, -profundidade], [largura, -altura, -profundidade],
            [largura, altura, -profundidade], [-largura, altura, -profundidade],
            [-largura, -altura, profundidade], [largura, -altura, profundidade],
            [largura, altura, profundidade], [-largura, altura, profundidade]
        ]
        
        # Mesma ordem de faces do cubo original
        faces = [
            [0, 3, 2, 1],  # Face traseira
            [7, 4, 5, 6],  # Face frontal
            [1, 5, 4, 0],  # Face inferior
            [3, 7, 6, 2],  # Face superior
            [1, 2, 6, 5],  # Face direita
            [4, 7, 3, 0]   # Face esquerda
        ]

        texCoords = [
            (0, 0),
            (1, 0),
            (1, 1),
            (0, 1),
        ]

        normais = [
            [0, 0, -1],  # Traseira
            [0, 0, 1],   # Frontal
            [0, -1, 0],  # Inferior
            [0, 1, 0],   # Superior
            [1, 0, 0],   # Direita
            [-1, 0, 0]   # Esquerda
        ]
        
        glGenerateMipmap(GL_TEXTURE_2D)

        glBegin(GL_QUADS)
        for i, face in enumerate(faces):
            glNormal3fv(normais[i])
            for j, vert in enumerate(face):
                glTexCoord2fv(texCoords[j])
                glVertex3fv(vertices[vert])
        glEnd()
        
        glBindTexture(GL_TEXTURE_2D, 0)
        glDisable(GL_TEXTURE_2D)

    def diego():
        if ObjetosClass.modeloDiego is None:
            ObjetosClass.modeloDiego = ModeloClass("Diego.obj", "diegoTexture.png")
        
        
        
        # mais ...

    def desenharModeloImportado():
        if ObjetosClass.modeloImportado is None:
            ObjetosClass.modeloImportado = ModeloClass(
                "Diego.obj",
                "Chao.png"
            )

        ObjetosClass.modeloImportado.desenhar()
      

        
    # Posiciona o modelo corretamente na cena
        
        