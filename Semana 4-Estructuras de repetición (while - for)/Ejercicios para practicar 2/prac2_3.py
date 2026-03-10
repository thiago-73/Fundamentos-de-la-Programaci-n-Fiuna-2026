# Validar cantidad inicial
# Se utiliza un bucle infinito para pedir la cantidad de números
# hasta que el usuario ingrese un valor válido
while True:
    try:
        # Se pide al usuario cuántos números va a introducir
        # int() convierte el texto ingresado en un número entero
        cantidad = int(input("¿Cuántos números vas a introducir? "))
        
        # Se verifica que la cantidad sea positiva
        if cantidad <= 0:
            # Si es 0 o negativo se muestra un mensaje de error
            print("Debe ser un número positivo")
        else:
            # Si el número es válido se sale del bucle
            break
            
    # Si el usuario ingresa algo que no es un número entero
    except ValueError:
        print("No es un número entero")

# Variable que contará cuántos números negativos se ingresan
negativos = 0

# Se repite el proceso 'cantidad' de veces
# range(cantidad) genera números desde 0 hasta cantidad-1
for i in range(cantidad):

    # Bucle para validar cada número que ingresa el usuario
    while True:
        try:
            # Se solicita el número al usuario
            # i+1 se usa para numerar los inputs desde 1 y no desde 0
            num = int(input(f"Número {i+1}: "))
            
            # Si el número es válido se sale del bucle
            break
            
        # Si el usuario no ingresa un número entero
        except ValueError:
            print("No es un número entero")
    
    # Se verifica si el número ingresado es negativo
    if num < 0:
        # Si lo es, se incrementa el contador de negativos
        negativos += 1

# Se muestra la cantidad total de números negativos ingresados
# f"" permite insertar variables dentro del texto
print(f"Has introducido {negativos} número(s) negativo(s)")