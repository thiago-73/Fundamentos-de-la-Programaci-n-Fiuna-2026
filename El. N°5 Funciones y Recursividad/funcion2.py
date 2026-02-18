# 2. Escriba un programa en C++ que lea un número entero y positivo (validar).
# Obtenga un nuevo número invirtiendo el orden de sus cifras y determine
# la diferencia entre el numero obtenido y el ingresado por teclado
# (restar el mayor del menor).
#
# Este programa:
# 1. Pide un número entero positivo.
# 2. Invierte sus cifras.
# 3. Compara ambos números.
# 4. Resta el mayor menos el menor.

# ----------------------------------------------------------
# MÉTODO 1: Invertir usando operaciones matemáticas
# ----------------------------------------------------------
def invertir1(n):

    # Variable donde construiremos el número invertido
    invertido = 0
    
    # Mientras el número sea mayor que 0
    while n > 0:

        # Obtenemos el último dígito usando módulo (%)
        # Ejemplo: 123 % 10 = 3
        digito = n % 10

        # Construimos el número invertido
        # Multiplicamos por 10 para "mover" las cifras a la izquierda
        # y sumamos el nuevo dígito
        invertido = invertido * 10 + digito

        # Eliminamos el último dígito del número original
        # // es división entera
        # Ejemplo: 123 // 10 = 12
        n = n // 10
    
    return invertido


# ----------------------------------------------------------
# MÉTODO 2: Invertir usando cadenas (string)
# ----------------------------------------------------------
def invertir2(n):

    # Convertimos el número a texto con str()
    # [::-1] invierte el texto
    # Luego lo convertimos nuevamente a entero con int()
    invertido = int(str(n)[::-1])  
    
    return invertido


# ----------------------------------------------------------
# VALIDACIÓN DEL NÚMERO INGRESADO
# ----------------------------------------------------------
while True:
    try:
        # Pedimos el número y lo convertimos a entero
        n = int(input("Ingrese número entero positivo: "))
        
        # Verificamos que sea mayor a 0
        if n > 0:
            break
        else:
            print("El número debe ser mayor a 0")
    
    except ValueError:
        # Si el usuario escribe letras o símbolos,
        # evitamos que el programa se rompa
        print("Error: Debe ingresar un número entero válido.")


# ----------------------------------------------------------
# COMPARACIÓN Y RESTA
# ----------------------------------------------------------

# Si el número original es menor que su versión invertida
if n < invertir2(n):

    # Restamos el mayor menos el menor
    r = n - invertir2(n)

    print(f"{invertir2(n)} es mayor a {n} y la resta de el mayor del menor es {r}")

# Si el número es igual a su versión invertida (capicúa)
elif n == invertir1(n):

    # Número capicúa: se lee igual de izquierda a derecha
    # y de derecha a izquierda
    print(f"{n} es capicúa, por lo tanto la diferencia es 0")

# Si el número original es mayor que el invertido
else:

    r = invertir2(n) - n

    print(f"{n} es mayor que {invertir2(n)} y la resta de el mayor del menor es {r}")
