# Definición de la clase Calificaciones
class Calificaciones:
    # El método __init__ se llama cuando se crea una instancia de la clase y recibe la tabla de calificaciones como argumento
    def __init__(self, tabla):
        self.tabla = tabla  # Almacena la tabla de calificaciones como un atributo de la instancia

    # Método para calcular el promedio de cada alumno
    def promedio_alumnos(self):
        promedios = []  # Lista para almacenar los promedios
        for fila in self.tabla:  # Itera a través de cada fila de la tabla (cada fila representa un alumno)
            promedio = sum(fila) / len(fila)  # Calcula el promedio de las calificaciones en la fila
            promedios.append(promedio)  # Agrega el promedio a la lista
        return promedios  # Retorna la lista de promedios

    # Método para encontrar el promedio más alto
    def promedio_mas_alto(self):
        return max(self.promedio_alumnos())  # Utiliza el método promedio_alumnos y encuentra el máximo

    # Método para encontrar el promedio más bajo
    def promedio_mas_bajo(self):
        return min(self.promedio_alumnos())  # Utiliza el método promedio_alumnos y encuentra el mínimo

    # Método para contar la cantidad de parciales reprobados (menores a 7.0)
    def parciales_reprobados(self):
        reprobados = 0  # Variable para contar los reprobados
        for fila in self.tabla:  # Itera a través de cada fila de la tabla
            for nota in fila:  # Itera a través de cada calificación en la fila
                if nota < 7.0:  # Comprueba si la calificación es menor a 7.0
                    reprobados += 1  # Incrementa el contador si es reprobado
        return reprobados  # Retorna la cantidad de parciales reprobados

    # Método para calcular la distribución de calificaciones finales
    def distribucion_calificaciones(self):
        distribucion = {  # Diccionario para almacenar la distribución
            "0 - 4.9": 0,
            "5.0 - 5.9": 0,
            "6.0 - 6.9": 0,
            "7.0 - 7.9": 0,
            "8.0 - 8.9": 0,
            "9.0 - 10": 0
        }
        for promedio in self.promedio_alumnos():  # Itera a través de los promedios de los alumnos
            if promedio < 5.0:  # Comprueba el rango y actualiza el contador correspondiente
                distribucion["0 - 4.9"] += 1
            elif promedio < 6.0:
                distribucion["5.0 - 5.9"] += 1
            elif promedio < 7.0:
                distribucion["6.0 - 6.9"] += 1
            elif promedio < 8.0:
                distribucion["7.0 - 7.9"] += 1
            elif promedio < 9.0:
                distribucion["8.0 - 8.9"] += 1
            else:
                distribucion["9.0 - 10"] += 1
        return distribucion  # Retorna el diccionario de distribución

# Datos de la tabla de calificaciones
tabla_calificaciones = [
    [5.5, 8.6, 10],
    [8.0, 5.5, 10],
    [9.0, 4.1, 7.8],
    [10, 2.2, 8.1],
    [7.0, 9.2, 7.1],
    [9.0, 4.0, 6.0],
    [6.5, 5.0, 5.0],
    [4.0, 7.0, 4.0],
    [8.0, 8.0, 9.0],
    [10, 9.0, 9.2],
    [5.0, 10, 8.4],
    [9.0, 4.6, 7.5]
]

# Crear una instancia de la clase Calificaciones
calificaciones = Calificaciones(tabla_calificaciones)

# Obtener los resultados e imprimirlos
print("a) Promedio de cada alumno:")
promedios_alumnos = calificaciones.promedio_alumnos()
for i, promedio in enumerate(promedios_alumnos, start=1):
    print(f"Alumno {i}: {promedio:.2f}")

print("\nb) Promedio más alto:")
print(calificaciones.promedio_mas_alto())

print("\nc) Promedio más bajo:")
print(calificaciones.promedio_mas_bajo())

print("\nd) Parciales reprobados:")
print(calificaciones.parciales_reprobados())

print("\ne) Distribución de calificaciones finales:")
distribucion = calificaciones.distribucion_calificaciones()
for rango, cantidad in distribucion.items():
    print(f"{rango}: {cantidad} Alumnos")
