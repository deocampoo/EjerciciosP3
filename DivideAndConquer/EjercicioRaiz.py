
"""
Calcule la raíz cuadrada entera de un número n > 0 utilizando
divide-and-conquer. Recuerde que la raíz cuadrada entera de un número
n es el máximo valor entero u tal que u

2 ≤ n. Por ejemplo, la raíz entera de 18 es 4 y la de 9 es 3.

"""

def RaizEntera(array, ini, fin, x):
    if x < 0:
        return -1  #Caso base.
    if ini > fin: #Caso base.
        return array[fin]  
    
    mid = (ini + fin) // 2

    if array[mid] * array[mid] == x: #Caso base. 
        return array[mid]
    elif array[mid] * array[mid] < x:
        if mid + 1 <= fin and array[mid + 1] * array[mid + 1] > x:
            return array[mid]  
        return RaizEntera(array, mid + 1, fin, x)
    else:
        return RaizEntera(array, ini, mid - 1, x)

p = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ini = 0
fin = len(p) - 1
x = 74
resultado = RaizEntera(p, ini, fin, x)

print(resultado)



"""
El costo de este algoritmo es de O(Log n). 
"""