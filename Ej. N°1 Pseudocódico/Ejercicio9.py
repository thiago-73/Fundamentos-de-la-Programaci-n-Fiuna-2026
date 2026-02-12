# 9. Diseñar un algoritmo que lea tres números y encuentre si uno de ellos es la suma de los otros dos.

n1 = float(input("Ingrese primer número: "))
n2 = float(input("Ingrese segundo número: "))
n3 = float(input("Ingrese tercer número: "))

if n1 + n2 == n3:
    print(f"{n3} es la suma de {n1} y {n2}")
elif n1 + n3 == n2:
    print(f"{n2} es la suma de {n1} y {n3}")
elif n2 + n3 == n1:
    print(f"{n1} es la suma de {n3} y {n2}")
else:
    print("Ninguno de los números es la suma de los otros 2")