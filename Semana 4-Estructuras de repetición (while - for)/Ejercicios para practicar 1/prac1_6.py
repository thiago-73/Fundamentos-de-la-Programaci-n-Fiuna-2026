# Se utiliza un ciclo infinito para solicitar un número válido al usuario
# while True crea un bucle que se repetirá indefinidamente
# El ciclo solo terminará cuando se ejecute la instrucción break
while True:
    try:
        # Se solicita al usuario que ingrese un número entero positivo
        # input() lee lo que escribe el usuario como texto (string)
        # int() intenta convertir ese texto a número entero
        n = int(input("Ingrese un entero positivo: "))
        
        # Se verifica que el número ingresado sea mayor que 0
        # Es decir, que sea un número positivo
        if n > 0:
            # Si el número es válido, se rompe el ciclo infinito
            # y el programa continúa con el resto del código
            break
        else:
            # Si el número es entero pero no positivo (0 o negativo)
            # se muestra un mensaje de error
            print("Error: Debe ser positivo.")

    # Si el usuario ingresa algo que no puede convertirse a entero
    # por ejemplo: letras, símbolos o números decimales
    # Python genera un error llamado ValueError
    # Este error se captura con except para evitar que el programa se detenga
    except ValueError:
        
        # Se muestra un mensaje indicando que el valor no es un entero válido
        print("Error: Debe ser un número entero.")
        

# Inicialización de las dos primeras variables de la sucesión de Fibonacci
# a representa el término actual
# b representa el siguiente término de la sucesión
# La sucesión comienza con 0 y 1
a, b = 0, 1

# Se repite el proceso n veces
# range(n) genera una secuencia desde 0 hasta n-1
# La variable "_" se usa cuando no necesitamos utilizar el contador
for _ in range(n):

    # Se actualizan simultáneamente los valores de a y b
    # a toma el valor anterior de b
    # b se convierte en la suma del antiguo a + antiguo b
    # Esto permite avanzar al siguiente término de Fibonacci
    a, b = b, a + b

# Se imprime el resultado final
# f"" permite insertar variables dentro del texto usando {}
# En este caso se muestra el término n de la sucesión de Fibonacci
print(f"El término {n} de Fibonacci es: {a}")