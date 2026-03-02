# Se solicita al usuario que ingrese un número entero
# Este número determinará la cantidad de filas del árbol
n = int(input())

# Se imprime un mensaje indicando cuántas filas tendrá el árbol
print(f"Arbol de {n} filas:")

# Se utiliza un ciclo for para generar cada fila del árbol
# 'i' representa la fila actual, empezando desde 1 hasta n inclusive
for i in range(1, n + 1):

    # Se calcula la cantidad de espacios en blanco antes de los asteriscos
    # Esto centra los asteriscos en la fila
    espacios = n - i

    # Se calcula la cantidad de asteriscos en la fila
    # La fórmula 2*i - 1 asegura que el número de asteriscos sea impar y crezca de 1 en 1
    asteriscos = 2 * i - 1

    # Se imprime la fila combinando los espacios y los asteriscos
    # Se multiplica el carácter por la cantidad correspondiente
    print((" " * espacios) + ("*" * asteriscos))