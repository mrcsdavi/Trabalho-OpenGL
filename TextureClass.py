import os
from PIL import Image

from OpenGL.GL import *

from PIL import Image
from OpenGL.GL import *

class textureClass:
    def __init__(self, fileName, folderPath = r"C:\GAMES\CODIGOS\COMPUTACAO GRAFICA\Trabalho OpenGL\Texturas"):
        # Junta o caminho da pasta com o nome do arquivo
        fullPath = os.path.join(folderPath, fileName)

        img = Image.open(fullPath)
        img = img.transpose(Image.FLIP_TOP_BOTTOM)
        imgData = img.convert('RGBA').tobytes()

        self.texId = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, self.texId)
        
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_MIRRORED_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_MIRRORED_REPEAT)
    
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)

        glTexImage2D(
            GL_TEXTURE_2D,
            0,
            GL_RGBA,
            img.width,
            img.height,
            0,
            GL_RGBA,
            GL_UNSIGNED_BYTE,
            imgData
        )

        glGenerateMipmap(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, 0)
