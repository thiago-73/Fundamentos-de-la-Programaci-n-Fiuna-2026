# 1.1-Escriba un programa que reciba la dimensión de los lados de un triángulo y luego calcule su área usando la fórmula de Heron.

a = float(input("Ingrese primer lado: "))
b = float(input("Ingrese segundo lado: "))
c = float(input("Ingrese tercer lado: "))

s = (a + b + c) / 2
p = s * (s - a) * (s - b) * (s - c)
área = p ** 0.5

print(f"El área del triángulo es {área}")
