# Programa que calcula el área de un triángulo usando la fórmula de Herón
# Fórmula de Herón:
# Área = √(s * (s - a) * (s - b) * (s - c))
# Donde s = (a + b + c) / 2 es el semiperímetro del triángulo

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
a = pedir_lado("Ingrese primer lado: ")
b = pedir_lado("Ingrese segundo lado: ")
c = pedir_lado("Ingrese tercer lado: ")

# ----------------------------------------------------------
# VERIFICAR SI LOS LADOS PUEDEN FORMAR UN TRIÁNGULO
# ----------------------------------------------------------
if a + b > c and a + c > b and b + c > a:
    # Calculamos el semiperímetro
    s = (a + b + c) / 2
    
    # Fórmula de Herón para el área
    p = s * (s - a) * (s - b) * (s - c)
    área = p ** 0.5
    
    print(f"El área del triángulo es {área}")
else:
    print("Los lados ingresados no pueden formar un triángulo")
