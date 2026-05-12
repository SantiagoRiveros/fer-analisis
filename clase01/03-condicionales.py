""" 
en la concatenacion o encadenamiento de condicionales, SIEMPRE el primero es if.
Si hay varios condicionales, la unica posicion posible del else, es la ultima.


"""

edad = 18

if edad >= 18:
    print("Es mayor de edad")
elif edad < 18:
    print("Es menor de edad")
else:
    print("Numero no valido")
