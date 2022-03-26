from random import randrange
a=True
print("Indovina il numero naturale che sto pensando, esso è compreso tra 1 e 10, estremi inclusi!")
while a is True:
  n=randrange(1, 10)
  while True:
   c=input("numero tentativi:")
   par=True
   try:
    b=int(b)
   except:
    par=False
   if par is False or b<1 or b>10:
      print("Non hai inserito un dato valido come numero di tentativi")
      continue
   else:
     break
  while True:
   b=input("Guess:")
   par=True
   try:
    b=int(b)
   except:
    par=False
   if par is False or b<1 or b>10:
      print("Non hai inserito un dato valido come numero da indovinare")
      continue
   else:
     break
  if b==n:
    d=input("Hai indovinato,complimenti. Vuoi rigiocare ?[si/no]")
    if d=='si' or d=='no': 
      if d=='si':
        continue
      else:
        a=False
        break
    else:
      print("risposta non valida") 
      while True:
        d=input("Vuoi rigiocare ?[si/no]")
        if d=='si' or d=='no': 
          if d=='si':
            continue
          else:
            a=False
            break
        else:
         print("risposta non valida")
         continue      
  break