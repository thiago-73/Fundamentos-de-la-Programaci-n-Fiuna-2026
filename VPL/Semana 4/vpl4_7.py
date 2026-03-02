# Se solicita al usuario que ingrese un número entero
n = int(input())

# Se verifica si el número es menor o igual a 0
# Los números primos solo existen en los números naturales positivos
if n <= 0:
    print("El numero no es positivo")

# Si el número es menor que 2, no puede ser primo
# El primer número primo es el 2
elif n < 2:
    print(f"El {n} no es un numero primo")

# Si el número es mayor o igual a 2, se procede a verificar si es primo
else:
    # Se crea una variable booleana que asumirá inicialmente que el número es primo
    es_primo = True

    # Se recorre un rango de números desde 2 hasta la raíz cuadrada de n
    # Esto se hace porque si un número tiene divisores,
    # al menos uno estará en este rango
    for i in range(2, int(n ** 0.5) + 1):

        # Se verifica si n es divisible por i
        # Si el residuo de la división es 0, entonces n tiene un divisor
        if n % i == 0:
            # En ese caso el número no es primo
            es_primo = False
            # Se rompe el ciclo porque ya no es necesario seguir comprobando
            break

    # Después del ciclo, se revisa el valor de la variable es_primo
    if es_primo:
        print(f"El {n} es un numero primo")
    else:
        print(f"El {n} no es un numero primo")