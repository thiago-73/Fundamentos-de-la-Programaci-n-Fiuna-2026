# Programa que valida si una fecha ingresada por el usuario es correcta
# Considera años bisiestos para febrero

# ----------------------------------------------------------
# FUNCIONES AUXILIARES
# ----------------------------------------------------------
def bisiesto(año):
    """
    Devuelve True si el año es bisiesto, False si no
    Un año es bisiesto si:
    - divisible por 4 y no por 100, o
    - divisible por 400
    """
    return ((año % 4 == 0) and (año % 100 != 0)) or (año % 400 == 0)

def validacion(dia, mes, año):
    """
    Devuelve True si la fecha es válida, False si no
    """
    # Año debe ser positivo
    if año < 1:
        return False

    # Mes debe estar entre 1 y 12
    if mes < 1 or mes > 12:
        return False

    # Días de cada mes
    mes_dia = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Febrero tiene 29 días si el año es bisiesto
    if bisiesto(año) and mes == 2:
        mes_dia[2] = 29

    # Día debe estar entre 1 y el máximo del mes
    if dia < 1 or dia > mes_dia[mes]:
        return False

    return True

# ----------------------------------------------------------
# PEDIR DÍA, MES Y AÑO CON VALIDACIÓN
# ----------------------------------------------------------
def pedir_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor > 0:
                return valor
            else:
                print("Error: Debe ser un número positivo.")
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")

dia = pedir_entero("Ingrese el día: ")
mes = pedir_entero("Ingrese el mes: ")
año = pedir_entero("Ingrese el año: ")

# ----------------------------------------------------------
# VERIFICAR SI LA FECHA ES VÁLIDA
# ----------------------------------------------------------
if validacion(dia, mes, año):
    print("La fecha es válida.")
else:
    print("La fecha es inválida.")
