def potencia (n, a):
  if(n==0):
    return 1
  elif(n==2):
    return a*a
  else:
    return potencia(n//2,a)

a=int(input("Ingrese un numero:"))
n= int(input("Ingrese un numero:"))
resultado =potencia(n, a)

print(resultado)