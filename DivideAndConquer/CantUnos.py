"""
Suponga que v es un vector de n dígitos binarios ordenados. Encuentre
un algoritmo eficiente (mejor que O(n)) que determine la cantidad de
unos en v.
Ejemplo. Si v = [0, 0, 0, 1, 1, 1, 1, 1] (aquí n = 8). El programa debería
retornar 5, que es la cantidad de unos en v.
"""
def BuscarPrimerUno(v, ini, fin):
    if ini > fin: #Caso base
        return -1
    
    mid = (ini + fin) // 2
    
    if v[mid] == 1 and (mid == 0 or v[mid - 1] == 0):
        return mid #Caso base
    elif v[mid] == 0:
        return BuscarPrimerUno(v, mid + 1, fin)
    else:
        return BuscarPrimerUno(v, ini, mid - 1)

def CantUnosOrdenado(v):
    n = len(v)
    primerUno = BuscarPrimerUno(v, 0, n - 1)
    
    if primerUno == -1:
        return 0
    else:
        return n - primerUno 

# Prueba
v = [0, 0, 0, 1, 1, 1, 1, 1]
Resultado = CantUnosOrdenado(v)
print(Resultado)

#Costo -> 

# a=1; b=2 k=0.

# 1=1 -> O(n^0 log n) -> O(log n)