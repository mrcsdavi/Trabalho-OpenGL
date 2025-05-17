import glfw
from OpenGL.GL import *

def framebuffer_size_callback(window, width, height):
    glViewport(0,0,width, height)

def render():
    glClearColor(0,0,0,0)

def main():
    glfw.init()
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR , 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, glfw.OPENGL_CORE_PROFILE)
    
    window = glfw.create_window(800, 600, "Janela", None, None)
    if window == None:
        glfw.terminate()
        return
    
    glfw.make_context_current(window)
    glViewport(0,0,800,600)

    glfw.set_framebuffer_size_callback(window, framebuffer_size_callback)
    
    # renderizar na janela
    while not glfw.window_should_close(window):
        glfw.swap_buffers(window)
        glfw.poll_events()
        render()
    glfw.terminate()

if __name__ == '__main__':
    main()