# Intentamos ejecutar el bloque para capturar errores de entrada
try:
    # Se solicita al usuario un timestamp en segundos
    timestamp = int(input())

    # Verificamos que el número sea positivo
    if timestamp < 0:
        print("Error: El timestamp debe ser un número entero positivo")
    else:
        # Se calcula la cantidad total de horas
        horas = timestamp // 3600
        
        # Se calcula la cantidad de minutos restantes después de las horas
        minutos = (timestamp % 3600) // 60
        
        # Se calcula la cantidad de segundos restantes después de horas y minutos
        segundos = timestamp % 60

        # Se muestran los resultados desglosados
        print(f"{timestamp} segundos:")
        print(f"{horas} horas, {minutos} minutos, {segundos} segundos")
        
        # Se muestra en formato HH:MM:SS con dos dígitos para cada valor
        print(f"Formato: {horas:02}:{minutos:02}:{segundos:02}")

# Capturamos el error si el usuario no ingresa un número entero
except ValueError:
    print("Error: Debe ingresar un número entero")