
stringa = input("Inserisci stringa: ")
a = {}
for ch in stringa:
    if ch in a:
        a[ch] += 1
    else:
        a[ch] = 1

import pprint

pp = pprint.PrettyPrinter(indent=1, width=10)
pp.pprint(a)
