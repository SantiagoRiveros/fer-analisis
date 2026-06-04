import pandas as pd

df = pd.read_csv("usuarios.csv")

# Medidas de tendencia Central

# Promedio (Mean)
print(df["Total"].mean())

# Que responde? -> Cuanto gasta en promedio un cliente

# Mediana (Median)
print(df["Total"].median())
# 1, 2, 3, 650, 651, 652, 653
# Que responde? -> Cual es el valor "central" del dataset

# Moda (Mode)
print(df["Producto"].mode())

# ¿Cual es el producto mas comprado?

# Medidas de dispersion
print(df["Total"].min())

print(df["Total"].max())

# Rango
print(df["Total"].max() - df["Total"].min())

# Desviacion estandar
print(df["Total"].std())
# Si es un numero bajo -> Los numeros son "parecidos"
# Si son altos -> Los numeros estan dispersos

# Cuartiles
Q1 = df["Total"].quantile(0.25)
Q2 = df["Total"].quantile(0.50)
Q3 = df["Total"].quantile(0.75)

IQR = Q3 - Q1
limiteInferior = Q1 - 1.5 * IQR
limiteSuperior = Q3 + 1.5 * IQR
# Limites y IQR
print("limite inferior:", limiteInferior)
print("limite superior:", limiteSuperior)

print("Q1:", Q1)
print("Q2:", Q2)
print("Q3:", Q3)

outliers = df[(df["Total"] < limiteInferior) | (df["Total"] > limiteSuperior)]
print(outliers)

# Correlacion
datos = pd.DataFrame({
    "Horas": [1, 2, 3, 4, 5],
    "Nota": [2, 4, 6, 8, 10],
    "Stress": [10, 8, 6, 4, 2],
    "Random": [31, 2, 149, 0, 1]
})
# 1 -> Correlacion positiva perfecta, -1 -> Correlacion negativa perfecta
correlacion = datos.corr(numeric_only=True)
print(correlacion)
# Positiva perfecta -> Ej: A aumenta 1, B aumenta 2, se mantiene esto, es perfecta
# Negativa perfecta -> A Aumenta 1, B disminuye 2, se mantiene esto, es perfecta

""" 
1 → relación positiva fuerte
0 → sin relación
-1 → relación negativa fuerte
"""

ventas = pd.DataFrame({
    "Publicidad": [100, 200, 300, 400, 500],
    "Ventas": [1000, 1800, 2800, 3500, 5000]
})

correlacion2 = ventas.corr(numeric_only=True)
print(correlacion2)

ventas = pd.DataFrame({
    "Publicidad": [100, 200, 300, 400, 500],
    "Ventas": [1000, 2000, 3000, 4000, 5000]
})

correlacion3 = ventas.corr(numeric_only=True)
print(correlacion3)

""" 
¿Cuántas ventas hay? X
¿Cuántos clientes distintos hay? X
¿Cuántos productos distintos hay? X 
¿Cuál es la venta promedio? X
¿Cuál es la venta más grande? X
¿Cuál es la venta más pequeña? X
¿Cuál es la mediana?
¿Cuál fue el producto más vendido?
¿Qué producto generó más dinero?
¿Qué cliente gastó más?
¿Qué categoría generó más ingresos?
¿Hay ventas atípicas?
¿Cuál podría ser el outlier?
¿Por qué aparece?
¿Qué mes vendió más?
¿Qué cliente realizó más compras?
¿Cuál fue la categoría con mayor ticket promedio?
"""

ventas_tienda = pd.read_csv("ventas_tienda.csv")
print("Cuantas ventas hay:\n", len(ventas_tienda))

print("Cuantos clientes distintos hay:\n", ventas_tienda["Cliente"].nunique())

print("Cuantos productos distintos hay:\n",
      ventas_tienda["Producto"].nunique())

print("Cual es la venta promedio:\n", ventas_tienda["Total"].mean())

print("Cual es la venta mas grande:\n", ventas_tienda["Total"].max())

print("Cual es la venta mas chica:\n", ventas_tienda["Total"].min())
