# Importamos la biblioteca tkinter, que nos permite crear interfaces gráficas.
# También importamos el valor de pi desde la biblioteca math para calcular áreas y perímetros de círculos.
import tkinter as tk
from math import pi

# Definimos una clase llamada CalculadoraGeometrica.
class CalculadoraGeometrica:
    def __init__(self, ventana):
        # Constructor de la clase. Recibe una ventana como parámetro.

        # Guardamos la ventana en una variable para poder acceder a ella más tarde.
        self.ventana = ventana
        self.ventana.title("Calculadora Geométrica")  # Establecemos el título de la ventana.

        # Etiqueta para seleccionar la figura.
        self.label_tipo = tk.Label(ventana, text="Seleccione una figura:")
        self.label_tipo.pack()  # Empaquetamos la etiqueta en la ventana.

        # Menú desplegable para seleccionar la figura.
        self.figura_var = tk.StringVar()  # Variable para almacenar la opción seleccionada.
        self.figura_var.set("Rectángulo")  # Valor predeterminado.
        # Creamos el menú desplegable con opciones y configuramos la función a llamar cuando cambia la selección.
        self.figura_menu = tk.OptionMenu(ventana, self.figura_var, "Rectángulo", "Círculo", "Cuadrado", "Triángulo", command=self.mostrar_campos)
        self.figura_menu.pack()  # Empaquetamos el menú en la ventana.

        # Etiquetas y campos de entrada para los datos de las figuras.
        self.label_lado1 = tk.Label(ventana, text="Lado 1:")
        self.label_lado2 = tk.Label(ventana, text="Lado 2:")
        self.label_radio = tk.Label(ventana, text="Radio:")
        self.label_base = tk.Label(ventana, text="Base:")
        self.label_altura = tk.Label(ventana, text="Altura:")

        # Campos de entrada.
        self.entry_lado1 = tk.Entry(ventana)
        self.entry_lado2 = tk.Entry(ventana)
        self.entry_radio = tk.Entry(ventana)
        self.entry_base = tk.Entry(ventana)
        self.entry_altura = tk.Entry(ventana)

        # Empaquetamos etiquetas y campos de entrada en la ventana.
        self.label_lado1.pack()
        self.entry_lado1.pack()
        self.label_lado2.pack()
        self.entry_lado2.pack()
        self.label_radio.pack()
        self.entry_radio.pack()
        self.label_base.pack()
        self.entry_base.pack()
        self.label_altura.pack()
        self.entry_altura.pack()

        # Botones para calcular área y perímetro.
        self.boton_calcular_area = tk.Button(ventana, text="Calcular Área", command=self.calcular_area)
        self.boton_calcular_area.pack()  # Empaquetamos el botón en la ventana.

        self.boton_calcular_perimetro = tk.Button(ventana, text="Calcular Perímetro", command=self.calcular_perimetro)
        self.boton_calcular_perimetro.pack()  # Empaquetamos el botón en la ventana.

        # Etiqueta para mostrar el resultado.
        self.label_resultado = tk.Label(ventana, text="")
        self.label_resultado.pack()  # Empaquetamos la etiqueta en la ventana.

    def mostrar_campos(self, *args):
        # Función para mostrar u ocultar campos de acuerdo a la figura seleccionada.

        figura = self.figura_var.get()  # Obtenemos la figura seleccionada.

        # Mostramos u ocultamos los campos según la figura seleccionada.
        if figura == "Rectángulo":
            self.label_lado1.pack()
            self.entry_lado1.pack()
            self.label_lado2.pack()
            self.entry_lado2.pack()
            self.label_radio.pack_forget()
            self.entry_radio.pack_forget()
            self.label_base.pack_forget()
            self.entry_base.pack_forget()
            self.label_altura.pack_forget()
            self.entry_altura.pack_forget()
        elif figura == "Círculo":
            self.label_radio.pack()
            self.entry_radio.pack()
            self.label_lado1.pack_forget()
            self.entry_lado1.pack_forget()
            self.label_lado2.pack_forget()
            self.entry_lado2.pack_forget()
            self.label_base.pack_forget()
            self.entry_base.pack_forget()
            self.label_altura.pack_forget()
            self.entry_altura.pack_forget()
        elif figura == "Cuadrado":
            self.label_lado1.pack()
            self.entry_lado1.pack()
            self.label_radio.pack_forget()
            self.entry_radio.pack_forget()
            self.label_lado2.pack_forget()
            self.entry_lado2.pack_forget()
            self.label_base.pack_forget()
            self.entry_base.pack_forget()
            self.label_altura.pack_forget()
            self.entry_altura.pack_forget()
        elif figura == "Triángulo":
            self.label_base.pack()
            self.entry_base.pack()
            self.label_altura.pack()
            self.entry_altura.pack()
            self.label_lado1.pack()
            self.entry_lado1.pack()
            self.label_lado2.pack()
            self.entry_lado2.pack()
            self.label_radio.pack_forget()
            self.entry_radio.pack_forget()

    def calcular_area(self):
        # Función para calcular el área de la figura seleccionada.

        figura = self.figura_var.get()  # Obtenemos la figura seleccionada.

        # Calculamos el área según la figura seleccionada.
        if figura == "Rectángulo":
            lado1 = float(self.entry_lado1.get())
            lado2 = float(self.entry_lado2.get())
            area = lado1 * lado2
            resultado = f"Área: {area:.2f}"
        elif figura == "Círculo":
            radio = float(self.entry_radio.get())
            area = pi * radio ** 2
            resultado = f"Área: {area:.2f}"
        elif figura == "Cuadrado":
            lado = float(self.entry_lado1.get())
            area = lado ** 2
            resultado = f"Área: {area:.2f}"
        elif figura == "Triángulo":
            base = float(self.entry_base.get())
            altura = float(self.entry_altura.get())
            area = (base * altura) / 2
            resultado = f"Área: {area:.2f}"
        else:
            resultado = "Figura no válida"

        self.label_resultado.config(text=resultado)  # Mostramos el resultado en la etiqueta.

    def calcular_perimetro(self):
        # Función para calcular el perímetro de la figura seleccionada.

        figura = self.figura_var.get()  # Obtenemos la figura seleccionada.

        # Calculamos el perímetro según la figura seleccionada.
        if figura == "Rectángulo":
            lado1 = float(self.entry_lado1.get())
            lado2 = float(self.entry_lado2.get())
            perimetro = 2 * (lado1 + lado2)
            resultado = f"Perímetro: {perimetro:.2f}"
        elif figura == "Círculo":
            radio = float(self.entry_radio.get())
            perimetro = 2 * pi * radio
            resultado = f"Perímetro: {perimetro:.2f}"
        elif figura == "Cuadrado":
            lado = float(self.entry_lado1.get())
            perimetro = 4 * lado
            resultado = f"Perímetro: {perimetro:.2f}"
        elif figura == "Triángulo":
            base = float(self.entry_base.get())
            lado1 = float(self.entry_lado1.get())
            lado2 = float(self.entry_lado2.get())
            perimetro = base + lado1 + lado2
            resultado = f"Perímetro: {perimetro:.2f}"
        else:
            resultado = "Figura no válida"

        self.label_resultado.config(text=resultado)  # Mostramos el resultado en la etiqueta.

# Bloque principal
if __name__ == "__main__":
    ventana = tk.Tk()  # Creamos una ventana principal.
    app = CalculadoraGeometrica(ventana)  # Creamos una instancia de la clase CalculadoraGeometrica.
    ventana.mainloop()  # Iniciamos el bucle principal de la interfaz gráfica.