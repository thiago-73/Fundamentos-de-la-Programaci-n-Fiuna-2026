# Se lee un número entero que indica cuántos elementos tendrá la lista
num = int(input())

# Se crea una lista vacía donde se guardarán los números ingresados
numeros = []

# Bucle para leer "num" cantidades de números
for i in range(num):
    # Se lee un número entero
    n = int(input())
    
    # Se agrega el número a la lista
    numeros.append(n)

# Se elimina el último elemento de la lista y se guarda en la variable "ultimo"
ultimo = numeros.pop(-1)

# Se inserta el último elemento al inicio de la lista (posición 0)
numeros.insert(0, ultimo)

# Se recorre la lista ya modificada
for i in numeros:
    # Se imprime cada elemento de la lista en una nueva línea
    print(i)