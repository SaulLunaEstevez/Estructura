class TorresDeHanoi:
    def __init__(self):
        pass

    def resolver_hanoi(self, n, origen, destino, auxiliar):
        if n == 1:
            print(f'Mover disco 1 de la torre {origen} a la torre {destino}')
            return  # Caso base: mueve el disco 1 directamente al destino

        # Mueve n-1 discos de origen a auxiliar, usando destino como auxiliar
        self.resolver_hanoi(n - 1, origen, auxiliar, destino)

        # Mueve el disco n de origen a destino
        print(f'Mover disco {n} de la torre {origen} a la torre {destino}')

        # Mueve n-1 discos de auxiliar a destino, usando origen como auxiliar
        self.resolver_hanoi(n - 1, auxiliar, destino, origen)
        
# Ejemplo de uso para las Torres de Hanoi
num_discos = int(input("Ingrese el número de discos: "))

torres_hanoi = TorresDeHanoi()  # Crea un objeto de la clase TorresDeHanoi
torres_hanoi.resolver_hanoi(num_discos, 'A', 'C', 'B')  # Resuelve el problema de las Torres de Hanoi