
#stringa = input("Inserisci stringa: ")
#a = {}
#for ch in stringa:
    #if ch in a:
        #a[ch] += 1
    #else:
        #a[ch] = 1

#import pprint

#pp = pprint.PrettyPrinter(indent=1, width=10)
#pp.pprint(a)
def draw_histogram(histogram_dict):
  for key in histogram_dict:
    if histogram_dict[key] >= 1:
      print (key + ": " + histogram_dict[key]*"*")

with open("lipsum.txt") as f:
    for line in f:
     a = {}
     for ch in line:
      if ch in a:
          a[ch] += 1
      else:
          a[ch] = 1
     if '\n' in a:
       a.pop('\n')
     draw_histogram(a)
