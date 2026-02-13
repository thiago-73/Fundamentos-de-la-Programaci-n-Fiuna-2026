# 3.2-Escriba un programa en que lea un número entero y positivo y luego verifique si el número es primo.

while True:  
    n = int(input("Ingrese número: "))
    
    if n > 1:
        break

i = 2

while n > i:
    r = n % i
    if r == 0:
        break
    else:
        i += 1
        
if i == n:
      print(F"{n} es primo")
else:
    print(F"{n} no es primo")
    