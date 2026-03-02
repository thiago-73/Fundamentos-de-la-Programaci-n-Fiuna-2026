# Se inicializan varias variables que servirán para llevar el control de diferentes cálculos

# Contador de números impares
cant_impares = 0

# Acumulador para sumar los números pares
suma_pares = 0

# Contador de cuántos números pares se ingresan
cant_pares = 0

# Contador de números que están dentro de la segunda docena (13 a 24)
cant_mayor_docena = 0

# Variable para almacenar el número mayor ingresado
mayor = 0

# Se utiliza un ciclo for que se repetirá 10 veces
# El guion bajo "_" se usa porque no necesitamos usar la variable del ciclo
for _ in range(10):

    # Se solicita al usuario que ingrese un número entero
    n = int(input())

    # Se verifica si el número ingresado es mayor que 36
    # Si lo es, se muestra un mensaje de error y se termina el ciclo
    if n > 36:
        print("Ingrese un valor entre 0 y 36")
        break

    # Se verifica si el número es impar
    # n % 2 devuelve el residuo de dividir entre 2
    # Si el residuo es distinto de 0, el número es impar
    if n % 2:
        cant_impares += 1

    # Si no es impar, se evalúa si es par y distinto de 0
    elif n != 0:
        # Se suma el número al acumulador de números pares
        suma_pares += n

        # Se incrementa el contador de números pares
        cant_pares += 1

    # Se verifica si el número pertenece a la segunda docena (entre 13 y 24 inclusive)
    if 13 <= n <= 24:
        cant_mayor_docena += 1

    # Se actualiza el valor del número mayor usando la función max()
    # max() devuelve el mayor entre los dos valores comparados
    mayor = max(mayor, n)

# Se calcula el promedio de los números pares
# Dividiendo la suma de los pares entre la cantidad de números pares
prom_pares = suma_pares / cant_pares

# Se imprimen los resultados obtenidos

# Cantidad de números impares ingresados
print(f"a = {cant_impares}")

# Promedio de los números pares
print(f"b = {prom_pares}")

# Cantidad de números dentro de la segunda docena
print(f"c = {cant_mayor_docena}")

# El número mayor ingresado
print(f"d = {mayor}")