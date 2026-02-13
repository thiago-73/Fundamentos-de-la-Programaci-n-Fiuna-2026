# Elaborar un programa en que solicite al usuario que introduzca por teclado el valor de cuatro variables A, B, C y D, y que verifique que A pertenezca al intervalo (C;D) y que B no pertenezca al mismo. De cumplirse ambas condiciones, imprimir A, B y A+B, sino imprimir A, B y A-B.

print("Ingrese 4 números.")

A = int(input("Ingrese primer valor: "))
B = int(input("Ingrese segundo valor: "))
C = int(input("Ingrese tercer valor: "))
D = int(input("Ingrese cuarto valor: "))

if A > C and A < D and (B <= C or B >= D):
    s = A + B
    print(f"El valor de A es {A}, el de B es {B} y la suma es de {s}")
else:
    r = A - B
    print(f"El valor de A es {A}, el de B es {B} y la diferencia es de {r}")