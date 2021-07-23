'''      
different method depends on NUMPY

'''

import numpy as np

x=[1,2,3,5,7]
y=[[12,4,5,],[11,5,90],[3,4,5]]
print(np.array(y),"\n")
print(x,"\n")

# creating zero matrices and perform some operation on it
n=np.zeros((3,3))
# n=np.zeros((3,3)) +5 : #for adding value in the matrix

print(n)
# identity matrix
print(np.eye(4),"\n")

#uniary matrix
print(np.ones((3,4)),"\n")
# to create the array between some range 
print(np.arange(30),"\n")
#to create matrix with some range 
print(np.arange(50).reshape(5,10),"\n")

#linear space to create array in  which each element are linearly space
print(np.linspace(10,50,10),"\n")
print(np.linspace,"\n")

# to find max & min in array
x=np.array(x)
print(x.max(),"\n")
print(x.min(),"\n")

#to get the index of any element
print(x.argmin(),"\n")
print(x.argmax(),"\n")

#to generate any random
print(np.random.rand(5),"\n" )
print(np.random.randn(5),"\n" ) #for negative values also
print(np.random.randint(5),"\n" ) #for integer values

