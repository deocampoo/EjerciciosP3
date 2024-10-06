"""
Dado un vector A de números enteros, calcular elemento mayoritario. Si se tiene
un vector A de n enteros, un elemento x se denomina mayoritario de A si x
aparece en el vector A más de n/2 veces. Considerar que no puede haber más
de un elemento mayoritario.
"""
def ElementoMayoritario(ini, fin, l):
    if ini == fin: #Caso base 
        return l[ini]
    
    mid = (ini + fin) // 2
    
    left_majority = ElementoMayoritario(ini, mid, l)
    right_majority = ElementoMayoritario(mid + 1, fin, l)
    
    if left_majority == right_majority:
        return left_majority
    
    left_count = l[ini:fin+1].count(left_majority)
    right_count = l[ini:fin+1].count(right_majority)
    
    if left_count > right_count:
        return left_majority
    else:
        return right_majority

# Prueba
l = [1,8,5,2,3,1,2,1,4,1,3,1,0,1,2,2]
ini = 0
fin = len(l) - 1
resultado = ElementoMayoritario(ini, fin, l)
print("Elemento mayoritario:", resultado)
