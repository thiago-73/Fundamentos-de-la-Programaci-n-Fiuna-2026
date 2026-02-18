# 4. Ingresar por teclado un numero entero mayor que 1000, validarlo,
# determinar e imprimir el menor de sus dígitos primos y la suma de sus dígitos.
#
# Este programa hace tres cosas:
# 1. Calcula la suma de todos los dígitos del número.
# 2. Encuentra el menor dígito primo dentro del número.
# 3. Muestra los resultados.

# ----------------------------------------------------------
# FUNCIÓN PARA VERIFICAR SI UN NÚMERO ES PRIMO
# ----------------------------------------------------------
def es_primo(num):   

    # Los números menores que 2 no son primos
    if num < 2:
        return False
 
    # Verificamos divisores desde 2 hasta la raíz cuadrada del número
    # Esto hace el algoritmo más eficiente
    for i in range(2, int((num ** 0.5)) + 1):

        # Si es divisible exactamente, no es primo
        if num % i == 0:
            return False
            
    # Si no encontramos divisores, es primo
    return True


# ----------------------------------------------------------
# FUNCIÓN PARA CALCULAR LA SUMA DE LOS DÍGITOS
# ----------------------------------------------------------
def sum_digitos(num):

    # Variable donde acumularemos la suma
    suma = 0

    # Recorremos cada dígito usando operaciones matemáticas
    while num > 0:

        # num % 10 obtiene el último dígito
        # Ejemplo: 123 % 10 = 3
        suma += (num % 10)

        # Eliminamos el último dígito
        # Ejemplo: 123 // 10 = 12
        num //= 10
        
    return suma


# ----------------------------------------------------------
# FUNCIÓN PARA ENCONTRAR EL MENOR DÍGITO PRIMO
# ----------------------------------------------------------
def digitos(num):

    # Inicializamos menor como None
    # None significa "no hay valor todavía"
    menor = None
    
    # Recorremos todos los dígitos
    while num > 0:

        # Obtenemos el último dígito
        digito = num % 10
        
        # Verificamos si el dígito es primo
        if es_primo(digito):

            # Si es el primer primo encontrado
            # o si es menor que el actual menor
            if menor is None or digito < menor:

                # Actualizamos el menor
                menor = digito

        else:
            # Si no es primo, eliminamos el dígito
            num //= 10
            
    return menor


# ----------------------------------------------------------
# VALIDACIÓN DE ENTRADA
# ----------------------------------------------------------
while True:
    try:
        # Pedimos el número al usuario
        n = int(input("Ingrese un número entero mayor que 1000: "))
        
        # Verificamos que sea mayor que 1000
        if n > 1000:
            break
        else:
            print("Error: El número debe ser mayor que 1000.")
    
    except ValueError:
        # Si el usuario ingresa letras o símbolos
        print("Error: Debe ingresar un número entero válido.")


# Calculamos la suma de los dígitos
suma = sum_digitos(n)

# Buscamos el menor dígito primo
menor = digitos(n)


# Mostramos la suma
print("Suma de los dígitos:", suma)


# Mostramos el menor dígito primo si existe
if menor is not None:

    print("Menor dígito primo:", menor)

else:

    print("No tiene dígitos primos")
