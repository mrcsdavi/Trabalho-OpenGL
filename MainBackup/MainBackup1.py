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
    glEnable(GL_CULL_FACE)
    glEnable(GL_DEPTH_TEST)

    # iniciar iluminação
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_NORMALIZE)  # Para corrigir normais após transformações
    gerarIluminacao()  
   
    
def gerarIluminacao():
    glLightfv(GL_LIGHT0, GL_POSITION, [5.0, 10.0, 5.0, 1.0])
    glLightfv(GL_LIGHT0, GL_AMBIENT, [0.2, 0.2, 0.2, 1.0])
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [0.7, 0.7, 0.7, 1.0])
    glLightfv(GL_LIGHT0, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])


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

# ==================== COLISAO AABB ====================
def testar_colisao_aabb(ponto, raio, aabb_min, aabb_max):
    px, py, pz = ponto
    xmin, ymin, zmin = aabb_min
    xmax, ymax, zmax = aabb_max

    if (px + raio < xmin or px - raio > xmax or
        py + raio < ymin or py - raio > ymax or
        pz + raio < zmin or pz - raio > zmax):
        return False
    return True

def testar_colisao(nova_pos):
    cubo_min = [-0.5, 0.0, -0.5]
    cubo_max = [0.5, 1.0, 0.5]
    raio = 1.3 # isso aqui altera a distancia da colisao
    return testar_colisao_aabb(nova_pos, raio, cubo_min, cubo_max)

# ==================== RENDER ====================
def desenharChao():

    chao = [
        [-10, 0, 10],
        [10, 0, 10],
        [10, 0, -10],
        [-10, 0, -10]
    ]
    

    gray = [0.75, 0.75, 0.75, 1.0]

    #iluminação phong
    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, [0.3, 0.9, 0.3, 1.0])
    glMaterialfv(GL_FRONT, GL_SPECULAR, [0.1, 0.1, 0.1, 1.0])
    glMaterialf(GL_FRONT, GL_SHININESS, 10.0)

    glNormal3f(0, 1, 0)
    glBegin(GL_QUADS)
    for v in chao:
        glVertex3fv(v)
    glEnd()

def desenharCubo():
    glColor3f(1.0, 0.0, 0.0)
    metade = 0.5
    vertices = [
        [-metade, -metade, -metade], [metade, -metade, -metade],
        [metade, metade, -metade], [-metade, metade, -metade],
        [-metade, -metade, metade], [metade, -metade, metade],
        [metade, metade, metade], [-metade, metade, metade]
    ]
    faces = [
        [0, 3, 2, 1], [7, 4, 5, 6],
        [1, 5, 4, 0], [3, 7, 6, 2],
        [1, 2, 6, 5], [4, 7, 3, 0]
    ]

    # iluminação phong
    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, [1.0, 0.2, 0.2, 1.0])
    glMaterialfv(GL_FRONT, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])
    glMaterialf(GL_FRONT, GL_SHININESS, 64.0)
    
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

    cubo_min = [-0.5, 0.0, -0.5]
    cubo_max = [0.5, 1.0, 0.5]

    v = [
        [cubo_min[0], cubo_min[1], cubo_min[2]],  # 0
        [cubo_max[0], cubo_min[1], cubo_min[2]],  # 1
        [cubo_max[0], cubo_min[1], cubo_max[2]],  # 2
        [cubo_min[0], cubo_min[1], cubo_max[2]],  # 3
        [cubo_min[0], cubo_max[1], cubo_min[2]],  # 4
        [cubo_max[0], cubo_max[1], cubo_min[2]],  # 5
        [cubo_max[0], cubo_max[1], cubo_max[2]],  # 6
        [cubo_min[0], cubo_max[1], cubo_max[2]]   # 7
    ]

    edges = [
        (0,1), (1,2), (2,3), (3,0),
        (4,5), (5,6), (6,7), (7,4),
        (0,4), (1,5), (2,6), (3,7)
    ]

    for a, b in edges:
        glVertex3fv(v[a])
        glVertex3fv(v[b])
    glEnd()

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

    window = glfw.create_window(800, 600, "Laboratorio", None, None)
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
