import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import math

# ==================== CONFIG CAMERA ====================
def inicializar_camera():
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

# ==================== OPENGL SETUP ====================
def iniciar():
    glClearColor(0.5, 0.8, 1.0, 1.0)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_FLAT)
    #glEnable(GL_CULL_FACE)
    glEnable(GL_DEPTH_TEST)

# ==================== PROJECAO ====================
def changeSize(w, h):
    if h == 0:
        h = 1
    fAspect = w / h
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, fAspect, 1.0, 425.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

# ==================== CAMERA ====================
def atualizar_camera(cam):
    yaw = math.radians(cam["yaw"])
    pitch = math.radians(cam["pitch"])

    x = math.cos(yaw) * math.cos(pitch)
    y = math.sin(pitch)
    z = math.sin(yaw) * math.cos(pitch)

    comprimento = math.sqrt(x ** 2 + y ** 2 + z ** 2)
    cam["front"] = [x / comprimento, y / comprimento, z / comprimento]

def processarInput(window, cam):
    pos = cam["pos"]
    front = cam["front"]
    up = cam["up"]
    vel = cam["velocidade"]

    # Calcular vetor lateral (right)
    right = [
        front[2] * up[1] - front[1] * up[2],
        front[0] * up[2] - front[2] * up[0],
        front[1] * up[0] - front[0] * up[1]
    ]
    comprimento = math.sqrt(sum(r ** 2 for r in right))
    right = [r / comprimento for r in right]

    # Inicializar deslocamento
    deslocamento = [0.0, 0.0, 0.0]

    if glfw.get_key(window, glfw.KEY_W) == glfw.PRESS:
        deslocamento[0] += front[0]
        deslocamento[2] += front[2]
    if glfw.get_key(window, glfw.KEY_S) == glfw.PRESS:
        deslocamento[0] -= front[0]
        deslocamento[2] -= front[2]
    if glfw.get_key(window, glfw.KEY_D) == glfw.PRESS:
        deslocamento[0] -= right[0]
        deslocamento[2] -= right[2]
    if glfw.get_key(window, glfw.KEY_A) == glfw.PRESS:
        deslocamento[0] += right[0]
        deslocamento[2] += right[2]

    # Normaliza deslocamento
    comprimento = math.sqrt(deslocamento[0]**2 + deslocamento[2]**2)
    if comprimento > 0:
        deslocamento[0] /= comprimento
        deslocamento[2] /= comprimento

        nova_pos = [
            pos[0] + deslocamento[0] * vel,
            pos[1],
            pos[2] + deslocamento[2] * vel
        ]
        if not testar_colisao(nova_pos):
            cam["pos"] = nova_pos

    if glfw.get_key(window, glfw.KEY_ESCAPE) == glfw.PRESS:
        glfw.set_window_should_close(window, True)

def mouse_callback(cam):
    def callback(window, xpos, ypos):
        if cam["primeiro_mov"]:
            cam["lastX"] = xpos
            cam["lastY"] = ypos
            cam["primeiro_mov"] = False

        xoffset = xpos - cam["lastX"]
        yoffset = cam["lastY"] - ypos
        cam["lastX"] = xpos
        cam["lastY"] = ypos

        xoffset *= cam["sensibilidade"]
        yoffset *= cam["sensibilidade"]

        cam["yaw"] += xoffset
        cam["pitch"] += yoffset

        cam["pitch"] = max(-89.0, min(89.0, cam["pitch"]))
        atualizar_camera(cam)
    return callback

# ==================== RENDER ====================
def desenharChao():

    chao = [
        [-10, 0, -100],
        [10, 0, -100],
        [10, 0, 100],
        [-10, 0, 100]
    ]
    glColor3f(0.3, 0.9, 0.3)

    glBegin(GL_QUADS)
    for v in chao:
        glVertex3fv(v)
    glEnd()

def desenharCubo():

    glColor3f(1.0, 0.0, 0.0)
    tamanho = 1.0
    metade = tamanho / 2.0
    vertices = [
        [-metade, -metade, -metade], [metade, -metade, -metade],
        [metade, metade, -metade], [-metade, metade, -metade],
        [-metade, -metade, metade], [metade, -metade, metade],
        [metade, metade, metade], [-metade, metade, metade]
    ]
    faces = [
        [0, 1, 2, 3], [4, 5, 6, 7],
        [0, 4, 7, 3], [1, 5, 6, 2],
        [3, 2, 6, 7], [0, 1, 5, 4]
    ]
    glPushMatrix()

    glTranslatef(0, 0.5, 0)
    glBegin(GL_QUADS)
    for face in faces:
        for vert in face:
            glVertex3fv(vertices[vert])
    glEnd()
    glPopMatrix()

def desenhar_caixa_colisao():
    glColor3f(1, 1, 0)
    glBegin(GL_LINES)
    v = [
        (-0.5, 0.0, -0.5), (0.5, 0.0, -0.5),
        (0.5, 0.0, 0.5), (-0.5, 0.0, 0.5),
        (-0.5, 1.0, -0.5), (0.5, 1.0, -0.5),
        (0.5, 1.0, 0.5), (-0.5, 1.0, 0.5)
    ]
    for i in range(4):
        glVertex3fv(v[i])
        glVertex3fv(v[(i+1)%4])
        glVertex3fv(v[i+4])
        glVertex3fv(v[((i+1)%4)+4])
        glVertex3fv(v[i])
        glVertex3fv(v[i+4])
    glEnd()

def testar_colisao(nova_pos):
    cubo_min = [-0.5, 0.0, -0.5]
    cubo_max = [1, 1.0, 1]
    raio = 0.2
    x, z = nova_pos[0], nova_pos[2]
    if (x + raio > cubo_min[0] and x - raio < cubo_max[0] and
        z + raio > cubo_min[2] and z - raio < cubo_max[2]):
        return True
    return False

def render(cam):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    pos = cam["pos"]
    front = cam["front"]
    up = cam["up"]

    gluLookAt(
        pos[0], pos[1], pos[2],
        pos[0] + front[0], pos[1] + front[1], pos[2] + front[2],
        up[0], up[1], up[2]
    )

    desenharChao()
    desenharCubo()
    desenhar_caixa_colisao()

# ==================== MAIN ====================
def main():
    if not glfw.init():
        return

    window = glfw.create_window(800, 600, "FPS Camera", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)
    cam = inicializar_camera()
    glfw.set_cursor_pos_callback(window, mouse_callback(cam))
    glfw.set_input_mode(window, glfw.CURSOR, glfw.CURSOR_DISABLED)

    iniciar()
    atualizar_camera(cam)

    while not glfw.window_should_close(window):
        width, height = glfw.get_framebuffer_size(window)
        changeSize(width, height)
        processarInput(window, cam)
        render(cam)
        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()
