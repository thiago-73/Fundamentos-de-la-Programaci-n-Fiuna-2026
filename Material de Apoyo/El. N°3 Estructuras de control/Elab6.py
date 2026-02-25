# Elaborar un programa en que lea mediante el teclado los coeficientes
# de un polinomio de segundo grado ax² + bx + c y que luego determine
# las raíces de dicho polinomio (tener en cuenta todos los valores posibles
# de a, b y c, incluso si las raíces son imaginarias).

# ----------------------------------------------------------
# VALIDACIÓN DE ENTRADA
# ----------------------------------------------------------

# Pedimos el valor de a
while True:
    try:
        # float() permite ingresar números decimales
        a = float(input("Ingrese el valor de a: "))
        break
    except ValueError:
        print("Error: Debe ingresar un número válido.")

# Pedimos el valor de b
while True:
    try:
        b = float(input("Ingrese el valor de b: "))
        break
    except ValueError:
        print("Error: Debe ingresar un número válido.")

# Pedimos el valor de c
while True:
    try:
        c = float(input("Ingrese el valor de c: "))
        break
    except ValueError:
        print("Error: Debe ingresar un número válido.")


# ----------------------------------------------------------
# ANÁLISIS DE LA ECUACIÓN
# ----------------------------------------------------------
# La ecuación general es:
# ax² + bx + c = 0

# Caso 1: Si a == 0, deja de ser ecuación cuadrática
if a == 0:

    # Entonces sería: bx + c = 0
    if b == 0:

        # Entonces sería: c = 0
        if c == 0:

             # 0 = 0 → se cumple siempre
             print("La ecuación tiene infinitas soluciones.")
        else:

            # Número distinto de 0 = 0 → imposible
            print("La ecuación no tiene solución.")
    else:

        # Ecuación lineal: bx + c = 0
        # Despejando:
        # x = -c / b
        x = -c / b
        
        print("Es una ecuación lineal.")
        print("La solución es:", x)      


# Caso 2: Si a ≠ 0, es ecuación cuadrática
else:

    # Calculamos el discriminante:
    # Δ = b² - 4ac
    discriminate = (b ** 2) - (4 * a * c)
    
    # Si el discriminante es positivo
    if discriminate > 0:

        # Dos raíces reales distintas
        x1 = (-b + discriminate ** 0.5) / (2 * a)
        x2 = (-b - discriminate ** 0.5) / (2 * a)
         
        print("Dos raíces reales distintas:")
        print("x1 =", x1)
        print("x2 =", x2)

    else:

        # Si el discriminante es exactamente 0
        if discriminate == 0:

            # Existe una única raíz real (raíz doble)
            x = -b / (2 * a)

            print("Una raíz real doble:")
            print("x =", x)

        else:

            # Si el discriminante es negativo
            # Las raíces son complejas (imaginarias)

            # Parte real:
            parte_real = -b / (2 * a)

            # Parte imaginaria:
            # √(-Δ) / 2a
            parte_imaginaria = ((-discriminate) ** 0.5) / (2 * a)

            print("Dos raíces complejas:")
            print("x1 =", parte_real, "+", parte_imaginaria, "i")
            print("x2 =", parte_real, "-", parte_imaginaria, "i")
