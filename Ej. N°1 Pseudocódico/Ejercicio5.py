# Programa que calcula el factorial de un número entero no negativo
# El factorial de n (n!) es: n! = n * (n-1) * ... * 2 * 1
# Por definición, 0! = 1

print("Cálculo de factorial.")

# ----------------------------------------------------------
# VALIDACIÓN DE ENTRADA
# ----------------------------------------------------------
while True:
    try:
        n = int(input("Ingrese un número entero no negativo: "))
        
        # El factorial solo está definido para números enteros >= 0
        if n >= 0:
            break
        else:
            print("Error: El número debe ser mayor o igual a 0.")
    except ValueError:
        print("Error: Debe ingresar un número entero válido.")

# Guardamos el valor original para mostrarlo al final
k = n

# Inicializamos el factorial
f = 1

# ----------------------------------------------------------
# CALCULO DEL FACTORIAL
# ----------------------------------------------------------
while n > 1:
    f *= n   # Multiplicamos f por el valor actual de n
    n -= 1   # Decrementamos n para continuar la multiplicación

# ----------------------------------------------------------
# MOSTRAR RESULTADO
# ----------------------------------------------------------
print(f"{k}! es: {f}")
