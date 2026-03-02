# Este programa verifica si tres números ingresados por el usuario
# pueden ser los lados de un triángulo rectángulo.

# Un triángulo rectángulo cumple el teorema de Pitágoras:
# El cuadrado del lado más largo es igual a la suma de los cuadrados de los otros dos lados.
# Es decir, si c es el lado más largo:
# c^2 = a^2 + b^2

# Usamos try-except para manejar errores si el usuario ingresa algo que no sea número.
try:
    # Pedimos al usuario los tres lados como enteros
    a = int(input("Ingrese el primer lado (entero positivo): "))
    b = int(input("Ingrese el segundo lado (entero positivo): "))
    c = int(input("Ingrese el tercer lado (entero positivo): "))

    # Verificamos que todos sean positivos
    if a > 0 and b > 0 and c > 0:

        # Primero comprobamos si pueden formar un triángulo
        if a + b > c and a + c > b and b + c > a:

            # Identificamos el lado más largo (hipotenusa)
            hipotenusa = max(a, b, c)
            if hipotenusa == a:
                lado1, lado2 = b, c
            elif hipotenusa == b:
                lado1, lado2 = a, c
            else:
                lado1, lado2 = a, b

            # Aplicamos el teorema de Pitágoras
            if hipotenusa ** 2 == lado1 ** 2 + lado2 ** 2:
                print("Estos números forman un triángulo rectángulo.")
            else:
                print("Estos números forman un triángulo, pero NO es rectángulo.")
        else:
            print("Estos números NO pueden formar un triángulo.")

    else:
        print("Error: Todos los lados deben ser enteros positivos.")

# Capturamos el error si el usuario no ingresa un número entero
except ValueError:
    print("Error: Debe ingresar números enteros válidos.")