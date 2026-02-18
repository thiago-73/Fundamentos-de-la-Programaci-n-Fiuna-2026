# 2. Leer un número y verificar si es flotante o entero.
# Considerar un numero como entero a partir de una tolerancia T.
#
# Este programa determina si un número es entero o flotante
# dependiendo de qué tan cerca esté de un número entero.
# La tolerancia T define el margen permitido.

print("Verificación de flotante o entero(Apartir de tolerancia).")

# Usamos while True para asegurarnos de que el usuario ingrese
# un número válido. Si ingresa letras u otro valor inválido,
# el programa volverá a pedir el número.
while True:
    try:
        # float() convierte el valor ingresado en número decimal
        # Ejemplo: 5 → 5.0, 3.14 → 3.14
        N = float(input("Ingrese número: "))
        break  # Salimos del bucle si no hay error
    except ValueError:
        # Este error ocurre si el usuario ingresa texto
        # que no puede convertirse a número
        print("Error: Debe ingresar un número válido.")

# Pedimos la tolerancia, que también es un número decimal
# La tolerancia es el margen que permite considerar
# un número como entero.
while True:
    try:
        T = float(input("Ingrese tolerancia: ")) 
        break
    except ValueError:
        print("Error: Debe ingresar un número válido.")

# Convertimos el número N a entero
# int() elimina la parte decimal (NO redondea, solo corta)
# Ejemplo:
# int(5.9) = 5
# int(3.2) = 3
E = int(N)

# Calculamos la diferencia entre el número original
# y su parte entera
# Esto nos da la parte decimal
# Ejemplo:
# N = 5.3
# E = 5
# X = 0.3
X =  N - E

# Aquí comparamos la parte decimal con la tolerancia
# Si la parte decimal es mayor que la tolerancia,
# entonces es flotante
if X > T:

    print(N, "es un número flotante.")
else:
    # Si la parte decimal es menor o igual a la tolerancia,
    # lo consideramos entero
    print(N, "es un número entero.")
