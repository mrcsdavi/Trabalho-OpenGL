from CameraClass import CameraClass

import glfw
import math


class InputClass:
    def __init__(window, cam):
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
            cam["pos"] = nova_pos

        if glfw.get_key(window, glfw.KEY_ESCAPE) == glfw.PRESS:
            glfw.set_window_should_close(window, True)

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
            ##if not testar_colisao(nova_pos):
            cam["pos"] = nova_pos

        if glfw.get_key(window, glfw.KEY_ESCAPE) == glfw.PRESS:
            glfw.set_window_should_close(window, True)