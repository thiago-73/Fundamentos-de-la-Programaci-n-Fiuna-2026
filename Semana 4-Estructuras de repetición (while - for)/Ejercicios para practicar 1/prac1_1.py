# Se utiliza un ciclo infinito (while True) para seguir pidiendo datos
# hasta que el usuario ingrese un número entero válido
while True:

    # Se solicita al usuario que ingrese un número
    # Se usa float para permitir que el usuario escriba números con decimales
    n = float(input("Ingrese un número entero: "))
    
    # Se verifica si el número es entero
    # Un número entero tiene residuo 0 cuando se divide entre 1
    if n % 1 == 0:
        # Si es entero, se convierte explícitamente a tipo int
        n = int(n)
        
        # Se muestra el número entero ingresado
        print("El número ingresado es el entero: ", n)
        
        # Se rompe el ciclo infinito porque ya se obtuvo un valor válido
        break

    # Si el número tiene parte decimal, no es entero
    else:
        # Se muestra un mensaje indicando que el valor ingresado no es válido
        print("Ingrese un número entero.")