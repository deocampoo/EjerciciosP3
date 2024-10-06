"""
El problema de la moneda falsa. El banco de Fraile Muerto recibió su
primera remesa de monedas de cinco pesos. Dentro de un lote de n
monedas se sabe que hay una falsa. La moneda falsa no se distingue de
las otras sino por su peso: es un poco más pesada. Se dispone de una
balanza de platillos que no da el peso cuantitativo; sólo dice si un grupo
de monedas en un platillo pesa más, menos, o lo mismo que otro grupo
de monedas en el otro platillo.
Disponiendo de este hardware, más bien modesto, determine el número
mínimo de pesadas (en el peor caso) para identificar la moneda falsa.
"""


def monedaFalsa(monedas):
    n = len(monedas) 
    
    if n==1:
        return 0
    
    tercio = n // 3 
    
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