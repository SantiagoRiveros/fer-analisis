import pandas as pd


clientes = pd.DataFrame({
    "ClienteID": [1, 2, 3],
    "Nombre": ["Juan", "Ana", "Pedro"]
})

ventas = pd.DataFrame({
    "ClienteID": [1, 2, 1],
    "Total": [100, 250, 300]
})

print(clientes)
print(ventas)

""" 
Unimos ambos usando la columna "ClienteID"
en dataframe clientes -> ClienteID = Clave Unica, o clave primaria, sirve para identificar de manera unica
ventas -> ClienteID = Clave Foranea, es decir, su valor, apunta al valor de una clave primaria de otro dataset
"""

# Un merge es una manera de unir/combinar/fusionar varios dataset

# Merge basico
resultado = pd.merge(clientes, ventas, on="ClienteID")
# Los dos primeros parametros que recibe, son los dataset a unir
# El ultimo parametro es en cual columna se van a unir

print(resultado)

# Tipos de JOIN
# Inner Join
innerJoin = pd.merge(clientes, ventas, on="ClienteID", how="inner")
# en how le indicamos el tipo de JOIN que vamos a usar
# El inner devuelve SOLO las coincidencias entre ambas tablas

# Left JOIN
leftJOIN = pd.merge(clientes, ventas, on="ClienteID", how="left")
# Te trae TODAS las entradas de la tabla de la izquierda, y solo las coincidencias de la derecha
# Cuando algo de la tabla izquierda no tiene coincidencia en la derecha, me lo rellena con un NaN

print(leftJOIN)

# Right Join
rightJoin = pd.merge(clientes, ventas, on="ClienteID", how="right")
# Lo mismo que el left, pero al reves

print(rightJoin)

# Outer JOIN
outerJOIN = pd.merge(clientes, ventas, on="ClienteID", how="outer")

print(outerJOIN)

# Ejemplo mas pro
empleados = pd.DataFrame({
    "EmpleadoID": [1, 2, 3],
    "Nombre": ["Juan", "Ana", "Pedro"],
    "SectorID": [1, 2, 1]
})

sectores = pd.DataFrame({
    "SectorID": [1, 2],
    "Sector": ["IT", "RRHH"]
})

resultadoFinal = pd.merge(empleados, sectores, on="SectorID")

print(resultadoFinal)
