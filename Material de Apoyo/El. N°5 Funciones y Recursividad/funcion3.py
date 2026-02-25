# 3. La conjetura de Goldbach afirma que:
# "Todo número par mayor a 2 puede escribirse como la suma de dos números primos".
#
# Ejemplo:
# 20 = 13 + 7
# 50 = 19 + 31
#
# Este programa calcula todas las posibles combinaciones
# de dos números primos que suman el número dado.

# ----------------------------------------------------------
# FUNCIÓN PARA VERIFICAR SI UN NÚMERO ES PRIMO
# ----------------------------------------------------------
def primo(num):

    # Los números menores que 2 NO son primos
    if num < 2:
        return False
    
    # Solo necesitamos comprobar divisores hasta la raíz cuadrada del número
    # Esto hace el algoritmo más eficiente
    for i in range(2, int((num ** 0.5)) + 1):

        # Si el número es divisible exactamente, no es primo
        if num % i == 0:
            return False
            
    # Si ningún número lo divide, es primo
    return True


# ----------------------------------------------------------
# FUNCIÓN QUE CALCULA LAS COMBINACIONES DE GOLDBACH
# ----------------------------------------------------------
def goldbach(num):

    # Lista donde guardaremos las combinaciones encontradas
    combinaciones = []
    
    # Recorremos desde 2 hasta la mitad del número
    # No necesitamos recorrer todo el número porque
    # las combinaciones se repetirían
    for i in range(2, (num // 2) + 1):

        # Verificamos:
        # 1. i es primo
        # 2. num - i también es primo
        if primo(i) and primo(num - i):

            # Guardamos la combinación como una tupla (i, num - i)
            combinaciones.append((i, num - i))
    
    return combinaciones            


# ----------------------------------------------------------
# VALIDACIÓN DE ENTRADA
# ----------------------------------------------------------
while True:
    try:
        # Pedimos el número al usuario
        num = int(input("Ingrese un número par positivo mayor a 2: "))
        
        # Verificamos que:
        # 1. Sea mayor a 2
        # 2. Sea par (num % 2 == 0)
        if num > 2 and num % 2 == 0:
            break
        else:
            print("Error: Debe ser un número PAR, mayor a 2.")
    
    except ValueError:
        # Si el usuario escribe letras o símbolos
        print("Error: Debe ingresar un número entero válido.")


# Llamamos a la función goldbach para obtener las combinaciones
resultado = goldbach(num)


# ----------------------------------------------------------
# MOSTRAR RESULTADOS
# ----------------------------------------------------------
if resultado:

    print(f"Formas de escribir {num} como suma de dos primos:")

    # Desempaquetamos cada tupla en a y b
    for a, b in resultado:

        print(f"{a} + {b}")

else:
    print(f"No se encontraron combinaciones para {num}")
