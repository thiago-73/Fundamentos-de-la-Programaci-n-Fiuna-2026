try:
    timestamp = int(input())

    if timestamp < 0:
        print("Error: El timestamp debe ser un número entero positivo")
    else:
        horas = timestamp // 3600
        minutos = (timestamp % 3600) // 60
        segundos = timestamp % 60

        print(f"{timestamp} segundos:")
        print(f"{horas} horas, {minutos} minutos, {segundos} segundos")
        print(f"Formato: {horas:02}:{minutos:02}:{segundos:02}")

except ValueError:
    print("Error: Debe ingresar un número entero")