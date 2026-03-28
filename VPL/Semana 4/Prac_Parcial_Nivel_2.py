try:
    timestamp = int(input())

    if timestamp < 0:
        print("Error: El timestamp debe ser un número entero positivo")
    else:
        dias = timestamp // 86400
        timestamp2 = timestamp % 86400
        horas = timestamp2 // 3600
        minutos = (timestamp2 % 3600) // 60
        segundos = timestamp2 % 60

        print(f"{timestamp} segundos:")
        print(f"Días: {dias}")
        print(f"Hora del día: {horas:02}:{minutos:02}:{segundos:02}")
        print(f"Total: {dias} día(s) + {horas:02}:{minutos:02}:{segundos:02}")

except ValueError:
    print("Error: Debe ingresar un número entero")