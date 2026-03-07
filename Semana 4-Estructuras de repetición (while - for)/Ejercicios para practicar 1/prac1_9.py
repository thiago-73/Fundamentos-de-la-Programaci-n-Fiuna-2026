# Se utiliza un bucle infinito para pedir el número hasta que sea válido
while True:
    try:
        # Se solicita al usuario que ingrese un número entero
        # int() convierte el valor ingresado (texto) en un número entero
        n = int(input("Ingrese número: "))
        
        # Se verifica que el número sea positivo y menor a 100000
        if n > 0 and n < 100000:
            # Si el número cumple la condición se sale del bucle
            break
        else:
            # Si el número no cumple la condición se muestra un mensaje de error
            print("El número debe ser positivo y menor a 100000")
            
    # Si el usuario ingresa algo que no puede convertirse a entero
    # Python genera un ValueError y se captura con except
    except ValueError:
        print("Error: Debe ser un número entero.")

# str(n) convierte el número en texto (cadena de caracteres)
# len() cuenta la cantidad de caracteres que tiene la cadena
# Como cada carácter representa un dígito, obtenemos la cantidad de dígitos del número
k = len(str(n))

# Se imprime el resultado mostrando cuántos dígitos tiene el número ingresado
# f"" permite insertar variables dentro del texto usando {}
print(f"La cantidad de dígitos de {n} es {k}")