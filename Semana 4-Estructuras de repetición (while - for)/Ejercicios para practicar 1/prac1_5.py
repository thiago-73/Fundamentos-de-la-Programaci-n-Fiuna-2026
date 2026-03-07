# Se utiliza un ciclo infinito para solicitar un número válido al usuario
while True:
    try:
        # Se solicita al usuario que ingrese un número entero positivo
        # int() convierte el valor ingresado a entero
        n = int(input("Ingrese un entero positivo: "))
        
        # Se verifica que el número sea mayor que 0
        if n > 0:
            break
        else:
            # Si el número es entero pero no positivo, se muestra un error
            print("Error: Debe ser positivo.")

    # Si el usuario ingresa algo que no puede convertirse a entero
    # Python genera un ValueError y se captura con except
    except ValueError:
        
        # Se muestra un mensaje indicando que el valor no es un entero
        print("Error: Debe ser un número entero.")

# Se inicializa la variable que almacenará el factorial
# Se comienza en 1 porque es el elemento neutro de la multiplicación
fact = 1

# Se guarda el valor original de n para poder mostrarlo al final
w = n

# Se calcula el factorial usando un ciclo while
# El ciclo se ejecuta mientras n sea mayor o igual a 1
while n >= 1:

    # Se multiplica el acumulador por el valor actual de n
    fact *= n 
    
    # Se reduce n en 1 para continuar con el siguiente número
    n -= 1

# Se imprime el resultado final del factorial
print(f"El factorial de {w} es: {fact}")