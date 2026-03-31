import random

# ============================================================
# PROCESADOR DE REGISTROS DE SENSOR
# ============================================================
# Este programa lee mediciones de un sensor y las interpreta.
# El formato en que están codificados los registros depende del
# último dígito de la cédula: par o impar.
# Como no tenemos la cédula real, se elige al azar (0 o 1).
# ============================================================

# Simulamos el último dígito de la cédula (0 = par, 1 = impar)
CEDULA_ULTIMO_DIGITO = random.choice([0, 1])

# ── PASO 1: Leer cuántas mediciones vamos a procesar ──────────
n = input()

# Validamos que sea un número entero positivo.
# .isdigit() devuelve True solo si todos los caracteres son dígitos (0-9).
if not n.isdigit() or int(n) <= 0:
    print("Error: numero de mediciones invalido")
else:
    n = int(n)  # Convertimos el texto a número ahora que sabemos que es válido

    # ── PASO 2: Leer el nombre/identificador del sensor ───────
    sensor = input()

    # ── PASO 3: Leer los n registros uno por uno ──────────────
    registros = []  # Lista vacía donde guardaremos cada registro leído
    for _ in range(n):  # El guión bajo "_" es convención cuando no usamos el índice
        r = input()

        # Cada registro debe ser exactamente 4 dígitos.
        # Si no cumple, avisamos y terminamos el programa con exit().
        if not r.isdigit() or len(r) != 4:
            print("Error: registro invalido")
            exit()

        registros.append(r)  # Guardamos el registro válido en la lista

    # ── PASO 4: Mostrar el nombre del sensor ──────────────────
    print(f"Sensor: {sensor}")

    # ── PASO 5: Interpretar cada registro según la cédula ─────
    # Cada registro es una cadena de 4 caracteres (dígitos).
    # La posición de cada campo (valor, sensor_id, tipo) dentro
    # de esos 4 caracteres cambia según si la cédula es par o impar.

    valores = []  # Aquí guardaremos solo los "valores" para calcular el máximo al final

    if CEDULA_ULTIMO_DIGITO % 2 == 0:
        # ── Formato PAR: los 4 dígitos se leen así ────────────
        # Posición: [ 0 ][ 1 ][ 2 ][ 3 ]
        # Campo:    [  valor  ][sid][tipo]
        # Ejemplo:  "4521" → valor=45, sensorID=2, tipo=1
        for r in registros:
            valor     = int(r[0:2])  # Primeros 2 caracteres → valor (ej: "45")
            sensor_id = int(r[2])    # Tercer carácter       → ID del sensor
            tipo      = int(r[3])    # Cuarto carácter       → tipo de medición

            print(f"SensorID {sensor_id} Tipo {tipo} Valor {valor}")
            valores.append(valor)
    else:
        # ── Formato IMPAR: los 4 dígitos se leen así ──────────
        # Posición: [ 0 ][ 1 ][ 2 ][ 3 ]
        # Campo:    [tipo][  valor  ][sid]
        # Ejemplo:  "4521" → tipo=4, valor=52, sensorID=1
        for r in registros:
            tipo      = int(r[0])    # Primer carácter        → tipo de medición
            valor     = int(r[1:3])  # Segundo y tercer car.  → valor (ej: "52")
            sensor_id = int(r[3])    # Cuarto carácter        → ID del sensor

            print(f"SensorID {sensor_id} Tipo {tipo} Valor {valor}")
            valores.append(valor)

    # ── PASO 6: Mostrar el valor máximo de todas las mediciones ─
    # max() recorre la lista y devuelve el número más grande.
    print(f"Valor maximo: {max(valores)}")
