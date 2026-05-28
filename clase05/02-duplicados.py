import pandas as pd

usuarios = pd.DataFrame({
    "Nombre": [
        "Juan",
        "Ana",
        "Juan"
    ]
})

# Vamos a detectar los duplicados

print(usuarios.duplicated())

print(usuarios[usuarios.duplicated()])

usuarios = usuarios.drop_duplicates()  # Esto me tira abajo los duplicados

print(usuarios)
