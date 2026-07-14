import numpy as np
a=np.array([20,30,40,50])
b=np.arange(4)
print("the elements in a are",a)
print("The elements in b are:",b)
print("add:",a+b)
print("sub:",a-b)
print("mul:",a*b)
print("div:",a/b)
print("increasing the number to the power of 4:",b**4)
print("applying sin and multiplying with 10",10*np.sin(a))
a[0]+=10
print("res after adding 10 to first element:",a)
print(np.dot(a,b))




