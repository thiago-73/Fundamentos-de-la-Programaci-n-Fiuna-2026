# Se solicita al usuario que ingrese el día de la semana.
# El valor se convierte a entero. En este programa el número 7 representa el domingo.
dia = int(input())

# Se pide al usuario la cantidad de horas trabajadas durante el día (horas diurnas).
# Se usa float para permitir valores con decimales.
horas_diurnas = float(input())

# Se pide al usuario la cantidad de horas trabajadas durante la noche (horas nocturnas).
# También se usa float para permitir valores decimales.
horas_nocturnas = float(input())

# Se verifica si el día ingresado es 7 (domingo).
# En este caso se aplica un recargo del 25% al pago total.
if dia == 7:
    # Se calcula el pago por horas diurnas multiplicando las horas por la tarifa correspondiente.
    tarifa1 = horas_diurnas * 10000

    # Se calcula el pago por horas nocturnas multiplicando las horas por su tarifa.
    tarifa2 = horas_nocturnas * 20000

    # Se suma el pago de horas diurnas y nocturnas y luego se agrega un 25% adicional.
    jornal = (tarifa1 + tarifa2) + (0.25 * (tarifa1 + tarifa2))

# Si el día no es domingo, se paga normalmente sin recargo.
else:
    # Cálculo del pago por horas diurnas.
    tarifa1 = horas_diurnas * 10000

    # Cálculo del pago por horas nocturnas.
    tarifa2 = horas_nocturnas * 20000

    # Se suman ambos pagos para obtener el jornal total.
    jornal = (tarifa1 + tarifa2) 
    
# Se imprime el jornal final.
# Se convierte a entero para mostrar el valor sin decimales.
print(int(jornal))
