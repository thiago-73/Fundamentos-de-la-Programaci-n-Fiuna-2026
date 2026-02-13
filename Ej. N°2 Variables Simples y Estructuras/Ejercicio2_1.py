# 2.1-Escriba un programa en que lea tres números enteros, positivos y verifique si los mismos pueden formar un triángulo rectángulo.

a = float(input("Ingrese lado 1: "))
b = float(input("Ingrese lado 2: "))
c = float(input("Ingrese lado 3: "))

if a + b > c and a + c > b and b + c > a:
    print("Sí pueden formar un triángulo")
else:
    print("No pueden formar un triángulo")