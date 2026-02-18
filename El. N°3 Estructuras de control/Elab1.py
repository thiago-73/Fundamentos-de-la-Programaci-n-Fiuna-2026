# Programa que verifica si una persona puede tomar bebidas alcohólicas
# Según la edad ingresada

# ----------------------------------------------------------
# VALIDACIÓN DE ENTRADA
# ----------------------------------------------------------
while True:
    try:
        edad = int(input("Ingrese su edad: "))
        
        # Verificamos que la edad sea positiva
        if edad >= 0:
            break
        else:
            print("Error: La edad no puede ser negativa.")
    except ValueError:
        print("Error: Debe ingresar un número entero válido.")

# ----------------------------------------------------------
# VERIFICACIÓN DE EDAD
# ----------------------------------------------------------
if edad < 21:
    # Si la edad es menor que 21 → prohibido beber alcohol
    print("Está prohibido que tomes bebidas alcohólicas")
else:
    # Si la edad es 21 o mayor → permitido
    print("Jaha a la BR a tomar")
