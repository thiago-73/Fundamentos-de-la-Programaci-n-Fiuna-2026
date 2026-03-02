# Este programa determina si un ángulo ingresado por el usuario
# es un ángulo recto o no.
# Un ángulo recto mide exactamente 90 grados.

# Usamos un bloque try-except para manejar errores.
# Esto evita que el programa se rompa si el usuario escribe algo que no sea un número.
try:
    # input() permite al usuario ingresar un valor desde el teclado.
    # Siempre devuelve texto (string).
    # float() convierte ese texto en un número decimal.
    angulo = float(input("Ingrese el valor del ángulo en grados: "))

    # Verificamos si el ángulo es exactamente igual a 90.
    # El operador == se usa para comparar si dos valores son iguales.
    if angulo == 90:
        # Si la condición es verdadera (True),
        # significa que el ángulo es exactamente 90 grados.
        print("El ángulo es recto.")
    else:
        # Si la condición es falsa (False),
        # significa que el ángulo no es 90 grados.
        print("El ángulo no es recto.")

# Si el usuario ingresa algo que no puede convertirse a número,
# se ejecutará este bloque.
except ValueError:
    print("Error: Debe ingresar un número válido.")