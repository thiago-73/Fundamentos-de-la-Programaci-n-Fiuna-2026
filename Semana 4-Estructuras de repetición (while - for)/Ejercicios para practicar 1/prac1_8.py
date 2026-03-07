# Bucle infinito para solicitar datos hasta que sean válidos
while True:
    try:
        # Se solicita al usuario el primer año
        # int() convierte el valor ingresado a un número entero
        n = int(input("Ingrese 1er año: "))

        # Se solicita el segundo año
        p = int(input("Ingrese 2do año: "))
        
        # Se valida que:
        # 1. Ambos años sean positivos
        # 2. El segundo año sea mayor o igual al primero
        if n > 0 and p > 0 and p >= n:
            # Si los valores son válidos se sale del bucle
            break
        else:
            # Si los valores no cumplen las condiciones se muestra un error
            print("Error: Ingrese años positivos y que el segundo sea mayor o igual al primero.")
            
    # Si el usuario ingresa algo que no es un número entero
    # Python genera un ValueError y se captura aquí
    except ValueError:
        print("Error: Debe ser un número entero.")

# Se crea una lista vacía donde se guardarán los años bisiestos encontrados
bisiestos = []

# Se recorre todos los años desde n hasta p
# p + 1 se usa porque range no incluye el último número
for i in range(n, p + 1):

    # Condición para determinar si un año es bisiesto
    # Un año es bisiesto si:
    # - Es divisible por 4 y no por 100
    # - O es divisible por 400
    if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0):

        # Si el año cumple la condición, se agrega a la lista
        bisiestos.append(i)

# Se imprime la lista de años bisiestos encontrados en el rango indicado
print(f"Los años bisiestos entre {n} y {p} son:", bisiestos)