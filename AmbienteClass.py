from TextureClass import textureClass
from ModeloClass import ModeloClass

from OpenGL.GL import *
from OpenGL.GLU import *

class AmbienteClass:
    
    texturaChao = None  # textura é da classe, para ser reutilizada
    texturaParede = None
    
    modeloParede = None
    modeloParedeJanela = None
    modeloJanela = None
    
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

    # def carregarTexturaParede():
    #     if AmbienteClass.texturaParede is None:
    #         AmbienteClass.texturaParede = textureClass("Parede.jpg")

    # PAREDES
    # def Parede():
    #     AmbienteClass.carregarTexturaParede()
    #     glEnable(GL_TEXTURE_2D)
    #     glBindTexture(GL_TEXTURE_2D, AmbienteClass.texturaParede.texId)
    #     glColor3f(1, 1, 1)

    #     parede = [
    #         [-6, 0, -6],
    #         [13, 0, -6],
    #         [13, 3, -6],
    #         [-6, 3, -6]
    #     ]
    #     texCoords = [
    #         (0, 0),
    #         (12, 0),
    #         (12, 2),
    #         (0, 2)
    #     ]

    #     glNormal3f(0, 0, 1)
    #     glBegin(GL_QUADS)
    #     for i in range(4):
    #         glTexCoord2f(*texCoords[i])
    #         glVertex3fv(parede[i])
    #     glEnd()
    #     glBindTexture(GL_TEXTURE_2D, 0)
    #     glDisable(GL_TEXTURE_2D)

    
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
        
        # parede da esquerda (janela)

        glPushMatrix()
        glRotatef(90, 0, 1, 0)
        glTranslatef(-6 , -0.01 , 8)
        glScalef(0.5, 0.6, 0.5)
        janela()
        glPopMatrix()
       


    def Laje():
        pass
