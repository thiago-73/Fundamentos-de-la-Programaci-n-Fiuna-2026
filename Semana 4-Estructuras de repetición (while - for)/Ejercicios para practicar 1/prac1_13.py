# Esta función determina si un número es primo o no
def es_primo(num):

    # El número 1 no se considera primo
    if num == 1:
        return False
    
    # Se prueban posibles divisores desde 2 hasta la raíz cuadrada del número
    # Esto hace el algoritmo más eficiente
    for i in range(2, int(num ** 0.5) + 1):

        # Si el número es divisible por i, entonces no es primo
        if num % i == 0:
            return False
        
    # Si no se encontró ningún divisor, el número es primo
    return True


# Se utiliza un ciclo infinito para solicitar un número válido al usuario
while True:
    try:
        # Se solicita al usuario que ingrese un número entero positivo
        # int() convierte el valor ingresado a entero
        n = int(input("Ingrese un entero positivo: "))
        
        # Se verifica que el número sea mayor que 0
        if n > 0:
            # Si el número es válido se termina el ciclo
            break
        else:
            # Si el número es entero pero no positivo, se muestra un error
            print("Error: Debe ser positivo.")

    # Si el usuario ingresa algo que no puede convertirse a entero
    # Python genera un ValueError y se captura con except
    except ValueError:
        
        # Se muestra un mensaje indicando que el valor no es un entero
        print("Error: Debe ser un número entero.")


# Se imprime un mensaje indicando el rango de números que se evaluarán
print(f"Números primos del 1 al {n}:")

# Se crea una lista vacía para almacenar los números primos encontrados
primos = []

# Se recorren todos los números desde 1 hasta n
for i in range(1, n + 1):

    # Se usa la función es_primo() para verificar si el número es primo
    if es_primo(i):

        # Si es primo, se agrega a la lista
        primos.append(i)

# Finalmente se imprime la lista de números primos encontrados
print(primos)