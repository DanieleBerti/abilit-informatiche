stringa = input("Inserisci stringa: ")
a = {}
for ch in stringa:
    if ch in a:
        a[ch] = a[ch] + 1
    else:
        a[ch] = 1
print(a)
#######################################à
def histo(b):
  for key in b:
    if b[key] >= 1:
      print (key + ": " + b[key]*"*")
with open("lipsum.txt") as f:
    for line in f:
     a = {}
     for ch in line:
      if ch in a:
          a[ch] = a[ch] + 1
      else:
          a[ch] = 1
     if '\n' in a:
       a.pop('\n')
     histo(a)