# Se utiliza un ciclo infinito para solicitar al usuario un número válido
while True:

    # Se pide al usuario que ingrese un número natural
    # Se usa float para poder detectar si el número tiene decimales
    n = float(input("Ingrese un número natural: "))
    
    # Se verifica que el número sea entero y mayor que 0
    # n == int(n) comprueba que el número no tiene parte decimal
    if n == int(n) and n > 0:
        # Si el número es válido, se sale del ciclo
        break
    else:
        # Si no es válido, se muestra un mensaje de error
        print("Ingrese un número natural, el número ingresado no es válido.")
        
# Se crea una lista vacía para guardar los múltiplos de 3
multiplos = []

# Se inicializa la variable i en 0
# Esta variable servirá como contador en el ciclo
i = 0

# Se ejecuta el ciclo mientras i sea menor que n
# De esta forma se recorren todos los números menores que n
while int(n) > i:

    # Se verifica si el número i es múltiplo de 3
    # Un número es múltiplo de 3 si al dividirlo entre 3 el residuo es 0
    if i % 3 == 0:
        # Si cumple la condición, se agrega a la lista
        multiplos.append(i)
        
    # Se incrementa el contador para evaluar el siguiente número
    i += 1

# Se calcula la suma de todos los múltiplos de 3 encontrados
suma = sum(multiplos)

# Se calcula el promedio dividiendo la suma entre la cantidad de múltiplos encontrados
promedio = suma / len(multiplos)
    
# Se muestran los resultados
print(f"La suma de los multiplos de 3 menores que {n} es {suma} y el promedio es {promedio}")