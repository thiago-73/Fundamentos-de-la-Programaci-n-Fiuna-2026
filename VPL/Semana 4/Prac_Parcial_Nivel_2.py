# Intentamos ejecutar el bloque para capturar errores de entrada
try:
    # Se solicita al usuario un timestamp en segundos
    timestamp = int(input())

    # Verificamos que el valor ingresado sea positivo
    if timestamp < 0:
        print("Error: El timestamp debe ser un número entero positivo")
    else:
        # Se calculan los días completos
        # 1 día = 86400 segundos
        dias = timestamp // 86400
        
        # Se obtiene el resto de segundos que no forman un día completo
        timestamp2 = timestamp % 86400
        
        # Se calculan las horas restantes después de los días
        horas = timestamp2 // 3600
        
        # Se calculan los minutos restantes después de horas
        minutos = (timestamp2 % 3600) // 60
        
        # Se calculan los segundos restantes después de minutos
        segundos = timestamp2 % 60

        # Se imprime el timestamp original
        print(f"{timestamp} segundos:")
        
        # Se imprimen los días completos
        print(f"Días: {dias}")
        
        # Se imprime la hora del día en formato HH:MM:SS con dos dígitos
        print(f"Hora del día: {horas:02}:{minutos:02}:{segundos:02}")
        
        # Se muestra la combinación de días + hora para una lectura completa
        print(f"Total: {dias} día(s) + {horas:02}:{minutos:02}:{segundos:02}")

# Capturamos el error si el usuario ingresa un valor no entero
except ValueError:
    print("Error: Debe ingresar un número entero")