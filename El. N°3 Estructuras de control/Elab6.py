# Elaborar un programa en que lea mediante el teclado los coeficientes de un polinomio de segundo grado ax² + bx + c y que luego determine las raíces de dicho polinomio (tener en cuenta todos los valores posibles de a, b y c, incluso si las raíces son imaginarias).

a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))

if a == 0:
    if b == 0:
        if c == 0:
             print("La ecuación tiene infinitas soluciones.")
        else:
            print("La ecuación no tiene solución.")
    else:
        x = -c / b
        
        print("Es una ecuación lineal.")
        print("La solución es:", x)      
else:
    discriminate = (b ** 2) - (4 * a *c)
    
    if discriminate > 0:
        x1 = (-b + discriminate ** 0.5) / (2 * a)
        x2 = (-b - discriminate ** 0.5) / (2 * a)
         
        print("Dos raíces reales distintas:")
        print("x1 =", x1)
        print("x2 =", x2)
    else:
        if discriminate == 0:
            x = -b / (2*a)
            print("Una raíz real doble:")
            print("x =", x)

        else:
            parte_real = -b / (2 * a)
            parte_imaginaria = ((-discriminate) ** 0.5) / (2 * a)

            print("Dos raíces complejas:")
            print("x1 =", parte_real, "+", parte_imaginaria, "i")
            print("x2 =", parte_real, "-", parte_imaginaria, "i")