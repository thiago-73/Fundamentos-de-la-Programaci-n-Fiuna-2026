# Este programa pide dos números enteros al usuario
# Luego calcula la suma de ambos números
# Finalmente muestra el último dígito de la suma

# Usamos un bloque try/except para evitar que el programa se rompa
# si el usuario escribe algo que no sea un número entero
try:
    # input() lee lo que el usuario escribe
    # int() convierte ese texto en un número entero
    a = int(input("Ingrese el primer número entero: "))
    b = int(input("Ingrese el segundo número entero: "))

    # Calculamos la suma de los dos números
    suma = a + b

    # El operador % (módulo) devuelve el resto de una división
    # Al dividir entre 10, obtenemos el último dígito del número
    ultimo_digito = suma % 10

    # Mostramos el resultado en pantalla
    # print() permite mostrar texto y variables
    print("El último digito de", a, "+", b, "es:", ultimo_digito)

# Si el usuario escribe algo que no es un número entero,
# se ejecuta este bloque
except ValueError:
    print("Error: Debes ingresar solo números enteros.")
