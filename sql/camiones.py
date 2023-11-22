import tkinter as tk
from tkinter import messagebox
import sqlite3

# Conectar a la base de datos SQLite
conn = sqlite3.connect('refaccioneria.db')
c = conn.cursor()

# Funciones de la aplicación
def agregar_camion():
    nombre = entry_nombre.get()
    almacenaje = entry_almacenaje.get()
    placas = entry_placas.get()
    marca = entry_marca.get()

    c.execute("INSERT INTO Camiones (nombre, totalAlmacenaje, placas, marca) VALUES (?, ?, ?, ?)",
              (nombre, almacenaje, placas, marca))
    conn.commit()
    mostrar_camiones()
    messagebox.showinfo("Información", "Camión agregado con éxito")

def actualizar_camion():
    nombre = entry_nombre.get()
    almacenaje = entry_almacenaje.get()
    placas = entry_placas.get()
    marca = entry_marca.get()

    c.execute("UPDATE Camiones SET totalAlmacenaje=?, placas=?, marca=? WHERE nombre=?",
              (almacenaje, placas, marca, nombre))
    conn.commit()
    mostrar_camiones()
    messagebox.showinfo("Información", "Camión actualizado con éxito")

def eliminar_camion():
    nombre = entry_nombre.get()
    c.execute("DELETE FROM Camiones WHERE nombre=?", (nombre,))
    conn.commit()
    mostrar_camiones()
    messagebox.showinfo("Información", "Camión eliminado con éxito")

def buscar_camion():
    nombre_busqueda = entry_buscar.get()
    c.execute("SELECT * FROM Camiones WHERE nombre LIKE ?", ('%' + nombre_busqueda + '%',))
    camiones = c.fetchall()
    lista_camiones.delete(0, tk.END)
    for camion in camiones:
        lista_camiones.insert(tk.END, camion)

def mostrar_camiones():
    c.execute("SELECT * FROM Camiones")
    camiones = c.fetchall()
    lista_camiones.delete(0, tk.END)
    for camion in camiones:
        lista_camiones.insert(tk.END, camion)

# Creación de la ventana principal
window = tk.Tk()
window.title("Gestión de Camiones")

# Creación de widgets
label_nombre = tk.Label(window, text="Nombre:")
label_nombre.grid(row=0, column=0)
entry_nombre = tk.Entry(window)
entry_nombre.grid(row=0, column=1)

label_almacenaje = tk.Label(window, text="Total Almacenaje:")
label_almacenaje.grid(row=1, column=0)
entry_almacenaje = tk.Entry(window)
entry_almacenaje.grid(row=1, column=1)

label_placas = tk.Label(window, text="Placas:")
label_placas.grid(row=2, column=0)
entry_placas = tk.Entry(window)
entry_placas.grid(row=2, column=1)

label_marca = tk.Label(window, text="Marca:")
label_marca.grid(row=3, column=0)
entry_marca = tk.Entry(window)
entry_marca.grid(row=3, column=1)

btn_agregar = tk.Button(window, text="Agregar", command=agregar_camion)
btn_agregar.grid(row=4, column=0)

btn_actualizar = tk.Button(window, text="Actualizar", command=actualizar_camion)
btn_actualizar.grid(row=4, column=1)

btn_eliminar = tk.Button(window, text="Eliminar", command=eliminar_camion)
btn_eliminar.grid(row=4, column=2)

label_buscar = tk.Label(window, text="Buscar Nombre:")
label_buscar.grid(row=5, column=0)
entry_buscar = tk.Entry(window)
entry_buscar.grid(row=5, column=1)
btn_buscar = tk.Button(window, text="Buscar/mostrar", command=buscar_camion)
btn_buscar.grid(row=5, column=2)

lista_camiones = tk.Listbox(window)
lista_camiones.grid(row=6, column=0, columnspan=3, sticky="nsew")

# Configurar la ventana para que los widgets se ajusten al cambiar el tamaño
window.grid_rowconfigure(6, weight=1)
window.grid_columnconfigure(1, weight=1)

mostrar_camiones()

# Ejecución de la aplicación
window.mainloop()

# Cerrar conexión a la base de datos
conn.close()
