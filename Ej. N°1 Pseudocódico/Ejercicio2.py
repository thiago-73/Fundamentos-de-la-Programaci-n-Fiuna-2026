# 2. Leer un número y verificar si es flotante o entero. Considerar un numero como entero a partir de una tolerancia T.

print("Verificación de flotante o entero(Apartir de tolerancia).")

N = float(input("Ingrese número: "))
T = float(input("Ingrese tolerancia: ")) 

E = int(N)
X =  N - E

if X > T:

    print(N, "es un número flotante.")
else:
    print(N, "es un número entero.")

    
