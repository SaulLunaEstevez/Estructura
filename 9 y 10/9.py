class Matriz2x2:
    def __init__(self, fila1, fila2):
        # Constructor de la clase Matriz2x2, inicializa la matriz con las dos filas
        self.matriz = [fila1, fila2]

    @staticmethod
    def leer_matriz(numero_matriz):
        # Método estático para leer una matriz de 2x2 desde la entrada del usuario
        print(f"Ingrese los valores de la matriz {numero_matriz} (2x2):")
        fila1 = [float(input(f"Ingrese el valor en la fila 1, columna 1: ")),
                 float(input(f"Ingrese el valor en la fila 1, columna 2: "))]
        fila2 = [float(input(f"Ingrese el valor en la fila 2, columna 1: ")),
                 float(input(f"Ingrese el valor en la fila 2, columna 2: "))]
        return Matriz2x2(fila1, fila2)

    def __str__(self):
        # Método especial para convertir la matriz en una cadena
        return "\n".join([str(fila) for fila in self.matriz])

    def suma(self, otra_matriz):
        # Método para sumar dos matrices y devolver el resultado
        resultado = []
        for i in range(2):  # Itera a través de las filas (0 y 1) de la matriz
            fila = []
            for j in range(2):  # Itera a través de las columnas (0 y 1) de la matriz
                suma = self.matriz[i][j] + otra_matriz.matriz[i][j]  # Suma los elementos correspondientes
                fila.append(suma)  # Agrega el resultado a la fila
            resultado.append(fila)  # Agrega la fila al resultado
        return Matriz2x2(resultado[0], resultado[1])  # Devuelve una nueva matriz con el resultado

    def resta(self, otra_matriz):
        # Método para restar dos matrices y devolver el resultado
        resultado = []
        for i in range(2):  # Itera a través de las filas (0 y 1) de la matriz
            fila = []
            for j in range(2):  # Itera a través de las columnas (0 y 1) de la matriz
                resta = self.matriz[i][j] - otra_matriz.matriz[i][j]  # Resta los elementos correspondientes
                fila.append(resta)  # Agrega el resultado a la fila
            resultado.append(fila)  # Agrega la fila al resultado
        return Matriz2x2(resultado[0], resultado[1])  # Devuelve una nueva matriz con el resultado

    def producto(self, otra_matriz):
        # Método para multiplicar dos matrices elemento por elemento y devolver el resultado
        resultado = []
        for i in range(2):  # Itera a través de las filas (0 y 1) de la matriz
            fila = []
            for j in range(2):  # Itera a través de las columnas (0 y 1) de la matriz
                producto = self.matriz[i][j] * otra_matriz.matriz[i][j]  # Multiplica los elementos correspondientes
                fila.append(producto)  # Agrega el resultado a la fila
            resultado.append(fila)  # Agrega la fila al resultado
        return Matriz2x2(resultado[0], resultado[1])  # Devuelve una nueva matriz con el resultado

    def division(self, otra_matriz):
        # Método para dividir dos matrices elemento por elemento y devolver el resultado
        resultado = []
        for i in range(2):  # Itera a través de las filas (0 y 1) de la matriz
            fila = []
            for j in range(2):  # Itera a través de las columnas (0 y 1) de la matriz
                if otra_matriz.matriz[i][j] == 0:
                    # Manejo de error si el divisor es cero
                    print("Error: No se puede dividir por cero.")
                    return None
                division = self.matriz[i][j] / otra_matriz.matriz[i][j]  # Divide los elementos correspondientes
                fila.append(division)  # Agrega el resultado a la fila
            resultado.append(fila)  # Agrega la fila al resultado
        return Matriz2x2(resultado[0], resultado[1])  # Devuelve una nueva matriz con el resultado

# Leer las dos matrices
matriz1 = Matriz2x2.leer_matriz(1)
matriz2 = Matriz2x2.leer_matriz(2)

# Calcular y mostrar los resultados
print("Matriz 1:")
print(matriz1)

print("Matriz 2:")
print(matriz2)

resultado_suma = matriz1.suma(matriz2)
resultado_resta = matriz1.resta(matriz2)
resultado_producto = matriz1.producto(matriz2)
resultado_division = matriz1.division(matriz2)

if resultado_suma:
    # Mostrar el resultado de la suma si no es None
    print("Suma de las matrices:")
    print(resultado_suma)

if resultado_resta:
    # Mostrar el resultado de la resta si no es None
    print("Resta de las matrices:")
    print(resultado_resta)

print("Producto de las matrices:")
print(resultado_producto)

if resultado_division:
    # Mostrar el resultado de la división si no es None
    print("División de las matrices:")
    print(resultado_division)
