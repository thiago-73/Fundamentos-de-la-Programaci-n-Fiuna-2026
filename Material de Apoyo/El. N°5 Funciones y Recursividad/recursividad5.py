# 5. Escribir una función recursiva para determinar si un número es capicúa.

while n > 0:
    




while True:
    try:
        n = int(input("Ingrese un número entero positivo: "))
        
        if n >= 0:
            break  
        else:
            print("Ingrese un número positivo.")
            
    except ValueError:
        print("Valor inválido.")