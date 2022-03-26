while True:
  while True:
   N=input("inserisci intero:")
   par=True
   try:
    N=int(N)
   except:
    par=False
   if par is False or N<=0:
      print("Non è un intero positivo, riavvio programma")
      continue
   else:
     print(' # '* N)
     break
  break  