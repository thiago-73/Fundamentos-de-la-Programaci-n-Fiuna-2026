# Función que determina si un año es bisiesto
def es_bisiesto(año):
    # Un año es bisiesto si:
    # - Es divisible entre 4
    # - Y no es divisible entre 100, excepto si también es divisible entre 400
    return (año % 4 == 0 and (año % 100 != 0 or año % 400 == 0))

# Bloque para capturar errores si el usuario no ingresa números válidos
try:
    # Se solicita el año
    año = int(input())
    
    # Se solicita la cantidad de días desde el 1 de enero
    dias = int(input())
    
    # Validación: ambos valores deben ser positivos
    if año < 0 or dias < 0:
        print("Error: El timestamp debe ser un número entero positivo")
    else:
        # Se verifica si el año es bisiesto
        if es_bisiesto(año):
            # Lista con la cantidad de días por mes (índice 1 = enero)
            meses = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            max_dias = 366
        else:
            # Lista para año normal (febrero tiene 28 días)
            meses = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            max_dias = 365

        # Validación: los días no pueden exceder los del año
        if dias >= max_dias:
            print("Error: cantidad de días fuera del rango del año")  
        else:
            # Se guarda el valor original de días
            dias1 = dias
            
            # i representará el mes (1 = enero, 2 = febrero, etc.)
            i = 1
            
            # Se recorre mes por mes hasta encontrar el correspondiente
            while i <= 12:
                
                # Si los días alcanzan para cubrir el mes completo
                if dias >= meses[i]:
                    # Se restan los días del mes actual
                    dias -= meses[i]
                    
                    # Se pasa al siguiente mes
                    i += 1
                else:
                    # Si no alcanza, estamos en el mes correcto
                    # Se calcula el día (se suma 1 porque se cuenta desde 0)
                    dia = dias + 1
                    
                    # Se guarda el mes actual
                    mes = i
                    break
        
            # Se imprime el resultado
            print(f"Año {año} , {dias1} días después del 1 de enero:") 
            
            # Se imprime el mes y día con formato de dos dígitos
            print(f"Mes: {mes:02}, Día: {dia:02}")      

# Captura de error si el usuario no ingresa enteros
except ValueError:
    print("Error: Debe ingresar un número entero")