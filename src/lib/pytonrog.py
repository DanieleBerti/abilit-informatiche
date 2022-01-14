import sys
import math



def f(y):
 if y >= 0.0:
  return y**5*math.exp(-y)
 else:
  return 0.0
infile='mydata.dat'
outfile='myout.dat'
indata = open( infile, 'r')
linee=indata.readlines()
indata.close()
processati=[ ]
x=[ ]
for el in linee:
 valori = el.split()
 x.append(float(valori[0])); y = float(valori[1])
 processati.append(f(y))
outdata = open(outfile, 'w')
i=0
for el in processati:
 outdata.write('%g %12.5e\n' % (x[i],el))
 i+=1
outdata.close()

#import numpy as np
#input = np.loadtxt("input.txt", dtype='i',
#delimiter=',')
#print(input)


l = []
t = []
m=4
with open('input.txt', 'r') as f:
 for line in f:
  line = line.strip()
  if len(line) > 0:
    l.append(list(map(int, line.split(','))))
#print(l)    
with open('input1.txt', 'r') as f:
 for line in f:
  line = line.strip()
  if len(line) > 0:
    t.append(list(map(int, line.split(','))))
#print(t)    
def print_matrix(matrix):
 for i in range(len(matrix)):
  for j in range(len(matrix[i])):
   print(str((matrix[i][j]))+"\t", end='')
  print("\n")
def matrix_x_matrix(l,t):
# iterate through rows of X
# result is 3x4
 result = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
 for i in range(len(l)):
  for j in range(len(t[0])):
   for k in range(len(t)):
     result[i][j] += l[i][k] * t[k][j]
 return result
print('prodotto matrice per matrice')
print_matrix(matrix_x_matrix(l,t))

def matrix_per_scalar(l,m):
 result1=[]
 for i in range(len(l)):
  tmp=[]
  for j in range(len(l[i])):
   tmp.append(l[i][j]*m)
  result1.append(tmp)
 return result1
print('prodotto matrice per scalare')
print_matrix(matrix_per_scalar(l,m))

class oggetti:
 def __init__(self, forma, lato):
  self.forma = forma
  self.lato = lato

g1=oggetti("quadrato",5)
print(g1.forma)


def divide(x, y):
 try:
  result = x / y
 except ZeroDivisionError:
  print("division by zero!")
 else:
  print("result is", result)
 finally:
  print("executing finally clause")
divide(1, 3)
divide(5,0)

j=0
for i in range(1,10):
  j=j+i
print("somma dei primi 9 naturali")   
print(j)

giorni = ['Lunedì', 'Martedì', 'Mercoledì']
value = [1, 2, 3]
result = zip(giorni, value)
result_list = list(result)
print(result_list)
g, v = zip(*result_list)
print('g =', g)
print('v =', v)