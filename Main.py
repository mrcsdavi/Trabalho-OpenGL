import glfw
from OpenGL.GL import *

# nao sei se precisa
        #def framebuffer_size_callback(window, width, height):
        #    glViewport(0,0,width, height)

# FUNÇÃO PRA RENDERIZAR A TELA
def render():
    glClearColor(1,0,0,1)
    glClear(GL_COLOR_BUFFER_BIT)

# função para pegar input do teclado
def processarInput(window):
    if(glfw.get_key(window, glfw.KEY_ESCAPE) == glfw.PRESS): # se precionar ESC a janela fecha
        glfw.set_window_should_close(window, True)

def main():
    glfw.init()
    #glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR , 3)
    #glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    #glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, glfw.OPENGL_CORE_PROFILE)
    
    window = glfw.create_window(800, 600, "Janela", None, None)
    if window == None:
        glfw.terminate()
        return
    
    glfw.make_context_current(window)
  
    glViewport(0,0,800,600)

    # nao sei se precisa
            # glfw.set_framebuffer_size_callback(window, framebuffer_size_callback)
    
    # renderizar tudo na janela do gflw
    while not glfw.window_should_close(window): 
        processarInput(window)


        render()


        glfw.swap_buffers(window)
        glfw.poll_events() 
    glfw.terminate() # encerra a janela do glfw

if __name__ == '__main__':
    main()