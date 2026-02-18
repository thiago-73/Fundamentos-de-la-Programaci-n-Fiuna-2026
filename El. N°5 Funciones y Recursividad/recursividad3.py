# 3. Calcule el producto de dos números utilizando funciones recursivas.

# Definimos la función recursiva "producto" que recibe dos números a y b
def producto(a, b):
    # Caso base: si b es 0, el producto siempre es 0
    if b == 0:
        return 0
    
    # Si b es negativo, invertimos el signo y llamamos recursivamente con -b
    if b < 0:
        return -producto(a, -b)
    
    # Caso general: sumamos 'a' al resultado de producto(a, b-1)
    # Esto es equivalente a hacer a + a + ... + a (b veces)
    return a + producto(a, b - 1)

# Ciclo para asegurar que el usuario ingrese números válidos
while True:
    try:
        # Se solicita el primer número
        a = int(input("Ingrese primer número: "))
        # Se solicita el segundo número
        b = int(input("Ingrese segundo número: "))
        break  # Si ambos son enteros, salimos del ciclo
    except ValueError:
        # Si el usuario ingresa algo que no es un entero, mostramos un mensaje y repetimos
        print("Ingrese un valor válido.")

# Calculamos el producto usando la función recursiva
resultado = producto(a, b)

# Mostramos el resultado al usuario
print(f"El producto entre {a} y {b} es: {resultado}")
