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
1- Transformar los datos
2- Cambiar nombres de columnas (Si es necesario)
3- Buscar duplicados


"""
