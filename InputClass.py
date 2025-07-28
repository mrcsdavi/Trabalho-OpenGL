from CameraClass import CameraClass
from LightClass import LightClass
import time
from ObjetosClass import ObjetosClass

import glfw
import math

class InputClass:
    luz = None  # atributo de classe (estático), acessível em qualquer método
    ultimo_toggle_luz = 0  # timestamp da última troca

    def configurarLuz(luz_obj):
        InputClass.luz = luz_obj

    def processarInput(window, cam):
        vel = 0.0
        
        width, height = glfw.get_framebuffer_size(window)
        if width == 1920 and height == 991: # ajustar a velocidade para a largura e altura da tela
            vel = cam["velocidade"] = 0.010
        else:
            vel = cam["velocidade"] = 0.003
        pos = cam["pos"]
        front = cam["front"]
        up = cam["up"]
        
        # Calcular vetor lateral
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
            ##if not testar_colisao(nova_pos):
            cam["pos"] = nova_pos

        if glfw.get_key(window, glfw.KEY_ESCAPE) == glfw.PRESS:
            glfw.set_window_should_close(window, True)

        # ------ INTERRUPTOR DO PROJETOR ------
        projetor_pos = [0, 0, 0]
        raio_ativacao_proj = 2.0

        dx_proj = cam["pos"][0] - projetor_pos[0]
        dz_proj = cam["pos"][2] - projetor_pos[2]
        distancia_proj = math.sqrt(dx_proj * dx_proj + dz_proj * dz_proj)

        if not hasattr(InputClass, "ultimo_toggle_projetor"):
            InputClass.ultimo_toggle_projetor = 0

        agora = time.time()
        cooldown = 0.5

        if (distancia_proj < raio_ativacao_proj and
            glfw.get_key(window, glfw.KEY_E) == glfw.PRESS and
            agora - InputClass.ultimo_toggle_projetor > cooldown):
            ObjetosClass.tela_projetor_com_textura = not ObjetosClass.tela_projetor_com_textura
            InputClass.ultimo_toggle_projetor = agora

        # ------ INTERRUPTOR ------
        interruptor_pos = [-3.0, 0.0, -5.92]  # posição do interruptor
        raio_ativacao = 2.0

        dx = cam["pos"][0] - interruptor_pos[0]
        dz = cam["pos"][2] - interruptor_pos[2]
        distancia = math.sqrt(dx * dx + dz * dz)

        agora = time.time()
        cooldown = 0.5  # meio segundo de delay

        if (distancia < raio_ativacao and
            glfw.get_key(window, glfw.KEY_E) == glfw.PRESS and
            agora - InputClass.ultimo_toggle_luz > cooldown):
            luz = InputClass.luz
            if luz is not None:
                if luz.light_pos == [10, 10.0, 5.0, 1.0]:
                    luz.light_pos = [0, 10, -50, -1]
                else:
                    luz.light_pos = [10, 10.0, 5.0, 1.0]
            InputClass.ultimo_toggle_luz = agora

    def mouseCallback(cam):
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
            CameraClass.atualizarCamera(cam)
        return callback

