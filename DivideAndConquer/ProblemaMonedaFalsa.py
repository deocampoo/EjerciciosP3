def monedaFalsa(monedas):
    n = len(monedas) # es uno mas al índice
    
    if n==1:
        return 0
    
    tercio = n // 3 # si len es 7, es 0,1,2,3,4,5,6 --> tercio = 2. 1: 
    
    #Se definen los limites para saber como dividir el arreglo en los distintos grupos. 
    grupo1 = monedas[ : tercio] 
    grupo2 = monedas[tercio : tercio * 2]
    grupo3 = monedas[tercio * 2 : ]
    
    if (sum(grupo1) > sum(grupo2)): 
        return monedaFalsa(grupo1)
    elif (sum(grupo1) < sum(grupo2)):
        return tercio + monedaFalsa(grupo2)
    else:
        return tercio * 2 + monedaFalsa(grupo3)
        
monedas = [10, 10, 11, 10, 10, 10, 10, 10, 10]
indice_moneda_falsa = monedaFalsa(monedas)
print("La moneda falsa está en la posición:", indice_moneda_falsa)