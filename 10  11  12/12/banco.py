from collections import deque
from cliente import Cliente

class Banco:
    def __init__(self):
        self.cola = deque()
        self.turno_actual = 1

    def cola_llena(self):
        # Puedes definir un límite para tu cola, por ejemplo 50
        return len(self.cola) >= 50

    def inserta_cliente(self, cliente):
        if not self.cola_llena():
            self.cola.append(cliente)
            self.turno_actual += 1
            return True
        return False

    def atender_cliente(self):
        if self.cola:
            return self.cola.popleft()
        return None
