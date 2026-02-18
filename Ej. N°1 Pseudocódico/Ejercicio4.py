# 4. Leer dos números enteros x y n. Escribir un pseudocodigo que eleve n a la potencia x.
#
# Este programa calcula una potencia.
# Una potencia significa multiplicar un número por sí mismo varias veces.
#
# Ejemplo:
# 2^3 = 2 * 2 * 2 = 8

print("Elevar potencia.")

# Pedimos la base (n)
# Usamos validación para asegurarnos de que el usuario ingrese un número entero válido
while True:
    try:
        # int() convierte el valor ingresado a número entero
        n = int(input("Ingrese base: "))
        break  # Si no hay error, salimos del bucle
    except ValueError:
        # Este error ocurre si el usuario ingresa letras o símbolos
        print("Error: Debe ingresar un número entero válido.")

# Pedimos el exponente o potencia (x)
while True:
    try:
        x = int(input("Ingrese potencia: "))
        break
    except ValueError:
        print("Error: Debe ingresar un número entero válido.")

# El operador ** es el operador de potencia en Python
#
# Ejemplos:
# 2 ** 3 = 8
# 5 ** 2 = 25
# 10 ** 0 = 1
#
# Significa:
# base elevado a exponente
p = n ** x

# Mostramos el resultado usando f-string
# f-string permite insertar variables dentro del texto usando {}
print(f"{n} elevado a {x} es igual a {p}")
