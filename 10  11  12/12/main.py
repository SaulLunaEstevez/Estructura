import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from cliente import Cliente
from banco import Banco

class AppBanco:
    def __init__(self, root):
        self.banco = Banco()
        self.root = root
        self.root.title("Ventanilla de Banco")
        
        # No. Turno
        self.label_turno = ttk.Label(root, text="No. Turno")
        self.label_turno.grid(row=0, column=0)
        
        self.turno_var = tk.StringVar()
        self.turno_var.set(self.banco.turno_actual)
        self.entry_turno = ttk.Entry(root, textvariable=self.turno_var, state='readonly')
        self.entry_turno.grid(row=0, column=1)


        # Nombre
        self.label_nombre = ttk.Label(root, text="Nombre del Cliente")
        self.label_nombre.grid(row=1, column=0)
        self.entry_nombre = ttk.Entry(root)
        self.entry_nombre.grid(row=1, column=1)

        # Tipo de Movimiento
        self.label_movimiento = ttk.Label(root, text="Tipo de Movimiento")
        self.label_movimiento.grid(row=2, column=0)
        self.movimientos = ["Pago de servicio", "Depósito", "Retiro", "Compra de tiempo-aire", "Consulta de saldo"]
        self.combobox_movimiento = ttk.Combobox(root, values=self.movimientos, state='readonly')
        self.combobox_movimiento.grid(row=2, column=1)
        self.combobox_movimiento.set(self.movimientos[0])

        # Listbox para registros
        self.listbox = tk.Listbox(root, height=10, width=50)
        self.listbox.grid(row=5, column=0, columnspan=2)

        # Botón para agregar a la cola
        self.button_agregar = ttk.Button(root, text="Agregar a la Cola", command=self.agregar_cliente)
        self.button_agregar.grid(row=3, column=0, columnspan=2)

        # Botón para atender al cliente
        self.button_atender = ttk.Button(root, text="Atender en Ventanilla", command=self.atender)
        self.button_atender.grid(row=4, column=0, columnspan=2)

    def agregar_cliente(self):
        turno = self.banco.turno_actual
        nombre = self.entry_nombre.get()
        tipo_movimiento = self.combobox_movimiento.get()
        hora_llegada = datetime.now()

        cliente = Cliente(turno, nombre, tipo_movimiento, hora_llegada)
        if self.banco.inserta_cliente(cliente):
            self.entry_turno.config(state=tk.NORMAL)
            self.entry_turno.delete(0, tk.END)
            self.entry_turno.insert(0, self.banco.turno_actual)
            self.entry_turno.config(state='readonly')
            self.listbox.insert(tk.END, f"Turno {turno}: {nombre} - {tipo_movimiento} - {hora_llegada.strftime('%H:%M:%S')}")
            self.entry_nombre.delete(0, tk.END)  # Limpiar el nombre para el siguiente cliente
        else:
            messagebox.showerror("Error", "La cola está llena.")

    def atender(self):
        cliente_atendido = self.banco.atender_cliente()
        if cliente_atendido:
            espera = datetime.now() - cliente_atendido.hora_llegada
            minutos, segundos = divmod(espera.seconds, 60)
            messagebox.showinfo("Información", f"Atendiendo a {cliente_atendido.nombre}.\n"
                                               f"Turno: {cliente_atendido.turno}\n"
                                               f"Motivo: {cliente_atendido.tipo_movimiento}\n"
                                               f"Hora de llegada: {cliente_atendido.hora_llegada.strftime('%H:%M:%S')}\n"
                                               f"Tiempo de espera: {minutos} minutos {segundos} segundos")
            self.listbox.delete(0)  # Eliminar el cliente atendido del listbox
        else:
            messagebox.showerror("Error", "No hay clientes en la cola.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AppBanco(root)
    root.mainloop()
