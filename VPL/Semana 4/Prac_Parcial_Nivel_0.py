try:
    timestamp = int(input())

    if timestamp < 0:
        print("Error: El timestamp debe ser un número entero positivo")
    else:
        dias = timestamp // 86400
        resto = timestamp % 86400

        print(f"Timestamp: {timestamp} segundos")
        print(f"Días: {dias}")
        print(f"Segundos restantes: {resto}")

except ValueError:
    print("Error: Debe ingresar un número entero")