# Programa que lee cuatro números A, B, C y D (pueden ser decimales)
# y verifica:
# 1. Que A esté dentro del intervalo (C, D)
# 2. Que B NO esté dentro del intervalo (C, D)
#
# Si ambas condiciones se cumplen → imprime A, B y A+B
# Sino → imprime A, B y A-B

print("Ingrese 4 números (pueden ser decimales).")

# ----------------------------------------------------------
# VALIDACIÓN DE ENTRADA CON NÚMEROS DECIMALES
# ----------------------------------------------------------
def pedir_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Error: Debe ingresar un número válido.")

# Pedimos cada valor
A = pedir_numero("Ingrese primer valor (A): ")
B = pedir_numero("Ingrese segundo valor (B): ")
C = pedir_numero("Ingrese tercer valor (C): ")
D = pedir_numero("Ingrese cuarto valor (D): ")

# ----------------------------------------------------------
# VERIFICACIÓN DE CONDICIONES
# ----------------------------------------------------------
# A está dentro del intervalo (C, D)
# B NO está dentro del intervalo (C, D) → B <= C o B >= D
if A > C and A < D and (B <= C or B >= D):
    suma = A + B
    print(f"El valor de A es {A}, el de B es {B} y la suma es de {suma}")
else:
    resta = A - B
    print(f"El valor de A es {A}, el de B es {B} y la diferencia es de {resta}")
