P = float(input())
r = float(input())
n = float(input())

A = P * ((1 + (r / 100)) ** n)

print("La cantidad final después de", int(n), "años es: $" + str(A))