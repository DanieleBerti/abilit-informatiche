def funzione(el,lista=[]):
 if el in lista:
  print("Elemento trovato nella lista fornita con indice",lista.index(el))
 else:
  print("Elemento non trovato nella lista fornita")
#esempi
Mesi = ["Gennaio", "Febbraio", "Marzo","Aprile","Maggio","Giugno","Luglio","Agosto","Settembre","Ottobre","Novembre","Dicembre"]
funzione(el = "Ottobre", lista = Mesi)
funzione(el = [1,2,3], lista = Mesi)