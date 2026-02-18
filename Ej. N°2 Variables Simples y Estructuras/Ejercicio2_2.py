# Programa que verifica si las rectas AB y CD son ortogonales
# Dos rectas son ortogonales si sus pendientes cumplen:
# m1 * m2 = -1, o si una es vertical y la otra horizontal

# ----------------------------------------------------------
# FUNCION PARA PEDIR COORDENADAS
# ----------------------------------------------------------
def pedir_coordenada(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Error: Debe ingresar un número válido.")

# Pedimos las coordenadas de los cuatro puntos
print("Ingrese coordenadas del punto A:")
x1 = pedir_coordenada("x1: ")
y1 = pedir_coordenada("y1: ")

print("Ingrese coordenadas del punto B:")
x2 = pedir_coordenada("x2: ")
y2 = pedir_coordenada("y2: ")

print("Ingrese coordenadas del punto C:")
x3 = pedir_coordenada("x3: ")
y3 = pedir_coordenada("y3: ")

print("Ingrese coordenadas del punto D:")
x4 = pedir_coordenada("x4: ")
y4 = pedir_coordenada("y4: ")

# ----------------------------------------------------------
# CALCULO DE PENDIENTES
# ----------------------------------------------------------
# Pendiente de AB
if x2 == x1:
    m_ab = None  # Recta vertical → pendiente indefinida
else:
    m_ab = (y2 - y1) / (x2 - x1)

# Pendiente de CD
if x4 == x3:
    m_cd = None  # Recta vertical → pendiente indefinida
else:
    m_cd = (y4 - y3) / (x4 - x3)

# ----------------------------------------------------------
# VERIFICAR ORTOGONALIDAD
# ----------------------------------------------------------
# Casos especiales: una recta vertical y la otra horizontal
if (m_ab is None and m_cd == 0) or (m_cd is None and m_ab == 0):
    print("Las rectas AB y CD son ortogonales")
# Caso general: producto de pendientes = -1
elif m_ab is not None and m_cd is not None and round(m_ab * m_cd, 5) == -1:
    print("Las rectas AB y CD son ortogonales")
else:
    print("Las rectas AB y CD no son ortogonales")
