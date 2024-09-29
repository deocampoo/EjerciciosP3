
def RaizEntera(array, ini, fin, x):
    mid = (ini+fin)//2
    if(x<0):
        return -1
    elif(array[mid]*array[mid]==x):
        return array[mid]
    elif(array[mid]*array[mid]>x and array[mid+1]*array[mid+1]<x):
        return array[mid]
    else:
        if (array[mid+1]*array[mid+1]>x):
            return RaizEntera(array, mid+1, fin, x)
        else:
            return RaizEntera(array, ini, mid-1,x)

    

p = [1,2,3,4,5,6,7,8,9,10]
ini = 0
fin = len(p) - 1
x=6
resultado = RaizEntera(p, ini, fin,x)

print(resultado)  

 #------------------------------------------------------------------------------------------------------------------------------------------------------------------

 def RaizEntera(ini, fin, x):
    if x < 0:  # Si x es negativo, no tiene sentido calcular la raíz
        return -1
    
    if ini > fin:  # Condición base: cuando ini supera a fin
        return fin  # En este caso, fin será la raíz entera
    
    mid = (ini + fin) // 2  # Cálculo correcto del punto medio
    
    # Si encontramos el número exacto cuya raíz cuadrada es x
    if mid * mid == x:
        return mid
    
    # Si el cuadrado de mid es mayor que x pero el cuadrado del siguiente es menor
    if mid * mid < x and (mid + 1) * (mid + 1) > x:
        return mid
    
    # Caso recursivo: si mid^2 es mayor que x, buscamos en la mitad inferior
    elif mid * mid > x:
        return RaizEntera(ini, mid - 1, x)
    
    # Si mid^2 es menor que x, buscamos en la mitad superior
    else:
        return RaizEntera(mid + 1, fin, x)

# Ejemplo de uso
n = 6  # Valor del cual queremos encontrar la raíz entera
resultado = RaizEntera(0, n, n)
print(f"La raíz cuadrada entera de {n} es {resultado}")
