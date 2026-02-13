# 3.3-Escriba un programa en C++ que lea un número entero y positivo n. Luego obtenga e imprima el primer par de números primos gemelos mayores que n.


def primo(num):
    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0: 
            return False
    return True

while True:  
    n = int(input("Ingrese número: "))
    
    if n >= 0:
        break

k = n

while True:
    k += 1
    if primo(k) and primo(k + 2):
        print(f"Los primos gemelos mayores a {n} son {k} y {k + 2}")
        break
    
    
