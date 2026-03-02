# Se solicita al usuario que ingrese dos números enteros
a = int(input())
b = int(input())

# Se utiliza un ciclo while para calcular el MCD (Máximo Común Divisor)
# El ciclo se repite mientras b sea diferente de 0
while b != 0:
    # Se aplica el algoritmo de Euclides:
    # Se intercambian los valores: a toma el valor de b
    # y b toma el residuo de a dividido entre b
    a, b = b, a % b

# Al terminar el ciclo, 'a' contiene el MCD de los dos números ingresados
print("MCD=", a)
