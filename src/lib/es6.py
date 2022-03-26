from random import randrange
a=True
s=True
cont=0
print("Indovina il numero naturale che sto pensando, esso è compreso tra 1 e 10, estremi inclusi!")
while a is True:
 n=randrange(1, 10)
 while a is True:
  while s is True:
   c=input("numero tentativi:")
   par=True
   try:
    c=int(c)
   except:
    par=False
   if par is False or c<0:
      print("Non hai inserito un dato valido come numero di tentativi")
   else:
     c=int(c)
     s=False
     cont=0
     break
  cont=cont+1
  while True:
   b=input("Guess:")
   par=True
   try:
    b=int(b)
   except:
    par=False
   if par is False or b<1 or b>10:
      print("Non hai inserito un dato valido come numero da indovinare")
   else:
     b=int(b)
     break
  if b==n:
    d=input("Hai indovinato,complimenti. Vuoi rigiocare ?[si/no]")
    if d=='si' or d=='no': 
      if d=='si':
        s=True
        break
      else:
        a=False
        break
    else:
      print("risposta non valida") 
      while True:
        d=input("Vuoi rigiocare ?[si/no]")
        if d=='si' or d=='no': 
          if d=='si':
            s=True
            break
          else:
            a=False
            break
        else:
         print("risposta non valida")
         continue      
    break 
  else:
    if cont==c:
      d=input("mi dispiace, hai finito i tentativi disponibili. Vuoi rigiocare ? [si/no]")
      if d=='si' or d=='no': 
       if d=='si':
         s=True
         break
       else:
        a=False
        break
      else:
       print("risposta non valida") 
       while True:
        d=input("Vuoi rigiocare ?[si/no]")
        if d=='si' or d=='no': 
          if d=='si':
            s=True
            break
          else:
            a=False
            break
        else:
         print("risposta non valida")
         continue      
      break 
    else:
      print("risposta sbagliata, numero tentativi rimasti",c-cont)

print("fine programma")
