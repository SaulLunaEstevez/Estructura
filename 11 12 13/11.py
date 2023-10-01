import random  # Importar el módulo random para generar números aleatorios.

# Función para generar una matriz de 5x10 con números aleatorios entre 1 y 100
def generar_matriz(filas, columnas):
    matriz = []  # Inicializar una lista vacía llamada 'matriz' para almacenar la matriz.
    for _ in range(filas):  # Iterar sobre el número de filas especificado.
        fila = [random.randint(1, 100) for _ in range(columnas)]  # Generar una fila de números aleatorios y agregarla a 'fila'.
        matriz.append(fila)  # Agregar la fila a la matriz.
    return matriz  # Devolver la matriz generada.

# Función para calcular la suma y el promedio de cada fila y columna
def calcular_suma_promedio(matriz):
    filas = len(matriz)  # Obtener el número de filas en la matriz.
    columnas = len(matriz[0])  # Obtener el número de columnas en la matriz. Se asume que todas las filas tienen la misma longitud.
    suma_filas = []  # Inicializar una lista vacía para almacenar las sumas de las filas.
    promedio_filas = []  # Inicializar una lista vacía para almacenar los promedios de las filas.
    suma_columnas = []  # Inicializar una lista vacía para almacenar las sumas de las columnas.
    promedio_columnas = []  # Inicializar una lista vacía para almacenar los promedios de las columnas.

    for i in range(filas):
        # Calcular la suma de la fila actual utilizando la función sum() y agregarla a la lista suma_filas.
        suma_fila = sum(matriz[i])
        promedio_fila = suma_fila / columnas  # Calcular el promedio de la fila actual.
        suma_filas.append(suma_fila)  # Agregar la suma de la fila a la lista suma_filas.
        promedio_filas.append(promedio_fila)  # Agregar el promedio de la fila a la lista promedio_filas.

    for j in range(columnas):
        # Calcular la suma de la columna actual utilizando una comprensión de lista y agregarla a la lista suma_columnas.
        suma_columna = sum(matriz[i][j] for i in range(filas))
        promedio_columna = suma_columna / filas  # Calcular el promedio de la columna actual.
        suma_columnas.append(suma_columna)  # Agregar la suma de la columna a la lista suma_columnas.
        promedio_columnas.append(promedio_columna)  # Agregar el promedio de la columna a la lista promedio_columnas.

    return suma_filas, promedio_filas, suma_columnas, promedio_columnas  # Devolver las listas con las sumas y promedios.

# Función para imprimir la matriz y los resultados en el formato deseado
def imprimir_resultados(matriz, suma_filas, promedio_filas, suma_columnas, promedio_columnas):
    filas = len(matriz)  # Obtener el número de filas en la matriz.
    columnas = len(matriz[0])  # Obtener el número de columnas en la matriz. Se asume que todas las filas tienen la misma longitud.

    # Imprimir la matriz y los resultados en el formato deseado
    for i in range(filas):
        for j in range(columnas):
            print(f"{matriz[i][j]:2d}\t", end="")  # Imprimir cada elemento de la matriz con formato de ancho fijo.
        print(f"\t{suma_filas[i]:2d}\t{promedio_filas[i]:.2f}")  # Imprimir la suma y el promedio de la fila.

    for suma in suma_columnas:
        print(f"{suma:.2f}\t", end="")  # Imprimir la suma de cada columna con formato de dos decimales.
    print()

    for promedio in promedio_columnas:
        print(f"{promedio:.2f}\t", end="")  # Imprimir el promedio de cada columna con formato de dos decimales.
    print()

# Generar la matriz
matriz = generar_matriz(5, 10)

# Calcular la suma y el promedio de cada fila y columna
suma_filas, promedio_filas, suma_columnas, promedio_columnas = calcular_suma_promedio(matriz)

# Imprimir la matriz y los resultados en el formato deseado
imprimir_resultados(matriz, suma_filas, promedio_filas, suma_columnas, promedio_columnas)
