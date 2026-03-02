# Se solicita al usuario que ingrese un número.
# Se convierte a float para permitir números con decimales.
n = float(input())

# Se verifica si el número NO es entero (tiene decimales) y es positivo.
# int(n) convierte n a entero truncando los decimales, por eso n != int(n) indica que tiene parte decimal.
if n != int(n) and n > 0:
    print("Error, el numero ingresado no es entero")

# Se verifica si el número es negativo pero entero.
elif n < 0 and n == int(n):
    print("Error, el numero ingresado no es positivo")

# Se verifica si el número es negativo y además no es entero (tiene decimales).
elif n < 0 and n != int(n):
    print("Error, el numero ingresado no es entero ni positivo")

# Se verifica si el número es mayor a 10000, en cuyo caso se considera demasiado grande.
elif n > 10000:
    print("Error, el numero ingresado es muy grande")

# Si ninguna de las condiciones anteriores se cumple, el número es válido.
else:
    # Se convierte a entero para eliminar posibles decimales y se calcula su cuadrado.
    cuadrado = int(n) ** 2
    
    # Se imprime el cuadrado del número ingresado.
    print(cuadrado)