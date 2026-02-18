# Programa que verifica si un número entero positivo es primo
# Un número primo es aquel que solo es divisible entre 1 y sí mismo

# ----------------------------------------------------------
# VALIDAR ENTRADA
# ----------------------------------------------------------
while True:
    try:
        n = int(input("Ingrese número entero positivo mayor que 1: "))
        if n > 1:
            break
        else:
            print("Error: El número debe ser mayor que 1.")
    except ValueError:
        print("Error: Debe ingresar un número entero válido.")

# ----------------------------------------------------------
# VERIFICAR SI EL NÚMERO ES PRIMO
# ----------------------------------------------------------
i = 2  # Comenzamos a probar divisores desde 2

while n > i:
    r = n % i  # Residuo de dividir n entre i
    if r == 0:
        break  # Si hay residuo 0, no es primo
    else:
        i += 1  # Si no, probamos con el siguiente número

# ----------------------------------------------------------
# MOSTRAR RESULTADO
# ----------------------------------------------------------
if i == n:
    print(f"{n} es primo")
else:
    print(f"{n} no es primo")
