# Bucle infinito para validar la entrada del número n
while True:
    try:
        # Se lee un número entero
        n = int(input())
        
        # Se verifica que sea positivo y múltiplo de 3
        if n > 0 and n % 3 == 0:
            break  # Si cumple, se sale del bucle
        else:
            print("Error: debe ser un número positivo y múltiplo de 3.")
    except:
        # Si el usuario ingresa algo que no es número
        print("Error: ingrese un número válido.")

# Lista donde se guardarán los valores binarios
binario = []

# Se repite n veces para ingresar los valores binarios
for i in range(n):
    while True:
        try:
            # Se lee un número
            num = int(input())
            
            # Se valida que solo sea 0 o 1
            if num == 0 or num == 1:
                binario.append(num)  # Se agrega a la lista
                break  # Se sale del bucle interno
            else:
                print("Error: solo se permite 0 o 1.")
        except:
            print("Error: ingrese un número válido.")

# Lista donde se guardará el resultado final
resultado = []

# Contador para llevar la suma de 1s en grupos de 3
contador = 0

# Se recorre toda la lista binaria
for i in range(len(binario)):
    # Se agrega el valor actual a la lista resultado
    resultado.append(binario[i])
    
    # Si el valor es 1, se incrementa el contador
    if binario[i] == 1:
        contador += 1
        
    # Cada vez que se completa un grupo de 3 elementos
    if (i + 1) % 3 == 0:
        # Se agrega la cantidad de unos encontrados en ese grupo
        resultado.append(contador)
        
        # Se reinicia el contador para el siguiente grupo
        contador = 0

# Se imprime la lista final como una sola línea separada por espacios
print(" ".join(map(str, resultado)))