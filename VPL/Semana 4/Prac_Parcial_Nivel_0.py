# Se intenta ejecutar el bloque, para capturar errores si el usuario no ingresa un número
try:
    # Se solicita al usuario que ingrese un timestamp en segundos
    timestamp = int(input())

    # Verificamos que el número sea positivo
    if timestamp < 0:
        print("Error: El timestamp debe ser un número entero positivo")
    else:
        # Se calcula la cantidad de días completos
        # 1 día = 86400 segundos
        dias = timestamp // 86400
        
        # Se calcula el resto de segundos que no forman un día completo
        resto = timestamp % 86400

        # Se imprimen los resultados
        print(f"Timestamp: {timestamp} segundos")
        print(f"Días: {dias}")
        print(f"Segundos restantes: {resto}")

# Si el usuario ingresa un valor que no se puede convertir a entero
except ValueError:
    print("Error: Debe ingresar un número entero")