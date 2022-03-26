def funzione(a,b):
 a=int(a)
 b=int(b)
 for i in range(b):
   if i==0 or i==b-1:
    for j in range(a):
        print('*', end=' ')
    print()
   else:
    for k in range(a):
      if k==0 or k==a-1:
        print('*', end=' ')
      else:
        print(' ', end=' ')
    print()

print("Ricorda di inserire numeri interi positivi e maggiori di 2, buon divertimento!")
while True: 
 while True:
  par=True
  a=input("lunghezza rettangolo:")
  try:
   a=int(a)
  except:
   par=False
  if par is False or a<3:
   print("Dato non valido, riprova")
   break
  else:
   a=int(a)
  par=True
  b=input("altezza rettangolo:")
  try:
   b=int(b)
  except:
   par=False
  if par is False or b<3:
   print("Dato non valido, riprova")
   break
  else:
   b=int(b)  
  funzione(a,b)
  break