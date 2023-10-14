import random

class Producto:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cantidad = random.randint(1, 100)
        self.precio = random.uniform(1.0, 100.0)
        
    def __str__(self):
        return f"{self.nombre} - Cantidad: {self.cantidad} - Precio: ${self.precio:.2f}"
