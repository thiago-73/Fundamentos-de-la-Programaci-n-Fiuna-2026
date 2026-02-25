# Programa que lee e imprime una serie de números distintos de cero
# La serie termina cuando el usuario ingresa 0 (cero)
# Se visualiza la cantidad de números leídos (sin contar el cero)

print("Leer series de números (ingrese 0 para finalizar).")

# Contador de números válidos leídos
c = 0

# Bucle infinito que se rompe al ingresar 0
while True:
    try:
        n = int(input("Ingrese un número (distinto de 0): "))
    except ValueError:
        print("Error: Debe ingresar un número entero válido.")
        continue  # vuelve a pedir el número

    if n == 0:
        # El cero termina la serie y no se cuenta
        print("El número 0 termina la serie, no se imprimirá.")
        break

    # Imprimimos el número ingresado
    print(n)

    # Incrementamos el contador solo si el número no es cero
    c += 1

# Mostramos la cantidad de números leídos
print(f"El número de valores leídos es {c}")
