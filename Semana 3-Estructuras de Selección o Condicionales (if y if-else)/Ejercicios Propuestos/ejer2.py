# Dados los valores a, b y c; indicar si pueden ser los lados de un triángulo.

# Para que tres números puedan formar un triángulo,
# deben cumplir la "condición de existencia del triángulo":
# La suma de dos lados siempre debe ser mayor que el tercero.
# Es decir:
# a + b > c
# a + c > b
# b + c > a

# Usamos try-except para evitar que el programa se rompa
# si el usuario ingresa algo que no sea un número.
try:
    # Pedimos al usuario que ingrese los tres lados.
    # float() convierte el texto ingresado en número decimal.
    a = float(input("Ingrese el valor del lado a: "))
    b = float(input("Ingrese el valor del lado b: "))
    c = float(input("Ingrese el valor del lado c: "))

    # Primero verificamos que los lados sean positivos.
    # Un lado no puede ser 0 ni negativo.
    if a > 0 and b > 0 and c > 0:

        # Aplicamos la condición de existencia del triángulo.
        if a + b > c and a + c > b and b + c > a:
            print("Sí pueden formar un triángulo.")
        else:
            print("No pueden formar un triángulo.")

    else:
        print("Error: Los lados deben ser mayores que 0.")

# Si el usuario escribe algo que no sea número,
# se captura el error y se muestra un mensaje.
except ValueError:
    print("Error: Debe ingresar valores numéricos válidos.")