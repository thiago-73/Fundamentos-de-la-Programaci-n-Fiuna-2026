# Función que determina si un número es triangular
# Un número triangular es aquel que puede escribirse como
# la suma de números consecutivos desde 1:
# 1, 1+2=3, 1+2+3=6, 1+2+3+4=10, etc.
def es_triangular(p):
    # Variable que representa el número que se irá sumando (1, 2, 3, ...)
    i = 1
    
    # Bucle que se repetirá hasta encontrar el resultado
    while True:
        # Se resta i al número p
        # Esto simula ir quitando 1, luego 2, luego 3, etc.
        p -= i
        
        # Si llegamos exactamente a 0, significa que
        # p era un número triangular
        if p == 0:
            return True
        
        # Si p sigue siendo positivo, seguimos probando
        # con el siguiente número
        elif p > 0:
            i += 1
        
        # Si p se vuelve negativo, significa que
        # no es un número triangular
        else:
            return False
        

# Se lee cuántos números se van a analizar
n = int(input())

# Lista donde se guardarán los números ingresados
numeros = []

# Se leen n números del usuario
for _ in range(n):
    
    # Se guarda el número como texto (string)
    # Esto permite recorrer cada dígito después
    num = input()
    
    # Se agrega el número a la lista
    numeros.append(num)
 

# Se analiza cada número ingresado
for i in range(n):
    
    # Variable para guardar la suma de los dígitos
    suma = 0
    
    # Se recorre cada dígito del número
    # Como el número está guardado como texto,
    # se puede recorrer carácter por carácter
    for x in numeros[i]:
        
        # Se convierte cada dígito a entero
        # y se suma al total
        suma += int(x)
        
    # Se verifica si la suma de los dígitos es triangular
    if es_triangular(suma):
        
        # Si lo es, se imprime "Bueno"
        print("Bueno")
        
    else:
        
        # Si no lo es, se imprime "MALO"
        print("MALO")