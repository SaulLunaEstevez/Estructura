# Importamos las bibliotecas necesarias.
import tkinter as tk
from tkinter import simpledialog, messagebox

# Definimos la clase Paciente, que representa a un paciente individual.
class Paciente:
    # Constructor de la clase Paciente.
    def __init__(self, nombre, edad, genero, telefono, diagnostico):
        self.nombre = nombre  # Nombre del paciente.
        self.edad = edad  # Edad del paciente.
        self.genero = genero  # Género del paciente.
        self.telefono = telefono  # Teléfono del paciente.
        self.diagnostico = diagnostico  # Diagnóstico del paciente.

    # Representación en cadena del objeto Paciente.
    def __str__(self):
        return f"{self.nombre}, {self.edad} años, {self.genero}, Tel: {self.telefono}, Diagnóstico: {self.diagnostico}"

# Clase para mantener un registro de pacientes.
class RegistroPacientes:
    # Constructor de la clase RegistroPacientes.
    def __init__(self):
        self.pacientes = []  # Lista para almacenar pacientes.

    # Método para agregar un paciente al registro.
    def agregar_paciente(self, paciente):
        self.pacientes.append(paciente)  # Añade el paciente a la lista.

    # Método recursivo para buscar un paciente por nombre.
    def buscar_paciente(self, nombre, index=0):
        # Si el índice actual es menor que la cantidad de pacientes...
        if index < len(self.pacientes):
            # ... y el nombre del paciente actual coincide con el buscado.
            if self.pacientes[index].nombre.lower() == nombre.lower():
                return self.pacientes[index]  # Retorna el paciente.
            # Si no coincide, sigue buscando en el próximo índice.
            return self.buscar_paciente(nombre, index+1)
        return None  # Retorna None si no encuentra el paciente.

    # Método para buscar pacientes por diagnóstico.
    def buscar_por_diagnostico(self, diagnostico):
        # Usa comprensión de lista para filtrar pacientes por diagnóstico.
        return [paciente for paciente in self.pacientes if paciente.diagnostico.lower() == diagnostico.lower()]

    # Método para eliminar un paciente por nombre.
    def eliminar_paciente(self, nombre):
        paciente = self.buscar_paciente(nombre)  # Busca al paciente por nombre.
        if paciente:  # Si encuentra el paciente...
            self.pacientes.remove(paciente)  # ... lo elimina de la lista.

    # Método para obtener estadísticas.
    def estadisticas(self):
        total_pacientes = len(self.pacientes)  # Cuenta el total de pacientes.
        # Calcula la edad promedio. Si no hay pacientes, la edad promedio es 0.
        edad_promedio = sum([paciente.edad for paciente in self.pacientes]) / total_pacientes if total_pacientes > 0 else 0
        return total_pacientes, edad_promedio

# Clase para la aplicación de interfaz gráfica.
class App:
    # Constructor de la clase App.
    def __init__(self, master):
        self.master = master  # Ventana principal.
        self.master.title("Sistema de Registro de Pacientes")
        self.registro = RegistroPacientes()  # Crea un registro de pacientes.

        # Botones y sus acciones asociadas.
        self.btn_agregar = tk.Button(master, text="Agregar paciente", command=self.agregar_paciente)
        self.btn_agregar.pack(pady=10)

        self.btn_buscar_nombre = tk.Button(master, text="Buscar paciente por nombre", command=self.buscar_paciente_nombre)
        self.btn_buscar_nombre.pack(pady=10)

        self.btn_buscar_diagnostico = tk.Button(master, text="Buscar por diagnóstico", command=self.buscar_paciente_diagnostico)
        self.btn_buscar_diagnostico.pack(pady=10)

        self.btn_mostrar = tk.Button(master, text="Mostrar todos los pacientes", command=self.mostrar_pacientes)
        self.btn_mostrar.pack(pady=10)

        self.btn_eliminar = tk.Button(master, text="Eliminar paciente", command=self.eliminar_paciente)
        self.btn_eliminar.pack(pady=10)

        self.btn_estadisticas = tk.Button(master, text="Estadísticas", command=self.estadisticas)
        self.btn_estadisticas.pack(pady=10)

        self.btn_salir = tk.Button(master, text="Salir", command=master.quit)
        self.btn_salir.pack(pady=10)

    # Método para agregar un paciente.
    def agregar_paciente(self):
        # Solicita datos del paciente mediante cuadros de diálogo.
        nombre = simpledialog.askstring("Agregar paciente", "Nombre Completo:")
        edad = simpledialog.askinteger("Agregar paciente", "Edad:")
        genero = simpledialog.askstring("Agregar paciente", "Género:")
        telefono = simpledialog.askstring("Agregar paciente", "Teléfono:")
        diagnostico = simpledialog.askstring("Agregar paciente", "Diagnóstico:")

        # Valida que ninguno de los valores sea nulo.
        if all([nombre, edad, genero, telefono, diagnostico]):
            paciente = Paciente(nombre, edad, genero, telefono, diagnostico)
            self.registro.agregar_paciente(paciente)
            messagebox.showinfo("Agregar paciente", "Paciente agregado con éxito.")
        else:
            messagebox.showerror("Agregar paciente", "Todos los campos son obligatorios.")

    # Método para buscar un paciente por nombre.
    def buscar_paciente_nombre(self):
        nombre = simpledialog.askstring("Buscar paciente", "Nombre a buscar:")
        if nombre:
            paciente = self.registro.buscar_paciente(nombre)
            if paciente:
                messagebox.showinfo("Buscar paciente", str(paciente))
            else:
                messagebox.showerror("Buscar paciente", "Paciente no encontrado.")

    # Método para buscar pacientes por diagnóstico.
    def buscar_paciente_diagnostico(self):
        diagnostico = simpledialog.askstring("Buscar por diagnóstico", "Diagnóstico a buscar:")
        if diagnostico:
            pacientes = self.registro.buscar_por_diagnostico(diagnostico)
            info = "\n".join([str(paciente) for paciente in pacientes])
            if pacientes:
                messagebox.showinfo("Buscar por diagnóstico", info)
            else:
                messagebox.showerror("Buscar por diagnóstico", "No hay pacientes con ese diagnóstico.")

    # Método para mostrar todos los pacientes.
    def mostrar_pacientes(self):
        info = "\n".join([str(paciente) for paciente in self.registro.pacientes])
        if info:
            messagebox.showinfo("Mostrar pacientes", info)
        else:
            messagebox.showinfo("Mostrar pacientes", "No hay pacientes registrados.")

    # Método para eliminar un paciente.
    def eliminar_paciente(self):
        nombre = simpledialog.askstring("Eliminar paciente", "Nombre del paciente a eliminar:")
        if nombre:
            self.registro.eliminar_paciente(nombre)
            messagebox.showinfo("Eliminar paciente", "Paciente eliminado con éxito.")

    # Método para mostrar estadísticas.
    def estadisticas(self):
        total, promedio = self.registro.estadisticas()
        info = f"Total de pacientes: {total}\nEdad promedio: {promedio:.2f}"
        messagebox.showinfo("Estadísticas", info)

# Punto de entrada principal del programa.
if __name__ == "__main__":
    root = tk.Tk()  # Crea la ventana principal.
    app = App(root)  # Crea la aplicación.
    root.mainloop()  # Ejecuta el bucle principal de la aplicación.
