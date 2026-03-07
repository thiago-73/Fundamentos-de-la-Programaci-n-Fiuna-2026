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
        
# Lista vacía para almacenar los factores primos del número
factores = []

# Empezamos a dividir desde el 2, el primer número primo
i = 2

# Mientras n sea mayor a 1, seguimos factorizando
while n > 1:
    # Si i divide exactamente a n
    if n % i == 0:
        # Se agrega i a la lista de factores
        factores.append(i)
        # Se divide n entre i para continuar factorizando
        n //= i
    else:
        # Si i no divide a n, se pasa al siguiente número
        i += 1

# Se imprime cada factor primo con su exponente
# sorted(set(factores)) obtiene los factores únicos ordenados
for x in sorted(set(factores)):
    # factores.count(x) cuenta cuántas veces aparece cada factor
    # end=" " hace que todos los factores se impriman en la misma línea
    print(f"{x}^{factores.count(x)}", end=" ")