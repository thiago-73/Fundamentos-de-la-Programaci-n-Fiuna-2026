# Se inicializa la variable n en 0
# Esta variable servirá como contador dentro del ciclo
n = 0

# Variable que almacenará la suma de los términos
suma = 0

# Variable que almacenará la multiplicación (producto) de los términos
# Se inicia en 1 porque es el elemento neutro de la multiplicación
mul = 1

# Se ejecuta el ciclo mientras n sea menor o igual a 8
while n <= 8:

    # Se calcula el término de la suma usando la fórmula (4 + 3n)
    # y se acumula en la variable suma
    suma += 4 + (3 * n)

    # Se calcula el término del producto usando la fórmula (6 + 3n)
    # y se multiplica al acumulador mul
    mul *= 6 + (3 * n)
    
    # Se incrementa el contador n para pasar al siguiente término
    n += 1

# Se calcula el resultado final dividiendo la suma entre el producto
resultado = suma / mul

# Se imprime el resultado obtenido
print("El resultado es: ", resultado)