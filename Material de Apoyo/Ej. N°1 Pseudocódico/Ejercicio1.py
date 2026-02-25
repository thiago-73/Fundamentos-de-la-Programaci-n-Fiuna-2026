# 1. Escribir un pseudocodigo que sume dos números enteros
# Este programa solicita al usuario dos números enteros
# y luego muestra la suma de ambos.

print("Suma de 2 numeros enteros.")

# Usamos un bucle while True para asegurarnos de que el usuario
# ingrese un número válido. Si se equivoca, el programa volverá
# a pedir el número hasta que lo haga correctamente.
while True:
    try:
        # input() siempre devuelve texto (string)
        # int() convierte ese texto a número entero
        a = int(input("Ingrese primer número: "))
        break  # Si no hay error, salimos del bucle
    except ValueError:
        # Este error ocurre si el usuario escribe algo
        # que no se puede convertir a entero (por ejemplo letras)
        print("Error: Debe ingresar un número entero válido.")

while True:
    try:
        b = int(input("Ingrese segundo número: "))
        break
    except ValueError:
        print("Error: Debe ingresar un número entero válido.")

# Aquí realizamos la suma
# El operador + sirve para sumar números
s = a + b

# Mostramos el resultado final
# La coma en print permite mostrar texto y variables juntas
print("La suma es: ", s)
