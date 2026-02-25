# Programa que verifica si tres números pueden formar un triángulo
# y si es un triángulo rectángulo
# Para un triángulo rectángulo se cumple el Teorema de Pitágoras: a² + b² = c²

# ----------------------------------------------------------
# FUNCION PARA PEDIR NÚMEROS POSITIVOS
# ----------------------------------------------------------
def pedir_lado(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor > 0:
                return valor
            else:
                print("Error: El lado debe ser mayor que 0.")
        except ValueError:
            print("Error: Debe ingresar un número válido.")

# Pedimos los tres lados
a = pedir_lado("Ingrese lado 1: ")
b = pedir_lado("Ingrese lado 2: ")
c = pedir_lado("Ingrese lado 3: ")

# ----------------------------------------------------------
# VERIFICAR SI PUEDEN FORMAR UN TRIÁNGULO
# ----------------------------------------------------------
if a + b > c and a + c > b and b + c > a:
    print("Sí pueden formar un triángulo")
    
    # ------------------------------------------------------
    # VERIFICAR SI ES TRIÁNGULO RECTÁNGULO
    # ------------------------------------------------------
    # Para esto, ordenamos los lados para identificar la hipotenusa
    lados = sorted([a, b, c])
    if round(lados[0]**2 + lados[1]**2, 5) == round(lados[2]**2, 5):
        print("Y es un triángulo rectángulo")
    else:
        print("Pero no es un triángulo rectángulo")
else:
    print("No pueden formar un triángulo")
