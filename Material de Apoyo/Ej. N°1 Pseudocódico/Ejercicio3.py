# 3. Diseñar un algoritmo que lea dos números y verifique
# si uno de ellos es divisor del otro y viceversa.
#
# Un número es divisor de otro si la división es exacta,
# es decir, si el residuo es 0.

print("Verificar divisor.")

# Pedimos el primer número entero
# Usamos validación para evitar que el usuario ingrese letras u otros valores inválidos
while True:
    try:
        # int() convierte el valor ingresado en número entero
        a = int(input("Ingrese primer número: "))
        break  # Si el número es válido, salimos del bucle
    except ValueError:
        # Este error ocurre si el usuario no ingresa un número entero
        print("Error: Debe ingresar un número entero válido.")

# Pedimos el segundo número entero
while True:
    try:
        b = int(input("Ingrese segundo número: "))
        break
    except ValueError:
        print("Error: Debe ingresar un número entero válido.")

# IMPORTANTE:
# El operador % se llama "módulo" o "residuo"
# Devuelve el resto de una división
#
# Ejemplos:
# 10 % 2 = 0   → 2 es divisor de 10
# 10 % 3 = 1   → 3 NO es divisor de 10

# Verificamos si b es divisor de a
# Es decir, si al dividir a entre b el residuo es 0
if a % b == 0:
    print(f"{b} es divisor de {a}.")

# Verificamos si a es divisor de b
elif b % a == 0:
    print(f"{a} es divisor de {b}.")

# Si ninguna de las condiciones anteriores se cumple,
# entonces no son divisores entre sí
else:
    print("No son divisores entre sí.")
