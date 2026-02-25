# Este programa lee dos números enteros desde el teclado.
# Luego calcula su suma.
# Finalmente obtiene el último dígito de esa suma
# y lo muestra en pantalla.

# input() permite al usuario escribir un valor.
# int() convierte ese valor (que es texto) en número entero.
a = int(input())
b = int(input())

# Aquí sumamos los dos números ingresados.
suma = a + b

# El operador % (módulo) devuelve el resto de la división.
# Al hacer % 10 obtenemos el último dígito del número.
ultimo_digito = suma % 10

# print() muestra el resultado en pantalla.
# Se imprime un mensaje junto con los valores de a, b
# y el último dígito calculado.
print("El primer digito de", a, "+", b, "es:", ultimo_digito)
