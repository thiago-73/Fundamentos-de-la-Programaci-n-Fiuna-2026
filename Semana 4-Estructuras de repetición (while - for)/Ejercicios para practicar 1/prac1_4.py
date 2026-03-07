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

# Se convierte definitivamente el valor a entero
n = int(n)

# Se imprime el primer símbolo "*" que representa la esquina superior izquierda
# end=" " evita que Python haga un salto de línea automático
print("*", end=" ")  

# Este ciclo imprime los números del encabezado de la tabla (1 hasta n)
for i in range(1, n + 1):
    print(i, end=" ")
    
# Se imprime un salto de línea para comenzar la tabla
print()

# Este ciclo recorre cada fila de la tabla de multiplicar
for i in range(1, n + 1):

    # Se imprime el número de la fila (sirve como encabezado lateral)
    print(i, end=" ")
    
    # Este ciclo recorre cada columna de la tabla
    for j in range(1, n + 1):

        # Se imprime el resultado de la multiplicación i * j
        print(i * j, end=" ")
    
    # Al terminar cada fila se hace un salto de línea
    print()