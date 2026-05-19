import pandas as pd
import matplotlib.pyplot as plt

dataframe = pd.read_csv("titanic-corregido.csv")


# Bar Chart
dataframe["Sex"].value_counts().plot(kind="bar")

plt.title("Cantidad por sexo")
plt.savefig("barchart-cantidad-por-sexo.jpg")

plt.clf()  # <- Nunca olvidar esto

# Pie CHart
dataframe["Survived"].value_counts().plot(
    kind="pie", labels=["Not Survived", "Survived"])
plt.savefig("piechart-sobrevivientes.jpg")

plt.clf()

# Histogram
dataframe["Age"].plot(kind="hist")
plt.savefig("histogram-edad.jpg")

plt.clf()

# Line Chart

dataframe["Age"].head(20).plot(kind="line")
plt.savefig("linechart-edad.jpg")

plt.clf()

# Scatterplot

dataframe.plot(kind="scatter", x="Age", y="Fare")

plt.savefig("scatter-edad-pasaje.jpg")

plt.clf()

# Boxplot
dataframe.boxplot(column="Age")

plt.savefig("boxplot-edad.jpg")

plt.clf()

# Area Chart

dataframe["Fare"].head(20).plot(kind="area")

plt.savefig("area-pasaje.jpg")

plt.clf()

# BARH
dataframe["Embarked"].value_counts().plot(kind="barh")
plt.savefig("barh-embarked.jpg")

plt.clf()

# KDE
dataframe["Age"].plot(kind="kde")

plt.savefig("kde-edad.jpg")

plt.clf()

# Subplots

dataframe[["Age", "Fare"]].plot(
    subplots=True
)

plt.savefig("subplots.jpg")
