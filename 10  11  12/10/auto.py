# auto.py
from datetime import datetime

class Auto:
    def __init__(self, placas, propietario):
        self.placas = placas
        self.propietario = propietario
        self.hora_entrada = datetime.now()

    def calcular_costo(self):
        tiempo_estacionado = datetime.now() - self.hora_entrada
        costo = tiempo_estacionado.total_seconds() * 2.00  # $2.00 por segundo
        return costo

    def __str__(self):
        return f"Placas: {self.placas}, Propietario: {self.propietario}, Hora de Entrada: {self.hora_entrada}"
