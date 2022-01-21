import np

c=np.arange(1,5)
d=np.array([[1,1,1,1],[2,2,2,2]])
print (d, "+", c ,"=", d+c)

a=np.arange(0,4*np.pi,0.1)
#VECTORIZED VERSION
y=np.sin(a)*2
#SCALAR VERSION
y=np.zeros(len(a))
for i in range(len(a)):
  y[i]=np.sin(a[i])*2

a=np.array([[1,2],[2,2]])
print(a.shape)
b=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(b.shape)

list=range(1,5)
a=np.array(list)
print(a)
print(a.dtype)

b=np.identity(2, dtype=None)
print(b)

b=np.array([5,6,7,8])
c=np.arange(1,5)
d=c+b
print("Sum " ,b,"+",c, "= ", b+c)
b+=1
print("Autoincrement b +=1 b=", b)
print("Multiply c*3 " ,c, "* 3= ",c*3)
print("Sin (c)", np.sin(c))

a=np.arange(20)
a.resize(8,9)
print(a)

a=np.arange(1,5)
b=np.arange(2,6)
a+=b
print(a)
print(a[3])
print(a[1:3])