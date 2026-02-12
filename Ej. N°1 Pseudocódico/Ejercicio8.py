# 8. Escribir un algoritmo que lea cuatro números y a continuación imprima el mayor de los cuatro.

print("Ingrese 4 números para verificar cuales mayor.")

n1 = float(input("Ingrese primer número: "))
n2 = float(input("Ingrese segundo número: "))
n3 = float(input("Ingrese tercer número: "))
n4 = float(input("Ingrese cuarto número: "))

m = max(n1, n2, n3, n4)

print(f"El mayor número es {m}")