import random

class GeneradorNumeros:
    def __init__(self):
        self.numeros = []
        self.pares = []
        self.impares = []

    def generar(self, cantidad=10):
        self.numeros = [random.randint(1, 100) for _ in range(cantidad)]

    def separar(self):
        self.pares = [num for num in self.numeros if num % 2 == 0]
        self.impares = [num for num in self.numeros if num % 2 != 0]
