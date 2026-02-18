# Programa que verifica si tres números pueden ser longitudes de los lados de un triángulo
# Para que tres números a, b, c formen un triángulo:
# Deben cumplir la "desigualdad triangular":
# a + b > c
# a + c > b
# b + c > a

# ----------------------------------------------------------
# FUNCION PARA PEDIR NÚMEROS CON VALIDACIÓN
# ----------------------------------------------------------
def pedir_numero(mensaje):
    while True:
        try:
            # float permite ingresar números decimales
            num = float(input(mensaje))
            
            # Los lados no pueden ser negativos ni cero
            if num > 0:
                return num
            else:
                print("El número debe ser mayor que 0.")
        except ValueError:
            print("Error: Debe ingresar un número válido.")

# Pedimos los tres lados
a = pedir_numero("Ingrese lado 1: ")
b = pedir_numero("Ingrese lado 2: ")
c = pedir_numero("Ingrese lado 3: ")

# ----------------------------------------------------------
# VERIFICACIÓN DE LA DESIGUALDAD TRIANGULAR
# ----------------------------------------------------------
if a + b > c and a + c > b and b + c > a:
    print("Sí pueden formar un triángulo")
else:
    print("No pueden formar un triángulo")
