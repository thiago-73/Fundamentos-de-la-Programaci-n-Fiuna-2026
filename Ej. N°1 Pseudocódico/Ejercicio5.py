# 5. Diseñar un pseudocodigo que calcule el factorial de un numero

print("Calculo de factorial.")

n = int(input("Ingrese número: "))

k = n
f = 1

while n > 1:
    f *= n
    n -= 1

print(f"{k}! es: {f}")