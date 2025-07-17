# Classe para colocar apenas valores para usar
class LightClass:
    def __init__(self):
        #inicia iluminação
        self.light_pos = [20.0, 10.0, 5.0, 1.0] # posição da luz
    
    def iluminacao(self):
        self.ambientLight = [0.2, 0.2, 0.2, 1.0] 
        self.diffuseLight = [0.7, 0.7, 0.7, 1.0]
        self.specular = [1.0, 1.0, 1.0, 1.0]
        self.specref =  [1.0, 1.0, 1.0, 1.0] ## refleção especular