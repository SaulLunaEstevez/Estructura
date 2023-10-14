from numeros import Numeros

class Generador:
    def __init__(self):
        self.numeros = Numeros()
        
    def obtener_pares(self):
        return self.numeros.pares
    
    def obtener_impares(self):
        return self.numeros.impares
