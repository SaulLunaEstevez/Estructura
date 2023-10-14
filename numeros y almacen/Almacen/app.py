import tkinter as tk
from tkinter import simpledialog, messagebox
from almacen import Almacen

class App:
    def __init__(self, root):
        self.almacen = Almacen()

        self.add_btn = tk.Button(root, text="Agregar producto", command=self.agregar_producto)
        self.add_btn.pack(pady=10)

        self.remove_btn = tk.Button(root, text="Retirar último producto", command=self.retirar_producto)
        self.remove_btn.pack(pady=10)

        self.remove_specific_btn = tk.Button(root, text="Retirar producto específico", command=self.retirar_producto_especifico)
        self.remove_specific_btn.pack(pady=10)

        self.remove_all_btn = tk.Button(root, text="Eliminar todos los productos", command=self.eliminar_todos)
        self.remove_all_btn.pack(pady=10)

        self.decrease_qty_btn = tk.Button(root, text="Disminuir cantidad de producto", command=self.disminuir_cantidad_producto)
        self.decrease_qty_btn.pack(pady=10)

        self.product_listbox = tk.Listbox(root, width=50)
        self.product_listbox.pack(pady=10)

        self.retirados_lbl = tk.Label(root, text="Productos Retirados:")
        self.retirados_lbl.pack(pady=10)

        self.retirados_listbox = tk.Listbox(root, width=50)
        self.retirados_listbox.pack(pady=10)

        self.actualizar_display()

    def agregar_producto(self):
        self.almacen.agregar_producto()
        self.actualizar_display()

    def retirar_producto(self):
        self.almacen.retirar_producto()
        self.actualizar_display()

    def retirar_producto_especifico(self):
        nombre = simpledialog.askstring("Input", "¿Cuál producto quieres retirar?")
        if nombre:
            self.almacen.retirar_producto(nombre)
            self.actualizar_display()

    def eliminar_todos(self):
        self.almacen.eliminar_todos()
        self.actualizar_display()

    def disminuir_cantidad_producto(self):
        nombre = simpledialog.askstring("Input", "¿De qué producto quieres disminuir la cantidad?")
        if nombre:
            if any(p.nombre == nombre for p in self.almacen.mostrar_productos()):
                cantidad_a_disminuir = simpledialog.askinteger("Input", f"¿Cuánto quieres disminuir del {nombre}?", minvalue=1)
                if cantidad_a_disminuir:
                    producto_a_modificar = next(p for p in self.almacen.mostrar_productos() if p.nombre == nombre)
                    if producto_a_modificar.cantidad >= cantidad_a_disminuir:
                        self.almacen.disminuir_cantidad(nombre,cantidad_a_disminuir)
                        producto_a_modificar.cantidad -= cantidad_a_disminuir
                        self.actualizar_display()
                    else:
                        messagebox.showinfo("Info", f"No puedes disminuir más de {producto_a_modificar.cantidad} unidades del {nombre}")
            else:
                messagebox.showinfo("Info", "Producto no encontrado")


    def actualizar_display(self):
        self.product_listbox.delete(0, tk.END)
        for prod in self.almacen.mostrar_productos():
            self.product_listbox.insert(tk.END, str(prod))
        
        self.retirados_listbox.delete(0, tk.END)
        for prod in self.almacen.mostrar_retirados():
            self.retirados_listbox.insert(tk.END, str(prod))

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Almacén de productos")
    app = App(root)
    root.mainloop()
