# Programa que lee cuatro números y muestra el mayor de ellos

print("Ingrese 4 números para verificar cuál es el mayor.")

# ----------------------------------------------------------
# FUNCION PARA PEDIR NÚMEROS CON VALIDACIÓN
# ----------------------------------------------------------
def pedir_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))  # float permite decimales
        except ValueError:
            print("Error: Debe ingresar un número válido.")

# Pedimos los cuatro números
n1 = pedir_numero("Ingrese primer número: ")
n2 = pedir_numero("Ingrese segundo número: ")
n3 = pedir_numero("Ingrese tercer número: ")
n4 = pedir_numero("Ingrese cuarto número: ")

# ----------------------------------------------------------
# DETERMINAR EL MAYOR
# ----------------------------------------------------------
# La función max() devuelve el mayor de los valores ingresados
m = max(n1, n2, n3, n4)

# Mostramos el resultado
print(f"El mayor número es {m}")
