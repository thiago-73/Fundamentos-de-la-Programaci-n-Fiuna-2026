# 2.2-Escriba un programa en que lea las coordenadas de cuatro puntos diferentes en un plano: A (x1, y1), B (x2, y2), C (x3, y3) y D (x4, y4) y luego verifique si las rectas AB y CD son ortogonales o no.

x1 = float(input("Ingrese coordenada x1: "))
y1 = float(input("Ingrese coordenada y1: "))

x2 = float(input("Ingrese coordenada x2: "))
y2 = float(input("Ingrese coordenada y2: "))

x3 = float(input("Ingrese coordenada x3: "))
y3 = float(input("Ingrese coordenada y3: "))

x4 = float(input("Ingrese coordenada x4: "))
y4 = float(input("Ingrese coordenada y4: "))

if x2 == x1:
    m_ab = None
else:
    m_ab = (y2 - y1) / (x2 - x1)

if x4 == x3:
    m_cd = None
else:
    m_cd = (y4 - y3) / (x4 - x3)

if m_ab is None and m_cd == 0:
    print("Las rectas AB y CD son ortogonales")
elif m_cd is None and m_ab == 0:
    print("Las rectas AB y CD son ortogonales")
elif m_ab is not None and m_cd is not None and m_ab * m_cd == -1:
    print("Las rectas AB y CD son ortogonales")
else:
    print("Las rectas AB y CD no son ortogonales")