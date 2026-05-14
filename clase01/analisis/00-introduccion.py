import pandas as pd

dataframe = pd.read_csv("titanic.csv")

# mostrar primeras 5 filas
# print(dataframe.head())

# Mostrar que columnas tiene
print(dataframe.columns)

# Siempre, el eje, se tiene que basar en:

""" 
1- medidas criticas
2- medidas numericas
3- medidas descriptivas
"""

# Ver informacion general
print(dataframe.info())

print(dataframe.describe())

# Rellenando edad
promedioEdad = dataframe["Age"].mean()
dataframe["Age"] = dataframe["Age"].fillna(promedioEdad)

print(dataframe.info())

dataframe["Embarked"] = dataframe["Embarked"].fillna("X")

print(dataframe.info())

dataframe = dataframe.drop("Cabin", axis=1)

print(dataframe.info())

# Faltaria:

""" 
3- Buscar duplicados
"""
print(dataframe[dataframe.duplicated()])


# Edad minima
print("Edad minima")
print(dataframe["Age"].min())

# Edad Maxima
print("Edad Maxima")
print(dataframe["Age"].max())

# Edad promedio
print("Edad Promedio")
print(dataframe["Age"].mean())


# Filtros

# Mostrar columna
print("Mostrar columna Age")
print(dataframe["Age"])

# Filtrar mayores de 30
print("Mostrar mayores de 30")
print(dataframe[dataframe["Age"] > 30])

# Mostrar solo mujeres
print("Mostrar mujeres")
print(dataframe[dataframe["Sex"] == "female"])

""" 
Vos seleccionas el dataframe, y en vez de darle una columna en especifico, le das una condicion
Dicho esto, cuando vos le das una columna, tambien es como una condicion
"""

# Mostrar solo hombres mayores de 30
print("Mostrar hombres mayores de 30")
print(dataframe[(dataframe["Age"] > 30) & (dataframe["Sex"] == "male")])

# en Pandas, no te permite usar "and" tenes que usar -> &
print("Mujeres que sobrevivieron de primera clase")
print(dataframe[(dataframe["Sex"] == "female") & (
    dataframe["Survived"] == 1) & (dataframe["Pclass"] == 1)])

print("Mujeres que sobrevivieron de segunda clase")
print(dataframe[(dataframe["Sex"] == "female") & (
    dataframe["Survived"] == 1) & (dataframe["Pclass"] == 2)])

print("Mujeres que sobrevivieron de tercera clase")
print(dataframe[(dataframe["Sex"] == "female") & (
    dataframe["Survived"] == 1) & (dataframe["Pclass"] == 3)])

""" 
Primero, que es lo mas importante del CSV? La cantidad de sobrevivientes/fallecidos.
Entonces, luego hay que pensar en el contexto de donde se sacaron los datos -> Occidente, 1912
Habia sesgo por capital? Habia sesgo por sexo? -> Causas sociocultares
La edad -> No llego al barco


"""

# Cantidad sobrevivientes
print("Cantidad sobrevivientes")
print(dataframe["Survived"].value_counts())

# Cantidad de sobrevivientes por sexo
print("Cantidad Sobrevivientes por sexo")
print("Fallecidos")
print(dataframe[dataframe["Survived"] == 0].groupby("Sex").count())
print("Sobrevivientes")
print(dataframe[dataframe["Survived"] == 1].groupby("Sex").count())

# Promedio de edad por sexo
print("Promedio de edad por sexo")
print(dataframe.groupby("Sex")["Age"].mean())

# Clase con mas sobrevivientes
print("Sobrevivientes")
print(dataframe[dataframe["Survived"] == 1].groupby("Pclass").count())
print("Fallecidos")
print(dataframe[dataframe["Survived"] == 0].groupby("Pclass").count())

# Guardar el CSV
dataframe.to_csv("titanic-corregido.csv")
