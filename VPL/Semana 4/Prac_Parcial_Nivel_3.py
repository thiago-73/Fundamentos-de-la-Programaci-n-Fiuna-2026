# Función que determina si un año es bisiesto
def es_bisiesto(año):
    # Un año es bisiesto si es divisible entre 4
    # excepto los múltiplos de 100 que no son múltiplos de 400
    return (año % 4 == 0) and ((año % 100 != 0) or (año % 400 == 0))

# Bloque try para capturar errores si el usuario no ingresa un número válido
try:
    # Se solicita al usuario la cantidad de días desde 1970
    dias_totales = int(input())

    # Validación de que el número sea positivo
    if dias_totales < 0:
        print("Error: El timestamp debe ser un número entero positivo")
    else:
        # Guardamos el valor original de días
        timestamp = dias_totales
        # Año inicial
        año = 1970

        print(f"{dias_totales} días después de 1970:")

        # Bucle que se repite hasta determinar el año correspondiente
        while True:
            # Verificamos si el año actual es bisiesto
            if es_bisiesto(año):
                dias_año = 366
                tipo = "bisiesto"
            else:
                dias_año = 365
                tipo = "normal"

            # Si los días restantes superan los del año actual
            if timestamp >= dias_año:
                # Restamos los días del año actual del total
                timestamp -= dias_año
                
                # Mostramos información intermedia
                print(f"{año} es {tipo} ({dias_año} días), resto: {timestamp}")
                
                # Pasamos al siguiente año
                año += 1
            else:
                # Si los días restantes no completan un año, salimos del bucle
                break

        # Se muestra el año final y los días sobrantes
        print(f"Año: {año}, sobran {timestamp} días")

# Capturamos el error si el usuario no ingresa un número entero
except ValueError:
    print("Error: Debe ingresar un número entero")