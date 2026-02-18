# Programa que solicita la edad de tres personas, calcula el promedio,
# y luego ajusta el promedio según la comparación con la primera edad

# Lista para guardar las edades
edades = []

# ----------------------------------------------------------
# PEDIR EDADES CON VALIDACIÓN
# ----------------------------------------------------------
for i in range(3):
    while True:
        try:
            edad = int(input(f"Ingrese la edad de la persona {i+1}: "))
            
            # Verificamos que la edad sea positiva
            if edad > 0:
                edades.append(edad)
                break
            else:
                print("Error: La edad debe ser un número positivo.")
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")

# ----------------------------------------------------------
# CALCULAR PROMEDIO
# ----------------------------------------------------------
prom = sum(edades) / len(edades)

print(f"El promedio de las edades es {prom}")

# ----------------------------------------------------------
# AJUSTAR EL PROMEDIO SEGÚN LA PRIMERA EDAD
# ----------------------------------------------------------
if prom > edades[0]:
    # Si el promedio es mayor que la primera edad → decrementamos 1
    prom -= 1  
    print(f"El promedio es mayor que la primera edad, se decrementa unitariamente: {prom}")
else:
    # Si el promedio es menor o igual que la primera edad → incrementamos 1
    prom += 1  
    print(f"El promedio es menor o igual que la primera edad, se incrementa unitariamente: {prom}")
