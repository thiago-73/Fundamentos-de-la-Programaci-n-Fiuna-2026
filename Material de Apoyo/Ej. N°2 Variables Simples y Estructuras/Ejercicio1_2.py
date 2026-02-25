# Programa que convierte una temperatura de grados Celsius a Fahrenheit
# Fórmula de conversión: F = (C * 9/5) + 32

print("Conversor de grados Celsius (°C) a Fahrenheit (°F)")

# ----------------------------------------------------------
# VALIDACIÓN DE ENTRADA
# ----------------------------------------------------------
while True:
    try:
        n = float(input("Ingrese grados en Celsius: "))
        break  # si se ingresó un número válido, salimos del bucle
    except ValueError:
        print("Error: Debe ingresar un número válido.")

# ----------------------------------------------------------
# CONVERSIÓN A FAHRENHEIT
# ----------------------------------------------------------
f = (n * (9 / 5)) + 32

# ----------------------------------------------------------
# MOSTRAR RESULTADO
# ----------------------------------------------------------
print(f"{n} °C son {f} °F")
