"""
En este ejercicio consideramos una función monótonamente decreciente
f : N → Z, esto es, una función definida sobre los números naturales que
devuelve valores enteros, de manera que es f (i) ≥ f (i + 1)). Asumiendo
que podemos evaluar f en cualquier punto i en tiempo constante,
queremos encontrar n = min{i ∈ N|f (i) ≤ 0}. En otras palabras,
queremos encontrar el valor en el que f se vuelve negativa.
Por supuesto, es posible resolver el problema en tiempo O(n) evaluando
f (1), f (2), f (3), . . . f (n). Describa un algoritmo que lo resuelva en
O(log n).
Ayuda: evalúe f en O(log n) valores x ≤ n cuidadosamente elegidos y tal
vez en algún valores entre n y 2n — pero tenga en cuenta que usted no
conoce el valor n inicialmente.

"""
def f(n, i):
    return n - i  


def buscar_n_negativo(ini, fin, n):
    # Caso base
    if ini > fin:
        return None 
    
    # Encontrar el punto medio
    mid = (ini + fin) // 2
    
    if f(n, mid) <= 0:
        izquierda = buscar_n_negativo(ini, mid - 1, n)  
        if izquierda is not None:
            return izquierda
        else:
            return mid
    else:
        return buscar_n_negativo(mid + 1, fin, n)  

# Prueba del algoritmo
n = 15
ini = 0
fin = 100  #Rango de 0 a 100
resultado = buscar_n_negativo(ini, fin, n)

if resultado is not None:
    print(f"El valor más pequeño de i donde f(i) <= 0 es: {resultado}")
else:
    print("No se encontró ningún valor de i donde f(i) sea <= 0.")

#Costo -> O(log n)