# 3. Diseñar un algoritmo que lea dos números y verifique si uno de ellos es divisor del otro y viceversa.

print("Verificar divisor.")

a = int(input("Ingrese primer número: "))
b = int(input("Ingrese segundo número: "))

if a % b == 0:
    print(f"{b} es divisor de {a}.")
elif b % a == 0:
    print(f"{a} es divisor de {b}.")
else:
    print("No son divisores entre sí.")