# Se solicita al usuario que ingrese la cantidad de personas
# sobre las que se registrarán las edades
n = int(input())

# Contador para las personas mayores de edad (18 años o más)
mayores = 0

# Contador para las personas menores de edad
menores = 0

# Se utiliza un ciclo que se repetirá n veces
# Cada repetición corresponde a la edad de una persona
for _ in range(n):

    # Se solicita al usuario que ingrese la edad
    edad = int(input())
    
    # Se verifica si la persona es mayor de edad (18 o más)
    if edad >= 18:
        # Se incrementa el contador de mayores de edad
        mayores += 1
    else:
        # En caso contrario, se incrementa el contador de menores de edad
        menores += 1
        
# Se calcula el total de personas ingresadas
total = mayores + menores

# Se calcula el porcentaje de personas mayores de edad
# Primero se divide la cantidad de mayores entre el total
# Luego se multiplica por 100 para obtener el porcentaje
# Finalmente se convierte a entero
porcentaje_mayores = int((mayores / total) * 100)

# Se calcula el porcentaje de personas menores de edad
porcentaje_menores= int((menores / total) * 100)

# Se muestran los resultados en pantalla
# Utilizando f-strings para insertar los valores dentro del texto
print(f"Mayores de edad: {porcentaje_mayores}% Menores de edad: {porcentaje_menores}%")