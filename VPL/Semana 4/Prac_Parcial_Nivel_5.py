# Leer múltiples líneas hasta que no haya más entrada
while True:
    try:
        # Leer una línea y eliminar espacios en blanco al inicio y al final
        entrada = input().strip()

        # Si la línea está vacía, ignorarla y pasar a la siguiente
        if not entrada:
            continue

        try:
            # Intentar convertir la entrada a número entero
            timestamp = int(entrada)

            # Validar que el timestamp sea positivo
            if timestamp < 0:
                print("Error: El timestamp debe ser un número entero positivo")
            else:
                print("Timestamp:", timestamp)

                # Calcular los segundos que sobran después de sacar los días completos
                segundos_restantes = timestamp % 86400

                # Extraer hora, minuto y segundo de los segundos restantes
                hora = segundos_restantes // 3600
                minuto = (segundos_restantes % 3600) // 60
                segundo = segundos_restantes % 60

                # Calcular cuántos días completos han pasado desde el 1 de enero de 1970
                dias = timestamp // 86400
                año = 1970

                # Restar años completos hasta que los días restantes quepan en el año actual
                while True:
                    # Determinar si el año actual es bisiesto (366 días) o no (365 días)
                    dias_año = 366 if (año % 4 == 0 and (año % 100 != 0 or año % 400 == 0)) else 365

                    # Si quedan más días que los del año actual, pasar al siguiente año
                    if dias >= dias_año:
                        dias -= dias_año
                        año += 1
                    else:
                        # Los días restantes pertenecen al año actual
                        break

                # Verificar si el año final es bisiesto para armar la lista de meses correcta
                bisiesto = año % 4 == 0 and (año % 100 != 0 or año % 400 == 0)

                # Lista con la cantidad de días de cada mes (febrero tiene 29 si es bisiesto)
                meses = [31, 29 if bisiesto else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

                mes = 1

                # Restar meses completos hasta encontrar en qué mes cae el día restante
                for dias_mes in meses:
                    if dias >= dias_mes:
                        dias -= dias_mes
                        mes += 1
                    else:
                        # Los días restantes pertenecen al mes actual
                        break

                # El día es los días restantes + 1 porque los días empiezan en 1, no en 0
                dia = dias + 1

                # Mostrar la fecha y hora en formato YYYY-MM-DD HH:MM:SS
                print(f"Fecha UTC: {año:04}-{mes:02}-{dia:02} {hora:02}:{minuto:02}:{segundo:02}")

        except ValueError:
            # Si la entrada no es un número entero, mostrar error
            print("Error: El timestamp debe ser un número entero positivo")

    except EOFError:
        # Cuando no hay más líneas para leer, terminar el programa
        break