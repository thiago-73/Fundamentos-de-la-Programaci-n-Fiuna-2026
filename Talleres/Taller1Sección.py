# Se lee un número entero ingresado por el usuario
A = int(input())

# Paso 1
# Se verifica si el número cumple alguna de estas condiciones:
# - Es menor que 0
# - Es mayor que 55555
# - Es divisible entre 3
# Si se cumple alguna, el programa imprime "NA"
if A < 0 or A > 55555 or A % 3 == 0:
    print("NA")
else:

    # Se convierte el número A en texto para poder recorrer cada dígito
    # Luego cada dígito se convierte nuevamente a entero
    # Ejemplo: A = 123 → [1, 2, 3]
    digitos = [int(d) for d in str(A)]

    # Si el número tiene menos de 5 dígitos,
    # se agregan ceros al inicio hasta que tenga exactamente 5
    # Ejemplo: 123 → 00123
    while len(digitos) < 5:
        digitos.insert(0,0)

    # Lista donde se guardarán los nuevos valores transformados
    B = []

    # Se recorren los dígitos originales
    for a in digitos:
        # Si el dígito es menor que 9 se le suma 1
        if a < 9:
            B.append(a + 1)
        else:
            # Si el dígito es 9, se convierte en 0
            B.append(0)

    # Se ordena la lista B de menor a mayor
    C = sorted(B)

    # Se guardan los cinco valores ordenados en variables separadas
    c1, c2, c3, c4, c5 = C

    # Se calcula c6 usando el residuo (módulo)
    # Si c1 es 0 se evita la división entre 0
    if c1 == 0:
        c6 = 0
    else:
        c6 = c5 % c1

    # Se calcula c7 de forma similar
    # Si c2 es 0 también se evita división entre 0
    if c2 == 0:
        c7 = 0
    else:
        c7 = c4 % c2

    # Se crea una nueva lista agregando c6 y c7 al final
    C_prima = C + [c6, c7]

    # Se imprimen todos los dígitos sin saltos de línea
    # end="" evita que se agregue un salto después de cada número
    for d in C_prima:
        print(d, end="")