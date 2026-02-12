# 10. Diseñar un algoritmo que determine si un numero es primo.

n = int(input("Ingrese número: "))
i = 2

while i < n:
    r = n % i 
    if r == 0:
        break
    else:
        i += 1

if i == n:
    print(F"{n} es primo")
else:
    print(F"{n} no es primo")
    