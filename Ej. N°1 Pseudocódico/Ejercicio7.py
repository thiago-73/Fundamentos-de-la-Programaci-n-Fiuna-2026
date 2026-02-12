# 7. Diseñar un algoritmo que lea e imprima una serie de números distintos de cero. El algoritmo debe terminar con un valor cero que no se debe imprimir. Visualizar el numero de valores leídos.

print("Leer series de números.")

c = 0

while True:
    n = int(input("Ingrese un números para ser leidos: "))
    c += 1
    
    if n == 0:
        print("El número 0 no puede ser leído.")
        break
    
    print(n)

print(f"El número de valores leídos es {c}")