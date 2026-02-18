# Programa que imprime y suma la serie de números: 3, 6, 9, 12, ..., 99
# La serie es una progresión aritmética con diferencia común de 3

# Inicializamos variable k (opcional, sirve como referencia)
k = 3

# Inicializamos la suma
s = 0

# ----------------------------------------------------------
# BUCLE PARA RECORRER LA SERIE
# ----------------------------------------------------------
# range(inicio, fin, paso)
# inicio = 3 → primer número de la serie
# fin = 100 → no incluye 100, por eso llega hasta 99
# paso = 3 → se incrementa de 3 en 3
for i in range(3, 100, 3):
    print(i)    # Imprimimos cada número
    s += i      # Acumulamos la suma

# ----------------------------------------------------------
# MOSTRAR RESULTADO FINAL
# ----------------------------------------------------------
print("La suma es:", s)
