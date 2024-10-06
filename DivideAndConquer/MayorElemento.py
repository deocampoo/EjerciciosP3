"""
Suponga que nos dan un arreglo A[0..n-1] ordenado de enteros que ha
sido desplazado circularmente k posiciones hacia la derecha. Por ejemplo,
[35, 42, 5, 15, 27, 29] es un arreglo ordenado desplazado circularmente
k = 2 posiciones, mientras que [27, 29, 35, 42, 5, 15] ha sido desplazado
k = 4 posiciones; [1, 3, 5, 6, 7, 15] ha sido desplazado k = 0.
Queremos encontrar el mayor elemento del arreglo en A . Obviamente,
podemos encontrarlo en tiempo O(n). Describa un algoritmo que resuelva
el problema en tiempo O(log n).

"""

def MayorElemento(v, ini, fin):
    
    if (ini==fin): #Caso base
        return v[ini]
    else:
        mid = (ini+fin)//2
        if(v[mid]>v[mid]-1 and v[mid]>v[mid]+1): #Caso base
            return mid
        elif(v[mid]>v[mid-1] and v[mid] < v[mid]+1):
            return MayorElemento(v, mid+1, fin)
        else:
            return MayorElemento(v, ini, mid-1)
        

#Prueba

v =[35, 42, 5, 15, 27, 29]
ini = 0
fin = len(v)-1
resultado =MayorElemento(v, ini, fin)
print(resultado)

#Costo -> O(log n).