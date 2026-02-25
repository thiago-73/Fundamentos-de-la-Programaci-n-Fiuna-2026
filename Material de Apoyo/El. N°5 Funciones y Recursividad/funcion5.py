# Programa que determina e imprime los 50 números capicúas consecutivos mayores que 1000
# Un número capicúa es aquel que se lee igual de derecha a izquierda y de izquierda a derecha
# Ejemplo: 1221, 23532

# ----------------------------------------------------------
# LISTA PARA GUARDAR LOS NÚMEROS CAPICÚAS
# ----------------------------------------------------------
capicuas = []

# Comenzamos desde el primer número mayor a 1000
n = 1000

# ----------------------------------------------------------
# GENERAR CAPICÚAS HASTA TENER 50
# ----------------------------------------------------------
while len(capicuas) < 50:
    # Convertimos el número a cadena y lo invertimos, luego comparamos
    if n == int(str(n)[::-1]):
        capicuas.append(n)  # Si es capicúa, lo agregamos a la lista
    
    n += 1  # Incrementamos para revisar el siguiente número

# ----------------------------------------------------------
# IMPRIMIR LOS NÚMEROS CAPICÚAS
# ----------------------------------------------------------
print("Los 50 números capicúas consecutivos mayores que 1000 son:")
for capicua in capicuas:
    print(capicua)
