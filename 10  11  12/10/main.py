# main.py
import tkinter as tk
from estacionamiento import Estacionamiento

class Aplicacion:
    def __init__(self, root):
        self.estacionamiento = Estacionamiento()
        self.root = root
        root.title("Sistema de Estacionamiento")

        self.label = tk.Label(root, text="Sistema de Estacionamiento")
        self.label.pack()

        self.placas_label = tk.Label(root, text="Placas:")
        self.placas_label.pack()
        self.placas_entry = tk.Entry(root)
        self.placas_entry.pack()

        self.propietario_label = tk.Label(root, text="Propietario:")
        self.propietario_label.pack()
        self.propietario_entry = tk.Entry(root)
        self.propietario_entry.pack()

        self.entrada_button = tk.Button(root, text="Entrada de Auto", command=self.entrada_auto)
        self.entrada_button.pack()

        self.salida_button = tk.Button(root, text="Salida de Auto", command=self.salida_auto)
        self.salida_button.pack()

        self.resultado = tk.Text(root, height=10, width=50)
        self.resultado.pack()

    def entrada_auto(self):
        placas = self.placas_entry.get()
        propietario = self.propietario_entry.get()
        auto = self.estacionamiento.entrada_auto(placas, propietario)
        self.resultado.insert(tk.END, f'Entrada: {auto}\n')

    def salida_auto(self):
        auto = self.estacionamiento.salida_auto()
        if auto is None:
            self.resultado.insert(tk.END, "Estacionamiento vacío\n")
        else:
            costo = auto.calcular_costo()
            self.resultado.insert(tk.END, f'Salida: {auto}, Costo: ${costo:.2f}\n')

root = tk.Tk()
app = Aplicacion(root)
root.mainloop()
