# Programa que calcula el factorial de un número entero positivo
# El factorial de n se define como: n! = 1 * 2 * 3 * ... * n

# ----------------------------------------------------------
# VALIDAR ENTRADA
# ----------------------------------------------------------
while True:
    try:
        n = int(input("Ingrese número entero positivo: "))
        if n >= 0:
            break
        else:
            print("Error: El número debe ser mayor o igual a 0.")
    except ValueError:
        print("Error: Debe ingresar un número entero válido.")

# ----------------------------------------------------------
# CALCULO DEL FACTORIAL
# ----------------------------------------------------------
f = 1  # Inicializamos el factorial en 1

# Multiplicamos todos los números de 1 hasta n
for i in range(1, n + 1):
    f *= i

# ----------------------------------------------------------
# MOSTRAR RESULTADO
# ----------------------------------------------------------
print(f"{n}! es: {f}")
