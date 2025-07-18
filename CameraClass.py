import math

from OpenGL.GL import *
from OpenGL.GLU import *

class CameraClass:
    def changeSize(w, h):
        #if h == 0:
        #    h = 1
 
        fAspect = w / h
        glViewport(0, 0, w, h)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45.0, fAspect, 1.0, 425.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    def atualizarCamera(cam):
        yaw = math.radians(cam["yaw"])
        pitch = math.radians(cam["pitch"])

        x = math.cos(yaw) * math.cos(pitch)
        y = math.sin(pitch)
        z = math.sin(yaw) * math.cos(pitch)

        comprimento = math.sqrt(x ** 2 + y ** 2 + z ** 2)
        cam["front"] = [x / comprimento, y / comprimento, z / comprimento]
        
    def inicializarCamera():
        return {
        "pos": [0.0, 1.1, 5.0],
        "front": [0.0, 0.0, -1.0],
        "up": [0.0, 1.0, 0.0],
        "yaw": -90.0,
        "pitch": 0.0,
        "lastX": 400,
        "lastY": 300,
        "primeiro_mov": True,
        "sensibilidade": 0.1,
        "velocidade": 0.003
    }