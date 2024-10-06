"""
Picos en un vector. Dado un vector u, un elemento pico es un elemento
que no es menor que sus vecinos inmediatos. Encuentre un algoritmo
eficiente (mejor que O(n)) que encuentre algún elemento pico en un
vector de n posiciones. Observe que puede haber varios elementos pico;
basta encontrar uno de ellos (siempre hay por lo menos uno.)
Ejemplo. Si la entrada fuera [0, 1, 3, 2, 5, 1, 0] la respuesta podría ser 3 o
5. Si la entrada fuera [7, 2, 3, 4, 5, 6] la respuesta podría ser 7 o 6. Si la
entrada fuera [1, 2, 3] la única respuesta sería 3.
"""

def pico(v, ini, fin):
    if(ini==fin):
        return v[ini]
    else:
        mid = (ini+fin)//2
        if(v[mid]>v[mid+1] and v[mid]<v[mid-1]):
            return mid
        elif(v[mid]<v[mid+1]):
            return pico(v, mid+1, fin)
        else:
            return pico(v, ini, mid-1)
    


# Prueba
v = [7, 2, 3, 4, 5, 6]
ini = 0
fin = len(v) - 1
resultado = pico(v, ini, fin)
print("Elemento mayoritario:", resultado)

#O(N LOG N)