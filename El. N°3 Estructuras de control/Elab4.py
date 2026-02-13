# Elaborar un programa en que solicite al usuario que introduzca por teclado 3 números, luego que imprima en pantalla si los mismos pueden ser longitudes de los lados de un triángulo.

a = float(input("Ingrese lado 1: "))
b = float(input("Ingrese lado 2: "))
c = float(input("Ingrese lado 3: "))

if a + b > c and a + c > b and b + c > a:
    print("Sí pueden formar un triángulo")
else:
    print("No pueden formar un triángulo")