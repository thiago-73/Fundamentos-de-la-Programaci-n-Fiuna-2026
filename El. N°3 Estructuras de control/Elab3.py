# Elaborar un programa en que solicite al usuario que introduzca por teclado un número entero y positivo comprendido en el intervalo [1; 12] (en caso contrario finalizar el programa) e imprima en pantalla a que mes corresponde dicho número.

numero = int(input("Ingrese un número del 1 al 12: "))
meses = [0, "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio","Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

if numero < 1 or numero > 12:
    print("Valor ingresado incorrecto, el programa finalizará.")
else:
    print("El mes correspondiente es:", meses[numero])