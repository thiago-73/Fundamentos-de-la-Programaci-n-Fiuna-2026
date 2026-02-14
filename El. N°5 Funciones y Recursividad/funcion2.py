# 2. Escriba un programa en C++ que lea un número entero y positivo (validar). Obtenga un nuevo número invirtiendo el orden de sus cifras y determine la diferencia entre el numero obtenido y el ingresado por teclado (restar el mayor del menor).

def invertir1(n):
    invertido = 0
    
    while n > 0:
        digito = n % 10
        invertido = invertido * 10 + digito
        n = n // 10
    
    return invertido

def invertir2(n):
    invertido = int(str(n)[::-1])  
    
    return invertido

while True:
    n = int(input("Ingrese número entero positivo: "))
    
    if n > 0:
        break
    else:
        print("El número debe ser mayor a 0")
        
if n < invertir2(n):
    r = n - invertir2(n)
    print(f"{invertir2(n)} es mayor a {n} y la resta de el mayor del menor es {r}")
elif n == invertir1(n):
    print(f"{n} es capicúa, por lo tanto la diferencia es 0")
else:
    r = invertir2(n) - n
    print(f"{n} es mayor que {invertir2(n)} y la resta de el mayor del menor es {r}")