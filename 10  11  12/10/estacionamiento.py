# estacionamiento.py
from collections import deque
from auto import Auto

class Estacionamiento:
    def __init__(self):
        self.cola = deque()

    def entrada_auto(self, placas, propietario):
        nuevo_auto = Auto(placas, propietario)
        self.cola.append(nuevo_auto)
        return nuevo_auto

    def salida_auto(self):
        if len(self.cola) == 0:
            return None
        auto = self.cola.popleft()
        return auto
