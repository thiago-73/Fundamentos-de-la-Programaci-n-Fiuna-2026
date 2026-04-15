# Bucle infinito para asegurar que el usuario ingrese un valor válido
while True:
    try:
        # Se lee una palabra o frase ingresada por el usuario
        palabra = str(input())
        break  # Si no hay error, se sale del bucle
    except:
        # Mensaje de error si ocurre una excepción
        print("Error: ingrese una palabra o frase.")

# Lista de vocales en mayúsculas y minúsculas
vocales = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

# Variable contador para contar cuántas vocales hay
contador = 0

# Se recorre cada carácter de la palabra ingresada
for i in palabra:
    # Se verifica si el carácter es una vocal
    if i in vocales:
        # Si es vocal, se incrementa el contador
        contador += 1

# Se imprime el resultado final con formato de texto
print(f"La palabra ingresada contiene: {contador} vocales")