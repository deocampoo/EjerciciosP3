"""
Dado un arreglo ordenado con números todos diferentes A[0..n-a], usted
quiere encontrar si existe un índice i tal que A[i] = i. Dé un algoritmo
divide & conquer que resuelva este problema en tiempo O(log n).

"""

def MismoIndice(v, ini, fin):

    if ini > fin:
        return -1 
    
    mid = (ini + fin) // 2

    if v[mid] == mid:
        return mid 
    
    # Si A[mid] > mid, buscamos en la mitad izquierda
    elif v[mid] > mid:
        return MismoIndice(v, ini, mid - 1)
    
    # Si A[mid] < mid, buscamos en la mitad derecha
    else:
        return MismoIndice(v, mid + 1, fin)

# Prueba del algoritmo
v = [-10, -5, 0, 3, 7, 9, 12]
resultado = MismoIndice(v, 0, len(v) - 1)

if resultado != -1:
    print(f"Se encontró un índice i tal que A[i] = i: {resultado}")
else:
    print("No se encontró ningún índice i tal que A[i] = i.")

