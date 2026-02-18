# Programa que determina si un número es primo
# Un número primo es aquel mayor que 1 que solo tiene divisores 1 y él mismo

# ----------------------------------------------------------
# VALIDACIÓN DE ENTRADA
# ----------------------------------------------------------
while True:
    try:
        n = int(input("Ingrese un número entero positivo: "))
        if n > 0:
            break
        else:
            print("Error: El número debe ser mayor que 0.")
    except ValueError:
        print("Error: Debe ingresar un número entero válido.")

# ----------------------------------------------------------
# VERIFICACIÓN DE PRIMALIDAD
# ----------------------------------------------------------
i = 2  # Comenzamos a probar divisores desde 2

while i < n:
    r = n % i  # residuo de la división
    if r == 0:
        # Si encontramos un divisor → no es primo
        break
    else:
        # Si no, seguimos probando el siguiente número
        i += 1

# Si llegamos a i == n → no encontramos divisores → es primo
if i == n:
    print(f"{n} es primo")
else:
    print(f"{n} no es primo")
