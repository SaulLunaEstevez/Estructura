# Definición de una clase llamada Matriz
class Matriz:
    # Constructor de la clase, recibe una matriz como argumento
    def __init__(self, matriz):
        self.matriz = matriz  # Almacena la matriz como un atributo de la instancia

    # Método para contar los ceros en una fila específica
    def contar_ceros_en_fila(self, fila_index):
        fila = self.matriz[fila_index]  # Obtiene la fila específica de la matriz
        contador_ceros = fila.count(0)  # Cuenta la cantidad de ceros en la fila
        return contador_ceros  # Devuelve el resultado

    # Método para contar los ceros en todas las filas de la matriz
    def contar_ceros_en_todas_las_filas(self):
        # Itera sobre las filas de la matriz utilizando un bucle for y enumerate
        for i, fila in enumerate(self.matriz):
            contador_ceros = self.contar_ceros_en_fila(i)  # Llama al método anterior para contar ceros en la fila
            # Imprime el resultado, indicando el número de fila y la cantidad de ceros
            print(f"En la fila {i + 1} hay {contador_ceros} ceros.")

# Definición de una matriz
matriz = [
    [0, 2, 5, 7, 6],
    [0, 0, 0, 3, 8],
    [2, 9, 6, 3, 4],
    [1, 5, 6, 1, 4],
    [0, 9, 2, 5, 0]
]

# Creación de una instancia de la clase Matriz, pasando la matriz como argumento
mi_matriz = Matriz(matriz)

# Llamada al método contar_ceros_en_todas_las_filas de la instancia mi_matriz
mi_matriz.contar_ceros_en_todas_las_filas()