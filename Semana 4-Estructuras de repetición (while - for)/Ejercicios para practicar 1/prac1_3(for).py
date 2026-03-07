# Se utiliza un ciclo infinito para solicitar un número válido al usuario
while True:

    # Se pide al usuario que ingrese un número natural
    # Se usa float para poder detectar si el número tiene decimales
    n = float(input("Ingrese un número natural: "))
    
    # Se verifica que el número sea entero y mayor que 0
    # n == int(n) comprueba que no tenga decimales
    if n == int(n) and n > 0:
        # Si el número es válido, se sale del ciclo
        break
    else:
        # Si no es válido, se muestra un mensaje de error
        print("Ingrese un número natural, el número ingresado no es válido.")
        
# Se crea una lista para almacenar los múltiplos de 3
multiplos = []

# Se recorre desde 0 hasta n-1
# Esto permite obtener los números menores que n
for i in range(int(n)):

    # Se verifica si el número es múltiplo de 3
    # Un número es múltiplo de 3 si el residuo de dividir entre 3 es 0
    if i % 3 == 0:
        # Si cumple la condición, se agrega a la lista
        multiplos.append(i)        

# Se calcula la suma de los múltiplos de 3 usando la función sum()
suma = sum(multiplos)

# Se calcula el promedio dividiendo la suma entre la cantidad de elementos de la lista
promedio = suma / len(multiplos)

# Se imprime la sumatoria y el promedio de los múltiplos encontrados
print(f"La sumatoria de los multiplos de 3 menores que {n} es {suma} y el promedio es {promedio}")