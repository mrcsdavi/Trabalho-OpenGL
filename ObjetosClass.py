from ModeloClass import ModeloClass
from LightClass import LightClass
from TextureClass import textureClass

import math
from OpenGL.GL import *
from OpenGL.GLU import *


class ObjetosClass:
    tela_projetor_com_textura = True  # Começa com textura

    texturaCubo = None
    texturaPorta = None
    texturaLixeira = None
    modeloDiego = None

    modeloMesaProf = None
    modeloLaptopProf = None
    modeloMesa = None
    modeloComputador = None
    modeloCadeira = None
    modeloLixeira = None

    modeloQuadro = None
    modeloTelaProjetor = None
    modeloProjetor = None

    def mesaProf():
        def mesaProf():
            if ObjetosClass.modeloMesaProf is None:
                ObjetosClass.modeloMesaProf = ModeloClass(
                    "MesaProf.obj",
                    "Porta.png"
                )
            ObjetosClass.modeloMesaProf.desenhar()

        glPushMatrix()
        glTranslatef(-3, -0.01, 3)
        glScalef(1.2, 1.2, 0.9)
        glRotatef(90,0,1,0)
        mesaProf()
        glPopMatrix()

    def laptopProf():
        def laptopProf():
            if ObjetosClass.modeloLaptopProf is None:
                ObjetosClass.modeloLaptopProf = ModeloClass(
                    "LaptopComputer.obj",
                    "AulaIvo.png"
                )
            ObjetosClass.modeloLaptopProf.desenhar()

        glPushMatrix()
        glTranslatef(-3.1, 0.9, 3)
        glScalef(0.02, 0.02, 0.02)
        glRotatef(210,0,1,0)
        laptopProf()
        glPopMatrix()

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

    def computador():
        def computador():
            if ObjetosClass.modeloComputador is None:
                ObjetosClass.modeloComputador = ModeloClass(
                    "desktopComputer.obj",
                    "Mainmenu_cs.png"
                )
            ObjetosClass.modeloComputador.desenhar()
        
        # lado esquerdo das mesas
        coluna = [10, 7, 4, 1]
        linha = 5
        for i in range(4):
            for j in range(3):
                glPushMatrix()
                glTranslatef(coluna[i], 0.75, linha)
                glScalef(0.5, 0.5, 0.5)
                glRotate(270, 0, 1, 0.0)
                computador()
                glPopMatrix()
                linha = linha - 1.5
            if linha < 2:
                linha = 5

        # lado direito das mesas
        linha = -2
        for i in range(3):
            for j in range(3):
                glPushMatrix()
                glTranslatef(coluna[i], 0.75, linha)
                glScalef(0.5, 0.5, 0.5)
                glRotate(270, 0, 1, 0.0)
                computador()
                glPopMatrix()
                linha = linha - 1.5
            if linha < 5:
                linha = -2

    def cadeira():
        def cadeira():
            if ObjetosClass.modeloCadeira is None:
                ObjetosClass.modeloCadeira = ModeloClass(
                    "Cadeira.obj",
                    "TexturaCadeira.png"
                )
            ObjetosClass.modeloCadeira.desenhar()

        #Cadeira do professor
        glPushMatrix()
        glTranslatef(-4, 0, 3)
        glScalef(1, 1, 1)
        glRotate(100, 0, 1, 0.0)
        cadeira()
        glPopMatrix()

        #Cadeiras da esquerda
        coluna = [11, 8, 5, 2]
        linha = 5
        for i in range(4):
            for j in range(3):
                glPushMatrix()
                glTranslatef(coluna[i], 0, linha)
                glScalef(1, 1, 1)
                glRotate(25, 0, 1, 0.0)
                cadeira()
                glPopMatrix()
                linha = linha - 1.5
            if linha < 2:
                linha = 5

        #Cadeiras da direita
        coluna = [11, 8, 5, 2]
        linha = -2
        for i in range(3):
            for j in range(3):
                glPushMatrix()
                glTranslatef(coluna[i], 0, linha)
                glScalef(1, 1, 1)
                glRotate(25, 0, 1, 0.0)
                cadeira()
                glPopMatrix()
                linha = linha - 1.5
            if linha < -5:
                linha = -2
       
    # tentar fazer o projetor ligar e apresentar imagem, 
    # pode ser com o glQuads bem no quadro, e usar blending pra deixar transparente
    def telaProjetor():
        def telaProjetorInterna():
            if ObjetosClass.modeloTelaProjetor is None:
                ObjetosClass.modeloTelaProjetor = ModeloClass(
                    "TelaProjetor.obj",
                    "AulaIvo.png"
                )
            # Ativa ou desativa a textura conforme o estado
            if ObjetosClass.tela_projetor_com_textura:
                ObjetosClass.modeloTelaProjetor.desenhar()
            else:
                # Desenha o modelo sem textura (força textureId=None temporariamente)
                tex_id_backup = ObjetosClass.modeloTelaProjetor.textureId
                ObjetosClass.modeloTelaProjetor.textureId = None
                ObjetosClass.modeloTelaProjetor.desenhar()
                ObjetosClass.modeloTelaProjetor.textureId = tex_id_backup

        glPushMatrix()
        glTranslatef(-4.5, -0.3, 0)
        glScalef(0.5, 0.5, 0.5)
        glRotate(180, 0, 1, 0.0)
        telaProjetorInterna()
        glPopMatrix()

    def projetor():
        def projetor():
            if ObjetosClass.modeloProjetor is None:
                ObjetosClass.modeloProjetor = ModeloClass(
                    "projetor.obj",
                    "ilumin1.png"
                )
            ObjetosClass.modeloProjetor.desenhar()
        
        glPushMatrix()
        glTranslatef(1, 1.5, 0)
        glScalef(0.1, 0.1, 0.1)
        glRotate(270, 0, 1, 0.0)
        projetor()
        glPopMatrix()

    def quadro(): # Tentar fazer o quadro produzir um reflexo
        def quadro():
            if ObjetosClass.modeloQuadro is None:
                ObjetosClass.modeloQuadro = ModeloClass(
                    "Quadro.obj",
                    None
                )
            ObjetosClass.modeloQuadro.desenhar()
        
        glPushMatrix()
        glTranslatef(-4.7, 1, 0)
        glScalef(3.5, 2.5, 8)
        glRotate(90, 0, 1, 0.0)
        quadro()
        glPopMatrix()

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

    def lixeira():
        def lixeira():
            if ObjetosClass.modeloLixeira is None:
                ObjetosClass.modeloLixeira = ModeloClass(
                    "Lixeira.obj",
                    "Lixeira.png"
                )
            ObjetosClass.modeloLixeira.desenhar()
        
        glPushMatrix()
        glTranslatef(-2, 0, -5)
        glScalef(0.02, 0.02, 0.02)
        lixeira()
        glPopMatrix()

    def diego():
        def diegoModelo():
            if ObjetosClass.modeloDiego is None:
                ObjetosClass.modeloDiego = ModeloClass(
                    "Diego.obj",
                    "DiegoCorpo.png"
                )
            ObjetosClass.modeloDiego.desenhar()
        
        glPushMatrix()
        glTranslatef(-1.5, 0, -5)
        glScalef(0.25, 0.25,0.25)
        glRotate(90, 0, 1, 0.0)
        diegoModelo()
        glPopMatrix()

    
      

        
    # Posiciona o modelo corretamente na cena

