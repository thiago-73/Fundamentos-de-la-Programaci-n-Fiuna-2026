# Se importa la librería random
# Una librería es un conjunto de herramientas o funciones ya creadas
# que Python nos ofrece para realizar ciertas tareas.
# En este caso, random permite generar números aleatorios
# (números que cambian cada vez que se ejecuta el programa).
import random

# Bucle infinito para pedir al usuario un número hasta que sea válido
while True:
    try:
        # Se solicita al usuario la cantidad de dados que se lanzarán
        # int() convierte el valor ingresado (texto) en un número entero
        n = int(input("Ingrese un número de dados: "))
        
        # Verifica que el número sea mayor a 0
        if n > 0:
            # Si el valor es válido se sale del bucle
            break
        else:
            # Si el número es 0 o negativo se muestra un mensaje de error
            print("El número debe ser positivo.")
    # Si el usuario ingresa algo que no puede convertirse a entero
    except ValueError:
        print("El número debe ser entero.")

# Listas donde se guardarán los valores de los dados de cada jugador
dados1 = []
dados2 = []

# Se generan n dados aleatorios para el jugador 1
# "_" se usa cuando no necesitamos usar la variable del ciclo
for _ in range(n):

    # random.randrange(1, 7, 1) genera un número aleatorio
    # entre 1 y 6 (el 7 no se incluye).
    # Esto simula el lanzamiento de un dado.
    #
    # Explicación de los parámetros:
    # 1 → valor inicial
    # 7 → valor final (no incluido)
    # 1 → paso entre números posibles
    dados1.append(random.randrange(1, 7, 1))

# Se generan n dados aleatorios para el jugador 2
for _ in range(n):
    # Cada resultado del dado se agrega a la lista dados2
    dados2.append(random.randrange(1, 7, 1))
    
# Se calcula la suma del valor máximo y el mínimo de los dados del jugador 1
suma1 = max(dados1) + min(dados1)

# Se calcula la suma del valor máximo y el mínimo de los dados del jugador 2
suma2 = max(dados2) + min(dados2)

# Se muestran los resultados del juego
print(f"\nResultados:")

# Se imprime la lista de dados del jugador 1, su valor máximo, mínimo y la suma
print(f"Jugador 1: {dados1} → Máx: {max(dados1)} + Mín: {min(dados1)} = {suma1}")

# Se imprime la lista de dados del jugador 2, su valor máximo, mínimo y la suma
print(f"Jugador 2: {dados2} → Máx: {max(dados2)} + Mín: {min(dados2)} = {suma2}")
print()

# Se comparan las sumas para determinar el ganador
if suma1 > suma2:
    # Si la suma del jugador 1 es mayor, gana el jugador 1
    print("Jugador 1 gana.")
elif suma2 > suma1:
    # Si la suma del jugador 2 es mayor, gana el jugador 2
    print("Jugador 2 gana.")
else:
    # Si ambas sumas son iguales, hay empate
    print("Es un empate.")