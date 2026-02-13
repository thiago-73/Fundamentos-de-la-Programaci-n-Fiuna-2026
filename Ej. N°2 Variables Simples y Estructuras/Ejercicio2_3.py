# 2.3-Escriba un programa en que lea cuatro números y obtenga el mayor y menor de los números.

numeros = []

for i in range(4):
    n = float(input(f"Ingrese número {i+1}: "))
    numeros.append(n)

mayor = max(numeros)
menor = min(numeros)

print(f"Mayor: {mayor}")
print(f"Menor: {menor}")