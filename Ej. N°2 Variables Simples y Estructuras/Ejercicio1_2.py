# 1.2-Escriba un programa que lea por teclado un valor de temperatura en grados Celsius y lo convierta a grados Fahrenheit.

print("Conversor de grados Celsius (°C) a Fahrenheit (°F)")

n = float(input("Ingrese grados en celsius: "))

f = (n * (9 / 5)) + 32

print(f"Son {f} grados fahrenheit")
