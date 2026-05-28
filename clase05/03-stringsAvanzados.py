import pandas as pd

usuarios = pd.DataFrame({
    "Nombre": [
        "Sr. Juan  ",
        "Sra. Ana",
        "Car los"
    ]
})

# Limpiar espacios
# el str es de string y el strip le saca los espacios antes y despues de las letras
usuarios["Nombre"] = usuarios["Nombre"].str.strip()

# Reemplazar Texto
# El primer argumento lo que va a reemplzar, y el segundo es porque lo va reemplzar
usuarios["Nombre"] = usuarios["Nombre"].str.replace("Sr.", "")

usuarios["Nombre"] = usuarios["Nombre"].str.replace("Sra.", "")

print(usuarios)

usuarios["Nombre"] = usuarios["Nombre"].str.strip()


print(usuarios[usuarios["Nombre"].str.contains(" ")])
usuarios["Nombre"] = usuarios["Nombre"].str.replace(" ", "")

# Convertir a mayusculas o minusculas
# usuarios["Nombre"].str.upper()
usuarios["Nombre"] = usuarios["Nombre"].str.lower()

print(usuarios)

usuarios["Nombre"] = usuarios["Nombre"].str.capitalize()

print(usuarios)

usuarios.to_csv("usuarios.csv")
