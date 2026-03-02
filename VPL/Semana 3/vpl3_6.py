# Se solicita al usuario que ingrese un número entero.
n = int(input())

# Se extraen los dígitos del número de tres cifras.
# c1: dígito de las centenas
c1 = n // 100

# c2: dígito de las decenas
# Primero se divide entre 10 para eliminar el dígito de las centenas, luego se obtiene el módulo 10 para el dígito de las decenas
c2 = (n // 10) % 10

# c3: dígito de las unidades
# Se obtiene usando módulo 10
c3 = n % 10

# Se verifica si cada dígito es 0 o 1
# Si los tres dígitos son 0 o 1, entonces el número es binario
if (c1 == 0 or c1 == 1) and (c2 == 0 or c2 == 1) and (c3 == 0 or c3 == 1):
    print("Es un numero binario")
# Si al menos un dígito no es 0 ni 1, el número no es binario
else:
    print("No es un numero binario")