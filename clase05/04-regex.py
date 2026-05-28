# Que es regex? -> Regular Expressions
# Que hace? -> Busca patrones de texto
import pandas as pd
import re

dataframe = pd.read_csv("usuarios.csv")

print(dataframe["Nombre"].str.contains(r"\d"))  # <- Busca numeros

# Que pasa si busco un email?

regexForEmail = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

emailValido = "juan@gmail.com"

if re.match(regexForEmail, emailValido):
    print("Email Valido")
else:
    print("Email invalido")

""" 
Para que nos sirve?
Validar formatos
Detectar formatos
Limpiar
etc
"""
