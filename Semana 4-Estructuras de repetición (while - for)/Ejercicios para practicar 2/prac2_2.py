# Se importa la librería random
# Esta librería permite generar números aleatorios.
# Los números aleatorios son números que cambian cada vez que se ejecuta el programa.
# En este ejercicio se usan para simular el lanzamiento de dados.
import random

# Pedir número de dados
# Se utiliza un bucle infinito para solicitar un valor válido
while True:
    try:
        # Se solicita al usuario la cantidad de dados que se lanzarán
        # int() convierte el valor ingresado (texto) en un número entero
        n = int(input("Ingrese un número de dados: "))
        
        # Se verifica que el número sea positivo
        if n > 0:
            # Si el valor es correcto se sale del bucle
            break
        else:
            # Si el número es 0 o negativo se muestra un mensaje de error
            print("El número debe ser positivo.")
            
    # Si el usuario ingresa algo que no puede convertirse a entero
    # Python genera un ValueError y se captura aquí
    except ValueError:
        print("El número debe ser entero.")

# Generar dados
# Se crea una lista vacía donde se guardarán los resultados de los dados
dados = []

# Se repite el proceso n veces para simular el lanzamiento de n dados
for _ in range(n):
    
    # random.randrange(1, 7, 1) genera un número aleatorio
    # entre 1 y 6 (el 7 no se incluye).
    # Esto representa los posibles valores de un dado.
    #
    # Parámetros:
    # 1 → número inicial
    # 7 → número final (no incluido)
    # 1 → paso entre números posibles
    dados.append(random.randrange(1, 7, 1))

# Se imprime la lista con los valores obtenidos en los dados
print(f"Dados: {dados}")

# Verificar si hay dados consecutivos iguales
# Se crea una variable que indicará si se encontró o no una coincidencia
hay_consecutivos = False

# Variable que se usará como índice para recorrer la lista
i = 0

# Se recorre la lista comparando cada dado con el siguiente
# n - 1 es importante para evitar acceder a una posición que no existe
while i < n - 1:  # Importante: n-1 para no salir del rango
    
    # Se compara el dado actual con el siguiente
    if dados[i] == dados[i + 1]:
        
        # Si son iguales significa que hay dados consecutivos iguales
        hay_consecutivos = True
        
        # Se termina el ciclo porque ya encontramos lo que buscábamos
        break
        
    # Se avanza al siguiente índice
    i += 1

# Se evalúa el resultado final
if hay_consecutivos:
    
    # Si se encontró al menos un par de dados consecutivos iguales
    print(f"¡El jugador ganó! Hay dados consecutivos iguales.")
    
else:
    
    # Si no se encontró ningún par consecutivo igual
    print("El jugador perdió. No hay dados consecutivos iguales.")