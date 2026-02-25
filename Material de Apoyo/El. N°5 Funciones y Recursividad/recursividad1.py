# Programa que simplifica una fracción NUM/DEM
# La fracción se simplifica dividiendo numerador y denominador
# por su máximo común divisor (MCD)

# ----------------------------------------------------------
# FUNCION PARA CALCULAR EL MCD
# ----------------------------------------------------------
def get_mcd(a, b):
    """
    Calcula el Máximo Común Divisor (MCD) de dos números usando el algoritmo de Euclides
    """
    while b != 0:
        a, b = b, a % b  # Intercambio: a toma valor de b, b toma valor del residuo
    return a

# ----------------------------------------------------------
# VALIDAR ENTRADA
# ----------------------------------------------------------
while True:
    try:
        NUM = int(input("Ingrese numerador (entero positivo): "))
        DEM = int(input("Ingrese denominador (entero positivo): "))
        
        if NUM > 0 and DEM > 0:
            break
        else:
            print("Error: Ambos números deben ser mayores que 0.")
            
    except ValueError:
        print("Error: Debe ingresar números enteros válidos.")

# ----------------------------------------------------------
# CALCULO DE LA FRACCION SIMPLIFICADA
# ----------------------------------------------------------
mcd = get_mcd(NUM, DEM)  # Calculamos el MCD

num = NUM // mcd   # Dividimos numerador por MCD
dem = DEM // mcd   # Dividimos denominador por MCD

# ----------------------------------------------------------
# MOSTRAR RESULTADO
# ----------------------------------------------------------
print(f"La fracción simplificada es: {num}/{dem}")
1