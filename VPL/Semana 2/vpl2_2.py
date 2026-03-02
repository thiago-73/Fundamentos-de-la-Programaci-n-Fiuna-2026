# Este programa calcula la velocidad final de un objeto
# usando la fórmula del movimiento rectilíneo uniformemente acelerado:
# vf = vi + a * t

# input() permite que el usuario ingrese un valor.
# float() convierte ese valor (que es texto) en un número decimal.

# vi representa la velocidad inicial (en m/s).
vi = float(input())

# a representa la aceleración (en m/s^2).
a = float(input())

# t representa el tiempo transcurrido (en segundos).
t = float(input())

# Aplicamos la fórmula de la velocidad final:
# velocidad final = velocidad inicial + aceleración por tiempo
vf = vi + a * t

# Mostramos el resultado en pantalla.
# Se imprime un mensaje junto con el tiempo y la velocidad final calculada.
print("La velocidad final después de", t, "segundos es:", vf, "m/s")