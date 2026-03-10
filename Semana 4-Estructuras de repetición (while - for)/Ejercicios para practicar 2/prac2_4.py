# Bucle infinito para pedir un número válido al usuario
while True:
    try:
        # Se solicita al usuario un número entero
        num = int(input("Ingresa un número entero positivo: "))
        
        # Se verifica que el número sea positivo
        if num <= 0:
            # Si el número es 0 o negativo se muestra un mensaje de error
            print("Debe ser positivo")
        else:
            # Si el número es válido se sale del bucle
            break
            
    # Si el usuario ingresa algo que no puede convertirse a entero
    except ValueError:
        print("No es un número entero")

# Variable booleana que indicará si el número es primo o no
# Se asume inicialmente que el número es primo
es_primo = True

# Caso especial: el número 1 no es considerado primo
if num == 1:
    es_primo = False
else:
    
    # Se revisa si el número tiene divisores entre 2 y la raíz cuadrada del número
    # num ** 0.5 calcula la raíz cuadrada de num
    # int(...)+1 se usa para recorrer los posibles divisores
    for i in range(2, int(num ** 0.5) + 1):
        
        # Si el número es divisible por i
        # significa que tiene un divisor distinto de 1 y de sí mismo
        if num % i == 0:
            
            # Entonces el número no es primo
            es_primo = False
            
            # Se termina el ciclo porque ya encontramos un divisor
            break

# Se muestra el resultado final
if es_primo:
    print(f"{num} es primo.")
else:
    print(f"{num} no es primo.")