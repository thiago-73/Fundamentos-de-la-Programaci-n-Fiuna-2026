# 1.3-Escriba un programa en que lea dos números enteros, positivos, luego calcule el cociente y el resto de la división.

dividendo = float(input("Ingrese dividendo: "))
divisor = float(input("Ingrese divisor: "))

cociente = dividendo / divisor
resto = dividendo % divisor

print(f"El cociente entre {dividendo} y {divisor} es {cociente} y el resto {resto}")

