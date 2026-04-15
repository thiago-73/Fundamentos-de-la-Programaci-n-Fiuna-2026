# Se lee un número entero (cantidad de elementos, aunque no se usa directamente después)
n = int(input())

# Se lee una lista de números en una sola línea y se convierte a enteros
L1 = list(map(int, input().split()))

# Lista donde se guardará el resultado final (elemento + cantidad de repeticiones)
L2 = []

# Lista para guardar los valores que ya fueron procesados (evita duplicados)
vistos = []

# Se recorre cada elemento de la lista original
for j in L1:
    # Se verifica si el elemento no ha sido contado antes
    if j not in vistos:
        
        # Se cuenta cuántas veces aparece ese elemento en la lista original
        cantidad = L1.count(j)
        
        # Se agrega el número al resultado
        L2.append(j)
        
        # Se agrega la cantidad de repeticiones del número
        L2.append(cantidad)
        
        # Se marca el número como ya visto para no repetirlo
        vistos.append(j)

# Se imprime la lista final en una sola línea separada por espacios
print(" ".join(map(str, L2)))