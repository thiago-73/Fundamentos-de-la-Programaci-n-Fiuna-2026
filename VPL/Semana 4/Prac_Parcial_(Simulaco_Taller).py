n = input()

if not n.isdigit() or int(n) <= 0:
    print("Error: numero de mediciones invalido")
else:
    n = int(n)
    sensor = input()

    registros = []

    for _ in range(n):
        r = input()

        if not r.isdigit() or len(r) != 4:
            print("Error: registro invalido")
            exit()

        registros.append(r)

    print(f"Sensor: {sensor}")

    valores = []

    for r in registros:
        tipo = int(r[0])
        valor = int(r[1:3])
        sensor_id = int(r[3])

        print(f"SensorID {sensor_id} Tipo {tipo} Valor {valor}")
        valores.append(valor)

    print(f"Valor maximo: {max(valores)}")