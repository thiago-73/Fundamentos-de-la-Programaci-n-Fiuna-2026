# Se solicita al usuario que ingrese un número entero
n = int(input())

# Se determina el signo del número
# Si es negativo, signo = -1, de lo contrario signo = 1
if n < 0:
    signo = -1
else:
    signo = 1

# Se obtiene el valor absoluto del número para poder invertirlo sin preocuparse del signo
n_positivo = abs(n)

# Variable que almacenará el número invertido
invertifo = 0

# Ciclo para invertir los dígitos del número
while n_positivo > 0:
    # Se obtiene el último dígito del número usando módulo 10
    digito = n_positivo % 10

    # Se agrega el dígito al número invertido
    # Multiplicamos el invertifo por 10 para "desplazar" los dígitos anteriores
    invertifo = (invertifo * 10) + digito

    # Se elimina el último dígito del número original usando división entera
    n_positivo //= 10

# Se aplica nuevamente el signo al número invertido
invertifo *= signo

# Se imprime el número invertido
print(invertifo)