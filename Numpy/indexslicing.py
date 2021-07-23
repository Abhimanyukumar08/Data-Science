import numpy as np

# creating array in particular range 
x = np.arange(0,10)
print(x)

# indexing the array 
print(x[0])
print(x[-2])
print(x[9])

#Slicing the array 
print(x[:7])
print(x[6:])
print(x[2:8])
print(x[-9:-1]) #for negative slicing

# editing the value in the array by indexing and slicing

y = x[2:5] = 30
print(y)
print(x) # here the original array is also changed 

# now using the  copy function

y = x.copy()
y[4:8] = 23
print(y)
print(x,"\n\n")


#...........................FOR 2D ARRAY......................

a = np.arange(50).reshape(5,10)
print(a)

#indexing
print(a[1,5])
print(a[0,7])

#slicing
print(a[0:2,3:],"\n\n")
print(a[1:4,3:6],"\n\n")
print(a[1:5,3:8])

# condtional selection
print(y[y>15])
print(y[y % 5])



