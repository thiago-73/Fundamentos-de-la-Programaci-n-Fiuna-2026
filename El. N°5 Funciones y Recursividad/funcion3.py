# 3. La conjetura de Goldbach afirma que: "Todo número par mayor a 2 puede escribirse como la suma de dos números primos". Ejemplo: 20=13+7; 50=19+31. Elabore un programa que calcule las posibles sumas de Goldbach de un número.

def primo(num):
    if num < 2:
        return False
    
    for i in range(2, int((num ** 0.5)) + 1):
        if num % i == 0:
            return False
            
    return True

def goldbach(num):
    combinaciones = []
    
    for i in range(2, (num // 2) + 1):
        if primo(i) and primo(num - i):
            combinaciones.append((i, num - i))
    
    return combinaciones            

while True:
    num = int(input("Ingrese un número par positivo mayor a 2: "))
    
    if num > 2 and num % 2 == 0:
        break

resultado = goldbach(num)

if resultado:
    print(f"Formas de escribir {num} como suma de dos primos:")
    for a, b in resultado:
        print(f"{a} + {b}")
else:
    print(f"No se encontraron combinaciones para {num}")