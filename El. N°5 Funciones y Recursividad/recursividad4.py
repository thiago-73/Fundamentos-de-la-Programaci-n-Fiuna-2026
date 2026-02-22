# 4. Ingresar un número y mostrar su equivalente en binario utilizando una función recursiva.

# Definimos la función recursiva "binario" que recibe un número entero n
def binario(n):
    # Caso base:
    # Si n es menor que 2 (es decir, 0 o 1),
    # ya es un número binario, entonces lo devolvemos como texto (string)
    if n < 2:       
        return str(n)
    else:
        # Caso recursivo:
        # n // 2 -> división entera (obtenemos el "siguiente paso")
        # n % 2  -> residuo de la división entre 2 (0 o 1)
        # Llamamos recursivamente a la función hasta llegar al caso base
        # y vamos concatenando los residuos como texto
        return binario(n // 2) + str(n % 2)
        

# Ciclo para validar que el usuario ingrese un número correcto
while True:
    try:
        # Pedimos al usuario un número entero positivo
        n = int(input("Ingrese un número entero positivo: "))
        
        # Validamos que el número no sea negativo
        if n >= 0:
            break  # Si es válido, salimos del ciclo
        else:
            print("Ingrese un número positivo.")
            
    except ValueError:
        # Si el usuario escribe algo que no es un número entero
        print("Valor inválido.")

# Mostramos el resultado llamando a la función recursiva
print("Binario:", binario(n))
