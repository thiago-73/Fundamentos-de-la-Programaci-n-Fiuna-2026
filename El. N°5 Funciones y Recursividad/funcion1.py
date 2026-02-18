# 1. Escriba un programa en que lea un número entero y positivo,
# obtenga e imprima todos sus factores primos.
#
# Un factor primo es un número primo que divide exactamente a otro número.
#
# Ejemplo:
# 12 → factores primos: 2 y 3
# porque:
# 12 ÷ 2 = 6
# 12 ÷ 3 = 4

# Esta función determina si un número es primo o no
def primo(num):

    # Los números menores o iguales a 1 NO son primos
    # Ejemplo: 0, 1, -5 → no son primos
    if num <= 1:
        return False

    # Probamos dividir el número entre todos los números desde 2 hasta num - 1
    # Si alguno lo divide exactamente, entonces NO es primo
    for x in range(2, num):

        # El operador % devuelve el residuo de la división
        # Si el residuo es 0, significa que es divisible
        if num % x == 0: 
            return False  # No es primo

    # Si ningún número lo divide, entonces es primo
    return True


# Pedimos al usuario un número positivo
# Usamos validación para evitar errores si el usuario escribe letras
while True:
    try:
        # Pedimos el número y lo convertimos a entero
        num = int(input("Ingrese número: "))
        
        # Verificamos que sea positivo
        if num > 0:
            break  # Salimos del bucle si es válido
        else:
            print("Error: Debe ingresar un número entero positivo.")
    except ValueError:
        print("Error: Debe ingresar un número entero válido.")


# Creamos una lista vacía donde guardaremos los factores primos
# Una lista permite almacenar múltiples valores
primos = []


# Primero verificamos si el número mismo es primo
if primo(num):

    # Si el número es primo, lo informamos
    print(f"{num} es un número primo.")

else:

    # Recorremos todos los números desde 2 hasta num
    # para verificar cuáles son factores primos
    for i in range(2, num + 1):

        # Verificamos dos condiciones:
        #
        # 1. num % i == 0  → i es factor de num
        # 2. primo(i)      → i es número primo
        #
        # Si ambas se cumplen, entonces i es factor primo
        if num % i == 0 and primo(i):

            # append() agrega el valor a la lista
            primos.append(i)

        # Esta línea no es necesaria porque el for ya incrementa i automáticamente,
        # pero se deja porque forma parte de tu código original
        i += 1


    # Mostramos los factores primos encontrados
    print("Factores primos:")

    # Recorremos la lista e imprimimos cada factor
    for factor in primos:

        print(factor)
