def funzione(lib,lista=[]):
 if lib in lista:
  print("Elemento trovato nella lista fornita con indice",lista.index(lib))
 else:
  print("Elemento non trovato nella lista fornita")


Mesi = ["Gennaio", "Febbraio", "Marzo","Aprile","Maggio","Giugno","Luglio","Agosto","Settembre","Ottobre","Novembre","Dicembre"]
funzione(lib = "Ottobre", lista = Mesi)
funzione(lib = "Mela", lista = Mesi)