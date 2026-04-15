# Se lee un número entero que indica cuántos números se van a ingresar
num = int(input())

# Se crea una lista vacía donde se guardarán los números ingresados
numeros = []

# Bucle que se repite "num" veces para leer los números
for i in range(num):
    # Se lee un número entero desde el usuario
    n = int(input())
    
    # Se agrega el número ingresado a la lista
    numeros.append(n)

# Se obtiene el número mayor de la lista usando la función max()
maximo = max(numeros)

# Se obtiene el número menor de la lista usando la función min()
minimo = min(numeros)

# Se imprime el valor máximo encontrado
print("El Mayor es ", maximo)

# Se imprime el valor mínimo encontrado
print("El menor es ", minimo)