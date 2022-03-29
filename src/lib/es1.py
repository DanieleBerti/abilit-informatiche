val=input("inserisci libro da trovare:")
m= { "Farenheit 451": 10, "Zibaldone": 7,
 "Aristotle's Metaphysics": 5, "L'Alchimista": 1, "Harry Potter": 2, "Cime tempestose": 1}
esauriti=[]
ordine=[]
if val in m:
  ind=m[val]
  m[val]=m[val]-1
  print("Libro in prestito")
  if m[val]==0: 
   m.pop(val)
   esauriti.append(val)
   #print(esauriti)
  #print(m)  
else:
 ordine.append(val)
 print("Libro non disponibile, è necessario fare un ordine d'acquisto")
 #print(ordine)
##########################################
def funzione(val):
 m= {"Farenheit 451": 10, "Zibaldone": 7,
 "Aristotle's Metaphysics": 5, "L'Alchimista": 1, "Harry Potter": 2, "Cime tempestose": 1}
 if val in m and m[val]>0:
  answer=True
 else:
  answer = False
 return answer 
print(funzione(input("Titolo Libro:")))