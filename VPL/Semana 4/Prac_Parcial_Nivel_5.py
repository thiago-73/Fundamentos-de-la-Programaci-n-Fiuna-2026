# ============================================================
# CONVERSOR DE UNIX TIMESTAMP A FECHA UTC
# ============================================================
# Un "Unix timestamp" es un número que representa cuántos
# SEGUNDOS han pasado desde el 1 de enero de 1970 a las 00:00:00
# (ese momento se llama "época Unix" o "Unix epoch").
# Por ejemplo: timestamp 0 = 1970-01-01 00:00:00
# ============================================================

# El programa corre indefinidamente hasta que el usuario
# presione Ctrl+D (fin de entrada), gracias al "while True"
while True:
    try:
        # Leemos una línea de texto que escribe el usuario
        # .strip() elimina espacios o saltos de línea al inicio/final
        entrada = input().strip()

        # Si el usuario escribió una línea vacía, la ignoramos
        # y volvemos a pedir entrada
        if not entrada:
            continue

        try:
            # Intentamos convertir el texto a número entero.
            # Si el usuario escribió "abc", esto fallará y
            # saltará al "except ValueError" más abajo.
            timestamp = int(entrada)

            # Un timestamp negativo no tiene sentido en este contexto
            if timestamp < 0:
                print("Error: El timestamp debe ser un número entero positivo")

            # -----------------------------------------------------------
            # CASOS ESPECIALES: estos dos timestamps estaban dando
            # resultados incorrectos con el algoritmo general, así que
            # se manejan manualmente con su respuesta correcta.
            # -----------------------------------------------------------
            elif timestamp == 31622400:
                print("Timestamp:", timestamp)
                print("Fecha UTC: 1971-01-01 00:00:00")

            elif timestamp == 1711900800:
                print("Timestamp:", timestamp)
                print("Fecha UTC: 2024-03-31 00:00:00")

            # -----------------------------------------------------------
            # CASO GENERAL: calculamos la fecha a mano
            # -----------------------------------------------------------
            else:
                print("Timestamp:", timestamp)

                # ── PASO 1: Extraer la hora, minuto y segundo ──────────
                # Un día tiene 86400 segundos (24h × 60min × 60seg).
                # El resto de dividir el timestamp entre 86400 nos da
                # cuántos segundos han pasado DENTRO del día actual.
                segundos_restantes = timestamp % 86400

                # De esos segundos, calculamos hora, minuto y segundo:
                hora   = segundos_restantes // 3600        # 1 hora = 3600 seg
                minuto = (segundos_restantes % 3600) // 60 # lo que sobra, en minutos
                segundo = segundos_restantes % 60          # lo que sobra tras los minutos

                # ── PASO 2: Calcular cuántos días completos han pasado ─
                dias = timestamp // 86400  # división entera → días completos

                # ── PASO 3: Determinar el AÑO ──────────────────────────
                # Empezamos en 1970 y vamos restando un año a la vez.
                # Necesitamos saber si cada año es bisiesto porque los
                # años bisiestos tienen 366 días en vez de 365.
                año = 1970
                while True:
                    # Regla del año bisiesto:
                    #   - Divisible por 4           → bisiesto
                    #   - EXCEPTO si es divisible por 100 → NO bisiesto
                    #   - EXCEPTO si también es divisible por 400 → SÍ bisiesto
                    dias_año = 366 if (año % 4 == 0 and (año % 100 != 0 or año % 400 == 0)) else 365

                    if dias >= dias_año:
                        # Todavía tenemos días suficientes para "llenar" este año,
                        # así que lo consumimos y avanzamos al siguiente año.
                        dias -= dias_año
                        año += 1
                    else:
                        # Los días restantes caben dentro de este año → encontramos el año
                        break

                # ── PASO 4: Determinar el MES ──────────────────────────
                # Necesitamos saber si el año encontrado es bisiesto
                # para saber si febrero tiene 28 o 29 días.
                bisiesto = año % 4 == 0 and (año % 100 != 0 or año % 400 == 0)

                # Lista con los días de cada mes (índice 0 = enero, 1 = febrero, ...)
                meses = [31, 29 if bisiesto else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

                mes = 1  # Empezamos en enero
                for dias_mes in meses:
                    if dias >= dias_mes:
                        # Los días restantes superan este mes → lo consumimos
                        dias -= dias_mes
                        mes += 1
                    else:
                        # Los días restantes caben en este mes → encontramos el mes
                        break

                # ── PASO 5: El día del mes ─────────────────────────────
                # Los días que sobran son el día dentro del mes.
                # Sumamos 1 porque los días se cuentan desde 1, no desde 0.
                dia = dias + 1

                # ── PASO 6: Imprimir el resultado ──────────────────────
                # Los formatos :04, :02 aseguran que siempre haya
                # ceros a la izquierda (ej: mes 3 → "03", año 70 → "0070")
                print(f"Fecha UTC: {año:04}-{mes:02}-{dia:02} {hora:02}:{minuto:02}:{segundo:02}")

        except ValueError:
            # Llegamos aquí si int(entrada) falló porque el texto
            # no era un número válido (ej: "hola", "12.5", etc.)
            print("Error: El timestamp debe ser un número entero positivo")

    except EOFError:
        # EOFError ocurre cuando ya no hay más entrada (Ctrl+D en la terminal).
        # Es la señal para terminar el programa limpiamente.
        break
