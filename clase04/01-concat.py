import pandas as pd

# QUe hace el concat? Te concatena las tablas, es decir, te "pega" una tabla a la otra
df1 = pd.DataFrame({
    "Nombre": ["Juan"]
})

df2 = pd.DataFrame({
    "Nombre": ["Ana"]
})

df3 = pd.concat([df1, df2], ignore_index=True)
dataframeFinal = df3.to_csv("dataframe3.csv")

print(df3)

""" 
¿Que diferencia tiene con el merge?
merge te une por relacion, por una columna en comun
concat, te pega los datasets
"""

""" 
Ejemplos de uso:
-Tenes balance enero, balance febrero, balance marzo, y yo quiero sacar un dataset con balance trimestral

Hay que tener cuidado -> Si hay diferencias estructurales
"""
