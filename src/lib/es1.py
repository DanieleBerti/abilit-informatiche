def funzione(val):
 answer = False
 m= ["Farenheit 451", 10, "Zibaldone", 7,
 "Aristotle's Metaphysics", 5, "L'Alchimista", 1, "Harry Potter", 2, "Cime tempestose", 1]
 esauriti=[]
 ordine=[]
 if val in m:
  #print("Libro trovato")
  ind=m.index(val)
  m[ind+1]=m[ind+1]-1
  if m[ind+1]==0: 
   m.remove(m[ind])
   m.remove(0)
   if val not in esauriti:
    esauriti.insert(len(esauriti),val)
    #print("Libro esaurito")
    answer = False
  else:
    #print("Libro in prestito, numero copie disponibili :", 
 #m[ind+1])
    answer = True
 else:
  ordine.insert(len(ordine),val)
  #print("Libro non trovato, inserito nella lista dei libri da ordinare")
  answer = False
 return answer

print(funzione(input("Titolo Libro:")))