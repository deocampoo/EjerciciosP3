def Mayoritario(l, ini, fin):
    if ini == fin:
        return (l[ini], 1)  # Cambié l(1) por l[ini], para obtener el valor correcto del elemento en la lista
    else:
        mid = (ini + fin) // 2

        m1 = Mayoritario(l, ini, mid)    # Cambié el orden de los parámetros
        m2 = Mayoritario(l, mid + 1, fin)

        if m1 is None and m2 is None:
            return None
        elif m1 is None:
            return m2
        elif m2 is None:
            return m1
        elif m1[0] == m2[0]:
            return (m1[0], m1[1] + m2[1])
        elif m1[1] > m2[1]:
            return (m1[0], m1[1] - m2[1])
        elif m2[1] > m1[1]:
            return (m2[0], m2[1] - m1[1])
        else:
            return None

# Prueba
l = [1, 2, 2, 3, 2, 1, 4, 1, 3, 1]
ini = 0
fin = len(l) - 1
resultado = Mayoritario(l, ini, fin)  
print("Elemento mayoritario:", resultado)
