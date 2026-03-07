# Bucle infinito para pedir al usuario un número hasta que sea válido
while True:
    try:
        # Se solicita al usuario un número entero positivo
        n = int(input("Ingrese un número entero y positivo: "))
        
        # Verifica que el número sea mayor a 0
        if n > 0:
            # Si es válido, se sale del bucle
            break
        else:
            # Si es menor o igual a 0, se muestra un mensaje de error
            print("El número debe ser positivo.")
    # Si el usuario ingresa algo que no puede convertirse a entero
    except ValueError:
        print("El número debe ser entero.")
   
for i in range(1, n + 1):
    print("*" * i, end="")
    
    print(" " * (2 * (n - i)), end="")
    
    print("*" * i,)

for i in range(n - 1, 0, -1):
    # Asteriscos izquierdos
        print("*" * i, end="")
        
        # Espacios del medio
        print(" " * (2 * (n - i)), end="")
        
        # Asteriscos derechos
        print("*" * i)