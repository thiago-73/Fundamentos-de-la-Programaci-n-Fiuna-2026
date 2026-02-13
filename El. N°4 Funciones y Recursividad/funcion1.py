# 1. Escriba un programa en que lea un número entero y positivo, obtenga e imprima todos sus factores primos.

def primo(num):
    if num <= 1:
        return False

    for x in range(2, num):
        if num % x == 0: 
            return False
    return True

while True:
    num = int(input("Ingrese número: "))
    
    if num > 0:
        break

primos = []

if primo(num):
    print(f"{num} es un número primo.")
else:
    for i in range(2, num + 1):
        if num % i == 0 and primo(i):
            primos.append(i)
        i += 1

    print("Factores primos:")
    for factor in primos:
        print(factor)
