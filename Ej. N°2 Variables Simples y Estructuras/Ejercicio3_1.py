# 3.1-Escriba un programa en que lea un número entero n, calcule e imprima el factorial del mismo.

n = int(input("Ingrese número: "))
f = 1

for i in range(1, n + 1):
    f *= i

print(f"{n}! es: {f}")