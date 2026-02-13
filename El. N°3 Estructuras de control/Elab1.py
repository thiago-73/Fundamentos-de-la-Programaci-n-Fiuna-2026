# Elaborar un programa en que solicite al usuario que introduzca por teclado su edad, si esta es menor que 21 años que imprima en pantalla un mensaje que diga “Está prohibido que tomes bebidas alcohólicas”, en caso contrario imprimir en pantalla “Jaha a la BR a tomar”.

edad = int(input("Ingrese edad: "))

if edad < 21:
    print("Está prohibido que tomes bebidas alcohólicas")
else:
    print("Jaha a la BR a tomar")
