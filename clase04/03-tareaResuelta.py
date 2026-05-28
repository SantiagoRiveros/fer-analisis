import pandas as pd

productos = pd.DataFrame({
    "ProductoID": [1, 2, 3],
    "Producto": ["Mouse", "Teclado", "Monitor"]
})

ventas = pd.DataFrame({
    "ProductoID": [1, 2, 1],
    "Cantidad": [2, 1, 4]
})

productosConVentas = pd.merge([productos, ventas])
