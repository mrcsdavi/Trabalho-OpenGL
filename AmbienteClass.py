from TextureClass import textureClass
from ModeloClass import ModeloClass

from OpenGL.GL import *
from OpenGL.GLU import *

class AmbienteClass:
    modeloSkybox = None
    
    texturaChao = None  # textura é da classe, para ser reutilizada
    texturaParede = None

    modeloParedeDir = None
    modeloParede = None
    modeloParedeJanela = None

    modeloJanela = None
    modeloJanela2 = None
    modeloLuz = None
    modeloInterruptor = None
    modeloArCondi = None
    
    def desenharChao():
        if AmbienteClass.texturaChao is None:
            AmbienteClass.texturaChao = textureClass("Chao.png") # abrir a textura

        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, AmbienteClass.texturaChao.texId)
        glColor3f(1, 1, 1)

        chao = [
            [-6, 0, 6],
            [13, 0, 6],
            [13, 0, -6],
            [-6, 0, -6]
        ]
        # coordernadas maiores do que 1 saem 
        
        texCoords = [
            (0, 0),
            (12, 0),
            (12, 6),
            (0, 6)
        ]
        
        glNormal3f(0, 1, 0)
        glBegin(GL_QUADS)
        for i in range(4):
            glTexCoord2f(*texCoords[i])  # Desempacota a tupla (u, v)
            glVertex3fv(chao[i])
        glEnd()
        glBindTexture(GL_TEXTURE_2D, 0)
        glDisable(GL_TEXTURE_2D)



    def Teto():
        if AmbienteClass.texturaParede is None:
            AmbienteClass.texturaParede = textureClass("Parede.jpg")  # Usa a mesma textura do chão, ou troque por "Teto.png"

        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, AmbienteClass.texturaParede.texId)
        glColor3f(1, 1, 1)

        teto = [
            [13, 3, 6],   # canto frontal esquerdo
            [-6, 3, 6],   # canto frontal direito
            [-6, 3, -6],  # canto traseiro direito
            [13, 3, -6]   # canto traseiro esquerdo
        ]

        texCoords = [
            (0, 0),
            (3, 0),
            (3, 3),
            (0, 3)
        ]

        glNormal3f(0, -1, 0)  # Normal apontando para baixo
        glBegin(GL_QUADS)
        for i in range(4):
            glTexCoord2f(*texCoords[i])
            glVertex3fv(teto[i])
        glEnd()

        glBindTexture(GL_TEXTURE_2D, 0)
        glDisable(GL_TEXTURE_2D)

    # Parede de frente e de costas
    def Parede():
        def Parede1():
            if AmbienteClass.modeloParede is None:
                AmbienteClass.modeloParede = ModeloClass(
                    "Parede.obj",
                    "Parede.jpg"
                )
            AmbienteClass.modeloParede.desenhar()
        
        # parede da frente
        glPushMatrix()
        glRotatef(180, 0, 1, 0)
        glTranslatef(5.5 , 0.1 , -5.7)
        glScalef(0.6, 0.6, 0.6)
        Parede1()
        glPopMatrix()

        # parede das costas
        glPushMatrix()
        glTranslatef(12.5, 0.1 , 6)
        glScalef(0.6, 0.6, 0.6)
        glRotatef(180, 0, 1, 0)
        Parede1()
        glPopMatrix()
       
    def ParedeDir():
        def ParedeDir():
            if AmbienteClass.modeloParedeDir is None:
                AmbienteClass.modeloParedeDir = ModeloClass(
                    "ParedeDireita.obj",
                    "Parede.jpg"
                )
            AmbienteClass.modeloParedeDir.desenhar()
        
        # parede da esquerda (janela)
        glPushMatrix()
        glRotatef(90, 0, 1, 0)
        glTranslatef(6.4 , -0.01 , 8)
        glScalef(0.5, 0.6, 0.5)
        ParedeDir()
        glPopMatrix()

    def ParedeJanela():
        def ParedeJanela():
            if AmbienteClass.modeloParedeJanela is None:
                AmbienteClass.modeloParedeJanela = ModeloClass(
                    "ParedeJanela.obj",
                    "Parede.jpg"
                )
            AmbienteClass.modeloParedeJanela.desenhar()
        
        # parede da esquerda (janela)
        glPushMatrix()
        glRotatef(90, 0, 1, 0)
        glTranslatef(-6 , -0.01 , 8)
        glScalef(0.5, 0.6, 0.5)
        ParedeJanela()
        glPopMatrix()

    def janela():
        def janela():
            if AmbienteClass.modeloJanela is None:
                AmbienteClass.modeloJanela = ModeloClass(
                    "Janela.obj",
                    None
                )
            AmbienteClass.modeloJanela.desenhar()
        
        #parede da esquerda (janelas) - buraco 1
        linha = 11.5
        coluna = 0.4
        for i in range(4):
            for j in range(4):
                glPushMatrix()
                glTranslatef(linha, coluna, 6)
                glRotatef(0, 0, 1, 0)
                glScalef(0.9, 0.6, 0.5)
                janela()
                glPopMatrix()
                linha = linha - 1.1
                if(linha < 8.2):
                    linha = 11.5  
            coluna = coluna + 0.6

        # buraco 2 - janelas
        linha1 = 6.5
        coluna1 = 0.4
        for i in range(4):
            for j in range(4):
                glPushMatrix()
                glTranslatef(linha1, coluna1, 6)
                glRotatef(0, 0, 1, 0)
                glScalef(0.9, 0.6, 0.5)
                janela()
                glPopMatrix()
                linha1 = linha1 - 1.1
                if(linha1 < 3.2):
                    linha1 = 6.5 
            coluna1 = coluna1 + 0.6

        # buraco 3 janelas
        linha2 = 1.2
        coluna2 = 0.4
        for i in range(6):
            for j in range(6):
                glPushMatrix()
                glTranslatef(linha2, coluna2, 6)
                glRotatef(0, 0, 1, 0)
                glScalef(0.9, 0.6, 0.5)
                janela()
                glPopMatrix()
                linha2 = linha2 - 1.1
                if(linha2 < - 5):
                    linha2 = 1.2
            coluna2 = coluna2 + 0.6
            if(coluna2 > 2.8):
                coluna2 = 0.4

    def janela2():
        def janela2():
            if AmbienteClass.modeloJanela2 is None:
                AmbienteClass.modeloJanela2 = ModeloClass(
                    "Janela2.obj",
                    None
                )
            AmbienteClass.modeloJanela2.desenhar()

        # janelas da parede da direita
        linha3 = 13
        for j in range(14):
            glPushMatrix()
            glTranslatef(linha3, 2.25, -6)
            glRotatef(180, 0, 1, 0)
            glScalef(0.9, 0.6, 0.5)
            janela2()
            glPopMatrix()
            linha3 = linha3 - 1.1

        glPushMatrix()
        glTranslatef(13, 2.25, -6)
        glRotatef(180, 0, 1, 0)
        glScalef(0.9, 0.6, 0.5)
        janela2()
        glPopMatrix()
    
    def desenharSkybox():
        def desenharSkybox():
            if AmbienteClass.modeloSkybox is None:
                AmbienteClass.modeloSkybox = ModeloClass(
                    "Skybox.obj",
                    "Skybox1.png"
                )
            AmbienteClass.modeloSkybox.desenhar()
        
        glPushMatrix()
        glTranslatef(0, 1, 0)
        glScalef(100, 100, 100)
        desenharSkybox()
        glPopMatrix()

    def desenharLuz():
        def desenharLuz():
            if AmbienteClass.modeloLuz is None:
                AmbienteClass.modeloLuz = ModeloClass(
                    "Luz.obj",
                    "ilumin2.png"
                )
            AmbienteClass.modeloLuz.desenhar()
        
        linha = 3
        coluna = 0
        for i in range(3):
            for j in range(3):
                glPushMatrix()
                glTranslatef(coluna, 3, linha)
                glScalef(-0.1, -0.1, -0.1)
                desenharLuz()
                glPopMatrix()
                linha = linha - 3
                if(linha < -3):
                    linha = 3
            coluna = coluna + 4

    def interruptor():
        def interruptor():
            if AmbienteClass.modeloInterruptor is None:
                AmbienteClass.modeloInterruptor = ModeloClass(
                    "interruptor.obj",
                    "ilumin2.png"
                )
            AmbienteClass.modeloInterruptor.desenhar()
        
        glPushMatrix()
        glTranslatef(-3, 1.5, -5.92)
        glScalef(0.4, 0.4, 0.4)
        glRotate(270, 0, 1,0)
        interruptor()
        glPopMatrix()

    def ArCondi():
        def ArCondi():
            if AmbienteClass.modeloArCondi is None:
                AmbienteClass.modeloArCondi = ModeloClass(
                    "ArCondicionado.obj",
                    "ilumin2.png"
                )
            AmbienteClass.modeloArCondi.desenhar()
        
        glPushMatrix()
        glTranslatef(-4.7, 1.7, 3)
        glScalef(0.2, 0.2, 0.2)
        ArCondi()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(12.9, 1.7, -3)
        glScalef(0.2, 0.2, 0.2)
        glRotate(180, 0, 1,0)
        ArCondi()
        glPopMatrix()

    def Laje():
        pass
