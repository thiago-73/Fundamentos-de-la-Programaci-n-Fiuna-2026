# 6. Diseñar un algoritmo que imprima y sume la serie de números 3, 6, 9, 12 y 99.

k = 3

s = 0

for i in range(3, 100, 3):
    print(i)
    s += i

print("La suma es:", s)