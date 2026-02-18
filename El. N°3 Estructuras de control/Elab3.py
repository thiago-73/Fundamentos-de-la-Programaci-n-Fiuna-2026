# Programa que solicita un número del 1 al 12 y muestra el mes correspondiente
# Si el número no está en el intervalo [1, 12], el programa finaliza

# Lista de meses
# El índice de la lista coincide con el número del mes
# Se pone un 0 en la posición 0 porque los meses empiezan desde 1
meses = [0, "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
         "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

# ----------------------------------------------------------
# VALIDACIÓN DE ENTRADA
# ----------------------------------------------------------
try:
    numero = int(input("Ingrese un número del 1 al 12: "))
    
    # Verificamos que esté dentro del intervalo
    if numero < 1 or numero > 12:
        print("Valor ingresado incorrecto, el programa finalizará.")
    else:
        # Mostramos el mes correspondiente
        print("El mes correspondiente es:", meses[numero])

except ValueError:
    # Si el usuario ingresa letras o símbolos
    print("Error: Debe ingresar un número entero válido.")
