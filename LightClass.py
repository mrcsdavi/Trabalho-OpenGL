# Classe para colocar apenas valores iniciais para usar
class LightClass:
    def __init__(self):
        #inicia iluminação
        self.light_pos = [10, 10.0, 5.0, 1.0] # posição da luz
        #self.light_pos = [0, 10, -50, -1] # iluminação do lado de fora
    def iluminacao(self):
        self.ambientLight = [0.2, 0.2, 0.2, 1.0] 
        self.diffuseLight = [0.7, 0.7, 0.7, 1.0]
        self.specular = [1.0, 1.0, 1.0, 1.0]
        self.specref =  [1.0, 1.0, 1.0, 1.0] ## refleção especular