# Programa que lee tres números y verifica si uno de ellos
# es la suma de los otros dos

# ----------------------------------------------------------
# FUNCION PARA PEDIR NÚMEROS CON VALIDACIÓN
# ----------------------------------------------------------
def pedir_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))  # Permite decimales
        except ValueError:
            print("Error: Debe ingresar un número válido.")

# Pedimos los tres números
n1 = pedir_numero("Ingrese primer número: ")
n2 = pedir_numero("Ingrese segundo número: ")
n3 = pedir_numero("Ingrese tercer número: ")

# ----------------------------------------------------------
# VERIFICAR SI ALGUNO ES SUMA DE LOS OTROS DOS
# ----------------------------------------------------------
if n1 + n2 == n3:
    print(f"{n3} es la suma de {n1} y {n2}")
elif n1 + n3 == n2:
    print(f"{n2} es la suma de {n1} y {n3}")
elif n2 + n3 == n1:
    print(f"{n1} es la suma de {n2} y {n3}")
else:
    print("Ninguno de los números es la suma de los otros 2")
