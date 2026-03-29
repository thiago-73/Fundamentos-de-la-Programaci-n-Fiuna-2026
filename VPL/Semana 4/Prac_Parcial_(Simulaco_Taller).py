# Se solicita el número de mediciones al usuario
n = input()

# Verificamos que el valor ingresado sea un número entero positivo
if not n.isdigit() or int(n) <= 0:
    print("Error: numero de mediciones invalido")
else:
    # Convertimos el valor a entero, ya que pasó la validación
    n = int(n)
    
    # Se solicita el nombre del sensor
    sensor = input()

    # Lista donde se guardarán los registros ingresados
    registros = []

    # Se leen n registros del usuario
    for _ in range(n):
        r = input()

        # Cada registro debe ser un número de 4 dígitos
        # isdigit() verifica que todos los caracteres sean dígitos
        # len(r) == 4 asegura que tenga exactamente 4 dígitos
        if not r.isdigit() or len(r) != 4:
            print("Error: registro invalido")
            exit()  # Sale del programa si hay un registro inválido

        # Se agrega el registro válido a la lista
        registros.append(r)

    # Se imprime el nombre del sensor
    print(f"Sensor: {sensor}")

    # Lista donde se guardarán los valores extraídos de cada registro
    valores = []

    # Se procesan los registros uno por uno
    for r in registros:
        # El primer dígito indica el tipo de sensor
        tipo = int(r[0])
        
        # Los dígitos 1 y 2 (índices 1:3) indican el valor del registro
        valor = int(r[1:3])
        
        # El último dígito indica el ID del sensor
        sensor_id = int(r[3])

        # Se imprime el registro desglosado
        print(f"SensorID {sensor_id} Tipo {tipo} Valor {valor}")
        
        # Se guarda el valor en la lista de valores
        valores.append(valor)

    # Se imprime el valor máximo entre todos los registros
    print(f"Valor maximo: {max(valores)}")