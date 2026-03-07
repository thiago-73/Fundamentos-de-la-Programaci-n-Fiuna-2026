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

# Caso especial: el número 1 no se considera primo
if n == 1:
    print(f"El número {n} no es primo.")     

else:
    # Se asume inicialmente que el número es primo
    es_primo = True

    # Se revisan posibles divisores desde 2 hasta la raíz cuadrada de n
    # Solo es necesario revisar hasta √n para determinar si es primo
    for i in range(2, int(n ** 0.5) + 1):

        # Si n es divisible entre i, entonces no es primo
        if n % i == 0:
            es_primo = False
            break
    
    # Se muestra el resultado final
    if es_primo:
        print(f"El número {n} es primo.")
    else:
        print(f"El número {n} no es primo.")