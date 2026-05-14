import pandas as pd
import matplotlib.pyplot as plt

dataframe = pd.read_csv("titanic-corregido.csv")

# Sobrevivieron o no?
dataframe["Survived"].value_counts().plot(kind="bar")
plt.title("Sobrevivientes")
plt.xlabel("Sobrevivieron")
plt.ylabel("Cantidad")
plt.savefig("sobrevivientes-barras.jpg")

# NUNCA OLVIDARSE
plt.clf()


dataframe["Survived"].value_counts().plot(
    kind="pie", labels=["Not Survived", "Survived"])
plt.savefig("sobrevivientes-torta.jpg")


plt.clf()
# Promedio de edad por sexo

dataframe.groupby("Sex")["Age"].mean().plot(kind="bar")
plt.savefig("promedio-edad-sexo.jpg")

plt.clf()

# Clase con mas sobrevivientes
dataframe.groupby("Pclass")["Survived"].sum().plot(kind="bar")
plt.savefig("sobrevivientes-por-clase.jpg")
