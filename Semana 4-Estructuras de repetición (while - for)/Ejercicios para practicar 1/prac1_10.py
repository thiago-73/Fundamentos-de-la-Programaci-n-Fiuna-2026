# Se solicita al usuario que ingrese el numerador de la fracción
num = int(input("Ingrese el numerador: "))

# Se solicita al usuario que ingrese el denominador de la fracción
den = int(input("Ingrese el denominador: "))

# Se copian los valores del numerador y denominador
# en nuevas variables (a y b) para poder trabajar con ellas
# sin modificar los valores originales
a, b = num, den

# Se aplica el algoritmo de Euclides para encontrar
# el Máximo Común Divisor (MCD)
# El proceso continúa mientras b sea diferente de 0
while b != 0:

    # En cada iteración:
    # a toma el valor de b
    # b toma el valor del resto de la división entre a y b
    # Esto permite ir reduciendo el problema hasta encontrar el MCD
    a, b = b, a % b

# Cuando b llega a 0, el valor de a es el MCD
mcd = a

# Se simplifica el numerador dividiéndolo por el MCD
num_s = num // mcd

# Se simplifica el denominador dividiéndolo por el MCD
den_s = den // mcd

# Se imprime la fracción ya simplificada
print("Fracción simplificada:", num_s, "/", den_s)