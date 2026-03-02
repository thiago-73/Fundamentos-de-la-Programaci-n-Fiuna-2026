# Se solicita al usuario que ingrese un número entero
# Este número será el límite hasta el cual se generará la serie de Fibonacci
n = int(input())

# Se inicializan las dos primeras variables de la serie de Fibonacci
a, b = 0, 1

# Se crea una lista vacía para almacenar los números de la serie
fbo = []

# Se genera la serie de Fibonacci hasta que 'a' sea mayor que n
while a <= n:
    # Se agrega el número actual 'a' a la lista
    fbo.append(a)
    
    # Se actualizan los valores de 'a' y 'b' para el siguiente número de la serie
    # 'a' toma el valor de 'b' y 'b' toma el valor de 'a + b'
    a, b = b, a + b

# Se imprime la lista de Fibonacci como una cadena separada por comas
# map(str, fbo) convierte cada número a texto para poder usar join
print(",".join(map(str, fbo)))