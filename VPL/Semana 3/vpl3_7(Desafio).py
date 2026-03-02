# Se utiliza un bloque try para intentar convertir los valores ingresados por el usuario
# a números enteros. Esto permite detectar errores si el usuario ingresa texto u otro
# tipo de dato que no pueda convertirse a entero.
try:
    # Se solicita al usuario el día de la fecha
    dia = int(input())
    
    # Se solicita el mes de la fecha
    mes = int(input())
    
    # Se solicita el año de la fecha
    año = int(input())

# Si ocurre un error al convertir los datos (por ejemplo si se ingresa texto),
# se ejecuta este bloque.
except ValueError:
    print("No es una fecha valida!!")

# Si no ocurrió ningún error en la conversión de datos,
# el programa continúa con la validación de la fecha.
else:
    # Lista que contiene la cantidad de días de cada mes.
    # El índice 0 no se usa para que el número del mes coincida con su posición.
    dias_mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Se verifica que el año sea positivo
    if año > 0:
            # Se verifica si el año es bisiesto.
            # Un año es bisiesto si:
            # - es divisible por 4 y no por 100
            # - o es divisible por 400
            if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
                # Si el año es bisiesto, febrero tiene 29 días
                dias_mes[2] = 29
            
            # Se verifica si el mes está fuera del rango válido (1 a 12)
            if mes < 1 or mes > 12:
                print("No es una fecha valida!!")
            
            # Se verifica si el día está fuera del rango válido según el mes
            elif dia < 1 or dia > dias_mes[mes]:
                print("No es una fecha valida!!")
            
            # Si la fecha es válida, se calcula el día siguiente
            else: 
                # Si el día aún no es el último del mes
                if dia < dias_mes[mes]:
                    # Se incrementa el día en 1
                    dia += 1
                else:
                    # Si es el último día del mes, se reinicia el día a 1
                    dia = 1
                    
                    # Si el mes no es diciembre, se incrementa el mes
                    if mes < 12:
                        mes += 1
                    else:
                        # Si es diciembre, se reinicia el mes a enero
                        mes = 1
                        # Y se incrementa el año
                        año += 1

                # Se imprime la fecha del día siguiente usando formato de texto
                print(f"{dia}/{mes}/{año}")

    # Si el año no es positivo, la fecha se considera inválida
    else:
        print("No es una fecha valida!!")

