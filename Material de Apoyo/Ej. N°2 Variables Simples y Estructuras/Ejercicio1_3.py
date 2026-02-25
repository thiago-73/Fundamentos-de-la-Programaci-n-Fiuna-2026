# Programa que calcula el cociente y el resto de la división de dos números positivos

# ----------------------------------------------------------
# FUNCION PARA PEDIR NÚMEROS POSITIVOS
# ----------------------------------------------------------
def pedir_numero(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor > 0:
                return valor
            else:
                print("Error: El número debe ser mayor que 0.")
        except ValueError:
            print("Error: Debe ingresar un número válido.")

# Pedimos dividendo y divisor
dividendo = pedir_numero("Ingrese dividendo: ")

# Para el divisor, además verificamos que no sea cero
while True:
    divisor = pedir_numero("Ingrese divisor: ")
    if divisor != 0:
        break
    else:
        print("Error: El divisor no puede ser cero.")

# ----------------------------------------------------------
# CALCULO DEL COCIENTE Y RESTO
# ----------------------------------------------------------
cociente = dividendo / divisor
resto = dividendo % divisor

# ----------------------------------------------------------
# MOSTRAR RESULTADO
# ----------------------------------------------------------
print(f"El cociente entre {dividendo} y {divisor} es {cociente} y el resto {resto}")
