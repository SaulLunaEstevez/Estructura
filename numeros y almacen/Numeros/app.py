import tkinter as tk
from tkinter import messagebox
from numeros import GeneradorNumeros

class App:
    def __init__(self, root):
        self.generador = GeneradorNumeros()

        self.generate_btn = tk.Button(root, text="Generar números aleatorios", command=self.generar_numeros)
        self.generate_btn.pack(pady=10)

        self.separate_btn = tk.Button(root, text="Separar pares e impares", command=self.separar_numeros)
        self.separate_btn.pack(pady=10)

        self.all_numbers_listbox = tk.Listbox(root, width=50)
        self.all_numbers_listbox.pack(pady=10)

        self.pares_listbox = tk.Listbox(root, width=50)
        self.pares_listbox.pack(pady=10)

        self.impares_listbox = tk.Listbox(root, width=50)
        self.impares_listbox.pack(pady=10)

    def generar_numeros(self):
        self.generador.generar()
        self.actualizar_display()

    def separar_numeros(self):
        self.generador.separar()
        self.actualizar_display()

    def actualizar_display(self):
        self.all_numbers_listbox.delete(0, tk.END)
        for num in self.generador.numeros:
            self.all_numbers_listbox.insert(tk.END, str(num))

        self.pares_listbox.delete(0, tk.END)
        for num in self.generador.pares:
            self.pares_listbox.insert(tk.END, str(num))

        self.impares_listbox.delete(0, tk.END)
        for num in self.generador.impares:
            self.impares_listbox.insert(tk.END, str(num))

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Pares e Impares")
    app = App(root)
    root.mainloop()
