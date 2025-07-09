import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import math

# Posição da câmera
cam_pos = [0.0, 1.0, 5.0]  # próxima ao chão (y = 1)
yaw = -90.0  # olhar para frente no eixo -Z
pitch = 0.0

# Direção da câmera
cam_front = [0.0, 0.0, -1.0]
cam_up = [0.0, 1.0, 0.0]

# Movimento do mouse
lastX, lastY = 400, 300
primeiro_movimento = True
sensibilidade = 0.1

# Velocidade de movimento
velocidade = 0.1

def iniciar():
    glClearColor(0.5, 0.8, 1.0, 1.0)
    glEnable(GL_DEPTH_TEST)

def atualizar_camera():
    global cam_front
    # converte yaw e pitch em vetor de direção
    rad_yaw = math.radians(yaw)
    rad_pitch = math.radians(pitch)
    
    front_x = math.cos(rad_yaw) * math.cos(rad_pitch)
    front_y = math.sin(rad_pitch)
    front_z = math.sin(rad_yaw) * math.cos(rad_pitch)

    # normaliza
    comprimento = math.sqrt(front_x ** 2 + front_y ** 2 + front_z ** 2)
    cam_front[0] = front_x / comprimento
    cam_front[1] = front_y / comprimento
    cam_front[2] = front_z / comprimento

def processarInput(window):
    global cam_pos

    # Movimento lateral (direita/esquerda)
    right = [
        cam_front[2] * cam_up[1] - cam_front[1] * cam_up[2],
        cam_front[0] * cam_up[2] - cam_front[2] * cam_up[0],
        cam_front[1] * cam_up[0] - cam_front[0] * cam_up[1]
    ]
    comprimento = math.sqrt(right[0]**2 + right[1]**2 + right[2]**2)
    right = [r / comprimento for r in right]

    # W e S movem para frente/trás
    if glfw.get_key(window, glfw.KEY_W) == glfw.PRESS:
        cam_pos[0] += cam_front[0] * velocidade
        cam_pos[2] += cam_front[2] * velocidade
    if glfw.get_key(window, glfw.KEY_S) == glfw.PRESS:
        cam_pos[0] -= cam_front[0] * velocidade
        cam_pos[2] -= cam_front[2] * velocidade
    # A e D movem lateralmente
    if glfw.get_key(window, glfw.KEY_A) == glfw.PRESS:
        cam_pos[0] -= right[0] * velocidade
        cam_pos[2] -= right[2] * velocidade
    if glfw.get_key(window, glfw.KEY_D) == glfw.PRESS:
        cam_pos[0] += right[0] * velocidade
        cam_pos[2] += right[2] * velocidade

    # ESC sai
    if glfw.get_key(window, glfw.KEY_ESCAPE) == glfw.PRESS:
        glfw.set_window_should_close(window, True)

def mouse_callback(window, xpos, ypos):
    global lastX, lastY, yaw, pitch, primeiro_movimento

    if primeiro_movimento:
        lastX = xpos
        lastY = ypos
        primeiro_movimento = False

    xoffset = xpos - lastX
    yoffset = lastY - ypos
    lastX = xpos
    lastY = ypos

    xoffset *= sensibilidade
    yoffset *= sensibilidade

    yaw += xoffset
    pitch += yoffset

    if pitch > 89.0:
        pitch = 89.0
    if pitch < -89.0:
        pitch = -89.0

    atualizar_camera()

def desenharChao():
    glColor3f(0.3, 0.9, 0.3)
    glBegin(GL_QUADS)
    glVertex3f(-100, 0, -100)
    glVertex3f(100, 0, -100)
    glVertex3f(100, 0, 100)
    glVertex3f(-100, 0, 100)
    glEnd()

def desenharCubo():
    glColor3f(1.0, 0.0, 0.0)
    tamanho = 1.0
    metade = tamanho / 2.0

    vertices = [
        [-metade, -metade, -metade],
        [ metade, -metade, -metade],
        [ metade,  metade, -metade],
        [-metade,  metade, -metade],
        [-metade, -metade,  metade],
        [ metade, -metade,  metade],
        [ metade,  metade,  metade],
        [-metade,  metade,  metade]
    ]

    faces = [
        [0, 1, 2, 3],
        [4, 5, 6, 7],
        [0, 4, 7, 3],
        [1, 5, 6, 2],
        [3, 2, 6, 7],
        [0, 1, 5, 4]
    ]

    glPushMatrix()
    glTranslatef(0, 0.5, 0)
    glBegin(GL_QUADS)
    for face in faces:
        for vert in face:
            glVertex3fv(vertices[vert])
    glEnd()
    glPopMatrix()

def render():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # Câmera estilo FPS
    center = [
        cam_pos[0] + cam_front[0],
        cam_pos[1] + cam_front[1],
        cam_pos[2] + cam_front[2]
    ]

    gluLookAt(
        cam_pos[0], cam_pos[1], cam_pos[2],
        center[0], center[1], center[2],
        cam_up[0], cam_up[1], cam_up[2]
    )

    desenharChao()
    desenharCubo()

def main():
    if not glfw.init():
        return

    window = glfw.create_window(800, 600, "FPS Camera", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)
    glfw.set_cursor_pos_callback(window, mouse_callback)

    glViewport(0, 0, 800, 600)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, 800/600, 0.1, 100)

    iniciar()
    atualizar_camera()
    glfw.set_input_mode(window, glfw.CURSOR, glfw.CURSOR_DISABLED)

    while not glfw.window_should_close(window):
        processarInput(window)
        render()
        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()
