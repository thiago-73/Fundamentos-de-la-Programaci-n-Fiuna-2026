# Se lee un número entero que indica cuántos valores se van a ingresar
num = int(input())

# Se crea una lista vacía donde se guardarán los números positivos
numeros = []

# Bucle que se repite "num" veces para leer los números
for i in range(num):
    # Se lee un número entero
    n = int(input())
    
    # Solo se agregan los números mayores a 0
    if n > 0:
        numeros.append(n)

# Se calcula la suma de todos los números guardados en la lista
suma = sum(numeros)

# Se verifica que la lista no esté vacía para evitar errores
if len(numeros) > 0:
    # Se calcula el promedio:
    # primero se divide suma / cantidad de elementos
    # luego se multiplica por 100 y se convierte a entero para truncar decimales
    # finalmente se divide entre 100 para dejar solo 2 decimales aproximados
    promedio = int((suma / len(numeros)) * 100) / 100
    
    # Se imprime la suma total
    print("La suma es", suma)
    
    # Se imprime el promedio con formato de 2 decimales
    print("El promedio es {:.2f}".format(promedio))