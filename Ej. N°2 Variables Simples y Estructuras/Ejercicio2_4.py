# 2.4- Escriba un programa en C++ que valide la fecha ingresada por el usuario. Se debe introducir por teclado el día, mes y año.


def bisiesto(año):
    return ((año % 4 == 0) and (año % 100 != 0)) or (año % 400 == 0)

def validación(dia, mes, año):
    if año < 1:
        return False
    if mes < 1 or mes > 12:
        return False

    mes_dia = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if bisiesto(año) and mes == 2:
        mes_dia[2] = 29
    if dia < 1 or dia > mes_dia[mes]:
        return False
    
    return True

dia = int(input("Ingrese el día: "))
mes = int(input("Ingrese el mes: "))
año = int(input("Ingrese el año: "))

if validación(dia, mes, año):
    print("La fecha es válida.")
else:
    print("La fecha es inválida.")

