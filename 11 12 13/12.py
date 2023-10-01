# Declarar e inicializar el arreglo de ventas
ventas = [
    [5, 16, 10, 12, 24],
    [40, 55, 10, 11, 18],
    [15, 41, 78, 14, 51],
    [35, 22, 81, 15, 12],
    [50, 12, 71, 10, 20],
    [70, 40, 60, 28, 22],
    [50, 50, 50, 36, 25],
    [40, 70, 40, 11, 20],
    [20, 20, 30, 12, 18],
    [10, 40, 32, 13, 16],
    [50, 3, 24, 15, 82],
    [40, 46, 15, 46, 22]
]

# Inicializar variables para la menor y mayor venta
venta_minima = float('inf')  # Inicialmente se establece en infinito positivo
venta_maxima = float('-inf')  # Inicialmente se establece en infinito negativo
mes_venta_minima = 0
dia_venta_minima = 0
mes_venta_maxima = 0
dia_venta_maxima = 0

# Inicializar variable para la venta total
venta_total = 0

# Inicializar un diccionario para las ventas por día de la semana
venta_por_dia = {
    'Lunes': 0,
    'Martes': 0,
    'Miércoles': 0,
    'Jueves': 0,
    'Viernes': 0
}

# Recorrer el arreglo de ventas
for mes, ventas_mes in enumerate(ventas, start=1):
    # Iterar sobre cada mes y sus ventas
    for dia, venta_dia in enumerate(ventas_mes, start=1):
        # Actualizar la venta total
        venta_total += venta_dia
        
        # Actualizar la venta mínima y máxima
        if venta_dia < venta_minima:
            venta_minima = venta_dia
            mes_venta_minima = mes
            dia_venta_minima = dia
        if venta_dia > venta_maxima:
            venta_maxima = venta_dia
            mes_venta_maxima = mes
            dia_venta_maxima = dia
        
        # Actualizar las ventas por día de la semana
        dia_semana = dia % 5  # Hay 5 días de la semana (1 a 5)
        if dia_semana == 1:
            venta_por_dia['Lunes'] += venta_dia
        elif dia_semana == 2:
            venta_por_dia['Martes'] += venta_dia
        elif dia_semana == 3:
            venta_por_dia['Miércoles'] += venta_dia
        elif dia_semana == 4:
            venta_por_dia['Jueves'] += venta_dia
        elif dia_semana == 0:
            venta_por_dia['Viernes'] += venta_dia

# Imprimir resultados
print("a) Arreglo de ventas:")
for mes, ventas_mes in enumerate(ventas, start=1):
    print(f"Mes {mes}: {ventas_mes}")

print(f"b) Menor venta realizada: ${venta_minima} en el mes {mes_venta_minima}, día {dia_venta_minima}")
print(f"c) Mayor venta realizada: ${venta_maxima} en el mes {mes_venta_maxima}, día {dia_venta_maxima}")
print(f"d) Venta total: ${venta_total}")

print("e) Ventas por día de la semana:")
for dia, venta_dia in venta_por_dia.items():
    print(f"{dia}: ${venta_dia}")
