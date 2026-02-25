# Programa que imprime la serie de Fibonacci hasta la posición N
# La serie de Fibonacci comienza así:
# 1, 1, 2, 3, 5, 8, 13, 21, ...

# ----------------------------------------------------------
# VALIDAR ENTRADA
# ----------------------------------------------------------
while True:
    try:
        N = int(input("Ingrese número entero positivo: "))
        
        if N > 0:
            break
        else:
            print("Ingrese un número mayor a 0.")
            
    except ValueError:
        print("Ingrese un valor válido.")

# ----------------------------------------------------------
# GENERAR LA SERIE DE FIBONACCI
# ----------------------------------------------------------
serie = []
a = 1
b = 1

for i in range(N):
    serie.append(a)     # Guardamos el número actual
    a, b = b, a + b    # Actualizamos valores (intercambio simultáneo)

# ----------------------------------------------------------
# IMPRIMIR LA SERIE
# ----------------------------------------------------------
print("Serie de Fibonacci:")
for i in serie:
    print(i)
