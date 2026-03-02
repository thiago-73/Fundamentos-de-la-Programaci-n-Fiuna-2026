# Se solicita al usuario que ingrese un número.
# El valor ingresado se convierte a tipo float para permitir números decimales.
n = float(input())

# Se verifica si el número ingresado es mayor que 0.
# Si se cumple esta condición, significa que el número es positivo.
if n > 0:
    print("El numero ingresado es positivo")

# Si la condición anterior no se cumple, se evalúa esta segunda condición.
# Aquí se verifica si el número es menor que 0, lo que indica que es negativo.
elif n < 0:
    print("El numero ingresado es negativo")

# Si ninguna de las condiciones anteriores se cumple,
# entonces el número necesariamente es igual a 0.
else:
    print("El numero ingresado es cero")

