# Programa que lee cuatro números y muestra el mayor y el menor

# ----------------------------------------------------------
# FUNCION PARA PEDIR UN NÚMERO VÁLIDO
# ----------------------------------------------------------
def pedir_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))  # Permite decimales
        except ValueError:
            print("Error: Debe ingresar un número válido.")

# Lista para almacenar los números ingresados
numeros = []

# Pedimos los cuatro números
for i in range(4):
    n = pedir_numero(f"Ingrese número {i+1}: ")
    numeros.append(n)

# ----------------------------------------------------------
# DETERMINAR MAYOR Y MENOR
# ----------------------------------------------------------
mayor = max(numeros)
menor = min(numeros)

# Mostramos el resultado
print(f"Mayor: {mayor}")
print(f"Menor: {menor}")
