# Se solicita al usuario que ingrese tres números enteros.
# Cada número se almacena en una variable distinta: a, b y c.
a = int(input())
b = int(input())
c = int(input())

# Se determina cuál de los tres números es el valor central (el que no es ni el mayor ni el menor).

# Se verifica si 'a' está entre 'b' y 'c'.
# La condición (a > b and a < c) verifica si 'a' está entre b y c de forma ascendente.
# La condición (a > c and a < b) verifica si 'a' está entre b y c de forma descendente.
if (a > b and a < c) or (a > c and a < b):
    central = a

# Se verifica si 'b' está entre 'a' y 'c' de manera similar.
elif (b > a and b < c) or (b > c and b < a):
    central = b

# Si ninguna de las condiciones anteriores se cumple, significa que 'c' es el número central.
else:
    central = c

# Se imprime el número central en pantalla.
print(central)