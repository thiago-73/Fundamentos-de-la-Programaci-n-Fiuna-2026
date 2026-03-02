# Este programa calcula el monto final de una inversión
# usando la fórmula del interés compuesto.

# input() permite al usuario escribir un valor.
# float() convierte ese valor (texto) en un número decimal.

# P representa el capital inicial (Principal).
P = float(input())

# r representa la tasa de interés anual en porcentaje.
r = float(input())

# n representa la cantidad de años.
n = float(input())

# Fórmula del interés compuesto:
# A = P * (1 + r/100) elevado a la n
# ** es el operador de potencia en Python.
A = P * ((1 + (r / 100)) ** n)

# print() muestra el resultado en pantalla.
# int(n) se usa para mostrar los años sin decimales.
# str(A) convierte el número A en texto para poder unirlo con "$".
print("La cantidad final después de", int(n), "años es: $" + str(A))