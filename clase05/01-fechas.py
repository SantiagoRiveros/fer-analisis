import pandas as pd

ventas = pd.DataFrame({
    "Fecha": [
        "2025-01-10",
        "2025-02-15",
        "2025-03-20"
    ],
    "Total": [100, 200, 300]
})

# Vamos a evaluar aca los tipos
print(ventas.info())

# El problema de la fecha -> Sigue siendo un string

# Lo pasamos a datetime, asi pandas interpreta dia mes y año

ventas["Fecha"] = pd.to_datetime(ventas["Fecha"])

print(ventas.info())

# Ventajas?
print(ventas["Fecha"].dt.year)

print(ventas["Fecha"].dt.month)

print(ventas["Fecha"].dt.day)

# Vamos a crear columna nueva "mes"


ventas["Año"] = ventas["Fecha"].dt.year

ventas["Mes"] = ventas["Fecha"].dt.month

ventas["Dia"] = ventas["Fecha"].dt.day

print(ventas)

# Supongamos que yo quiero mostrar,  las ventas de febrero en adelante
print(ventas[ventas["Fecha"] > "2025-02-01"])

print(ventas[(ventas["Mes"] >= 2) & (ventas["Año"] == 2025)])

""" 
Podemos hacer rangos
Comparaciones
Analisis Temporal
"""
