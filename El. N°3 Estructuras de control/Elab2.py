# Elaborar un programa en que solicite al usuario que introduzca por teclado el valor de la edad de tres personas, luego determine e imprima en pantalla el promedio de dichas edades, a continuación decrementar unitariamente el promedio si es mayor a la primera edad, caso contrario incrementar unitariamente. Imprimir en pantalla el resultado.

edades = []

for i in range(3):
    edad = int(input("Ingrese edades: "))
    edades.append(edad)
    
prom = sum(edades) / len(edades)

print(f"El promedio de las edades es {prom}")

if prom > edades[0]:
    prom -= 1  
    print(f"El promedio es mayor que la primera edad, se decrementa unitariamente: {prom}")
else:
    prom += 1  
    print(f"El promedio es menor o igual que la primera edad, se incrementa unitariamente: {prom}")