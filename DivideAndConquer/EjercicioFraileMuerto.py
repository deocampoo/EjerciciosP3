def NumeroRepepetido(p, ini, fin):
    mid = (ini + fin) // 2
    
    if ini > fin or fin < ini: #De esta forma se verifica que ini y fin esten dentro de los limites validos.
        return -1

    # En cada if se verifica que  mid no se salga del rango y si el numero que esta en la posicion mid de ese momento es igual al que esta en mid+1 o mid-1 
    if mid > 0 and p[mid] == p[mid-1]:
        return mid  # Devuelve el número repetido
    if mid < len(p) - 1 and p[mid] == p[mid+1]:
        return mid+1  # Devuelve el número repetido

   #Continuar búsqueda en el lado correcto
    if p[mid]!=p[mid+1]: 
        return NumeroRepepetido(p, mid + 1, fin)
    else:
        return NumeroRepepetido(p, ini, mid - 1)

p = [0, 1, 1, 2, 3, 4, 5, 6]
ini = 0
fin = len(p) - 1
resultado = NumeroRepepetido(p, ini, fin)

print(resultado)  

