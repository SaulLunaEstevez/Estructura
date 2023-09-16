# Definimos una clase llamada CalculadoraDeCambio para manejar el cálculo del cambio.
class CalculadoraDeCambio:
    def __init__(self, monedas_disponibles):
        # Constructor: inicializa la calculadora con una lista de monedas disponibles.
        self.monedas_disponibles = sorted(monedas_disponibles, reverse=True)

    def calcular_cambio(self, cantidad):
        # Método público para calcular el cambio para una cantidad dada.
        return self._calcular_cambio_recursive(cantidad, 0)

    def _calcular_cambio_recursive(self, cantidad, indice_moneda):
        # Método privado y recursivo para calcular el cambio de manera recursiva.

        # Caso base 1: Si la cantidad es cero, hemos encontrado un conjunto de monedas que suma al cambio.
        if cantidad == 0:
            return {}

        # Caso base 2: Si la cantidad es negativa o hemos agotado todas las monedas disponibles, no hay solución.
        if cantidad < 0 or indice_moneda >= len(self.monedas_disponibles):
            return None

        # Obtenemos el valor de la moneda actual que estamos considerando.
        moneda_actual = self.monedas_disponibles[indice_moneda]

        # Llamada recursiva 1: Usar la moneda actual y reducir la cantidad.
        usar_moneda = self._calcular_cambio_recursive(cantidad - moneda_actual, indice_moneda)

        # Llamada recursiva 2: No usar la moneda actual y pasar a la siguiente.
        no_usar_moneda = self._calcular_cambio_recursive(cantidad, indice_moneda + 1)

        # Si podemos usar la moneda actual, la agregamos a la solución.
        if usar_moneda is not None:
            usar_moneda[moneda_actual] = usar_moneda.get(moneda_actual, 0) + 1
            return usar_moneda

        # Si no podemos usar la moneda actual, seguimos con las siguientes monedas.
        return no_usar_moneda
class TorresDeHanoi:
    def __init__(self):
        pass
    
    
    #ejemplo de uso cambio monedas
# Lista de monedas disponibles
monedas_disponibles = [100, 50, 20, 5, 2, 1, 0.5]

# Cantidad de cambio a calcular
cambio = 188.5

# Creamos una instancia de la CalculadoraDeCambio con las monedas disponibles.
calculadora = CalculadoraDeCambio(monedas_disponibles)

# Llamamos al método calcular_cambio para obtener la solución.
resultado = calculadora.calcular_cambio(cambio)

# Verificamos si se encontró una solución.
if resultado is not None:
    print(f"Para un cambio de {cambio} se necesitan las siguientes monedas:")
    for moneda, cantidad in resultado.items():
        print(f"{cantidad} monedas de {moneda}")
else:
    print("No es posible dar cambio con las monedas disponibles.")