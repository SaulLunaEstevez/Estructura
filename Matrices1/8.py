# Definición de una clase llamada CuadroMagico
class CuadroMagico:
    # Constructor de la clase, recibe una matriz como argumento
    def __init__(self, matriz):
        self.matriz = matriz  # Almacena la matriz como un atributo de la instancia
        self.n = len(matriz)  # Calcula la dimensión de la matriz y la almacena en 'n'

    # Método para verificar si la matriz es un cuadro mágico
    def es_cuadro_magico(self):
        # Calcular la suma de la primera fila (será la constante mágica)
        constante_magica = sum(self.matriz[0])

        # Verificar la suma de las filas
        for fila in self.matriz:
            if sum(fila) != constante_magica:
                return False

        # Verificar la suma de las columnas
        for j in range(self.n):
            suma_columna = sum(self.matriz[i][j] for i in range(self.n))
            if suma_columna != constante_magica:
                return False

        # Verificar la suma de la diagonal principal
        suma_diagonal_principal = sum(self.matriz[i][i] for i in range(self.n))
        if suma_diagonal_principal != constante_magica:
            return False

        # Verificar la suma de la diagonal secundaria
        suma_diagonal_secundaria = sum(self.matriz[i][self.n - 1 - i] for i in range(self.n))
        if suma_diagonal_secundaria != constante_magica:
            return False

        return constante_magica  # Si todo está bien, devuelve la constante mágica

    # Método para obtener la constante mágica del cuadro (llama al método es_cuadro_magico)
    def obtener_constante_magica(self):
        return self.es_cuadro_magico()

# Bloque principal del programa
try:
    # Solicitar al usuario que ingrese el tamaño del cuadro mágico (n)
    n = int(input("Ingrese el tamaño del cuadro mágico (n): "))

    # Verificar si el tamaño es menor que 2
    if n < 2:
        print("El tamaño del cuadro mágico debe ser al menos 2x2.")
    else:
        matriz = []
        # Solicitar al usuario que ingrese los valores de cada fila
        for i in range(n):
            fila = list(map(int, input(f"Ingrese los valores de la fila {i + 1} separados por espacios: ").split()))
            # Verificar si la fila tiene la longitud correcta
            if len(fila) != n:
                print("La fila no tiene la longitud correcta.")
                break
            matriz.append(fila)

        # Crear una instancia de la clase CuadroMagico con la matriz ingresada
        cuadro_magico = CuadroMagico(matriz)
        # Obtener la constante mágica llamando al método obtener_constante_magica
        constante = cuadro_magico.obtener_constante_magica()

        # Imprimir el resultado
        if constante:
            print(f"Es un cuadro mágico con constante mágica {constante}.")
        else:
            print("No es un cuadro mágico.")
except ValueError:
    print("Por favor, ingrese un número válido para el tamaño del cuadro mágico.")
