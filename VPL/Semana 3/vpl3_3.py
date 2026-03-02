# Se solicita al usuario que ingrese un carácter.
# Se convierte a tipo string (texto) para poder analizarlo como carácter.
caracter = str(input())

# El método islower() verifica si el carácter es una letra minúscula.
# Si el carácter es una letra entre 'a' y 'z', la condición será verdadera.
if caracter.islower():
    print("El caracter ingresado es una letra (minuscula)")

# Si la condición anterior no se cumple, se evalúa si el carácter es una letra mayúscula.
# El método isupper() verifica si el carácter es una letra entre 'A' y 'Z'.
elif caracter.isupper():
    print("El caracter ingresado es una letra (mayuscula)")

# Si no es ni minúscula ni mayúscula, entonces el carácter no corresponde a una letra.
# Puede ser un número, símbolo o cualquier otro tipo de carácter.
else:
    print("El caracter ingresado NO corresponde a una letra")