# Bucle infinito para pedir el primer número hasta que sea válido
while True:
    try:
        # Se solicita al usuario un número entero positivo
        num1 = int(input("Ingresa un número entero positivo: "))
        
        # Se verifica que el número sea positivo
        if num1 <= 0:
            print("Debe ser positivo")
        else:
            # Si el valor es válido se sale del bucle
            break
            
    # Si el usuario ingresa algo que no puede convertirse a entero
    except ValueError:
        print("No es un número entero")
        
# Bucle para pedir el segundo número
# Este número debe ser mayor que el primero
while True:
    try:
        # Se solicita un número mayor que num1
        num2 = int(input(f"Ingresa un número entero mayor que {num1}: "))
        
        # Se verifica que el segundo número sea mayor que el primero
        if num2 <= num1:  
            print(f"Debe ser mayor que {num1}")
        else:
            # Si el valor es válido se sale del bucle
            break
            
    # Manejo de error si el usuario no ingresa un número entero
    except ValueError:
        print("No es un número entero")
        
# Se crea una lista con todos los números desde num1 hasta num2
# num2 + 1 se usa porque range no incluye el último número
numeros = list(range(num1, num2 + 1))
    
# Se calcula la suma de todos los números de la lista
# sum() es una función de Python que suma todos los elementos de una lista
suma = sum(numeros)

# Se imprime el resultado de la suma
print(f"La suma desde {num1} hasta {num2} es {suma}")

# Se muestra la suma paso a paso
# map(str, numeros) convierte cada número de la lista en texto
# join une los elementos con " + " entre ellos
# Esto permite mostrar algo como: 3 + 4 + 5 + 6 = 18
print(" + ".join(map(str, numeros)) + " = " + str(suma))