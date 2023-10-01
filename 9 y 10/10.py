class EliminacionGaussiana:
    def __init__(self, matriz):
        # Constructor: inicializa la instancia de la clase con una matriz.
        self.matriz = matriz

    def intercambiar_filas(self, fila1, fila2):
        # Método para intercambiar dos filas en la matriz.
        self.matriz[fila1], self.matriz[fila2] = self.matriz[fila2], self.matriz[fila1]

    def multiplicar_fila(self, fila, constante):
        # Método para multiplicar una fila entera por una constante.
        self.matriz[fila] = [elemento * constante for elemento in self.matriz[fila]]

    def restar_filas(self, fila1, fila2, factor):
        # Método para restar una fila multiplicada por un factor de otra fila.
        self.matriz[fila1] = [elem1 - elem2 * factor for elem1, elem2 in zip(self.matriz[fila1], self.matriz[fila2])]

    def imprimir_matriz(self):
        # Método para imprimir la matriz actual.
        for fila in self.matriz:
            print(fila)

    def gauss(self):
        # Método principal que realiza la eliminación de Gauss.
        self._eliminacion_hacia_adelante()
        self._eliminacion_hacia_atras()
        self._normalizar_filas()

    def _eliminacion_hacia_adelante(self):
        # Método privado que realiza la eliminación hacia adelante.
        filas, columnas = len(self.matriz), len(self.matriz[0])

        for i in range(min(filas, columnas - 1)):
            # Bucle para encontrar el máximo elemento en la columna actual.
            max_elemento = max(range(i, filas), key=lambda x: abs(self.matriz[x][i]))
            # Intercambia las filas para poner el máximo elemento en la fila actual.
            self.intercambiar_filas(i, max_elemento)

            for j in range(i + 1, filas):
                # Bucle para hacer ceros debajo del elemento diagonal.
                factor = self.matriz[j][i] / self.matriz[i][i]
                self.restar_filas(j, i, factor)

    def _eliminacion_hacia_atras(self):
        # Método privado que realiza la eliminación hacia atrás.
        filas = len(self.matriz)

        for i in range(filas - 1, 0, -1):
            for j in range(i - 1, -1, -1):
                # Bucle para hacer ceros por encima del elemento diagonal.
                factor = self.matriz[j][i] / self.matriz[i][i]
                self.restar_filas(j, i, factor)

    def _normalizar_filas(self):
        # Método privado para normalizar las filas de la matriz.
        filas = len(self.matriz)
        for i in range(filas):
            factor = 1 / self.matriz[i][i]
            self.multiplicar_fila(i, factor)

# Ejemplo de uso
matriz = [
    [2, -1, 1],
    [-3, 0, 1],
    [-1, 3, -2]
]

solver = EliminacionGaussiana(matriz)
print("Matriz original:")
solver.imprimir_matriz()
solver.gauss()

print("\nMatriz después de Gauss:")
solver.imprimir_matriz()
