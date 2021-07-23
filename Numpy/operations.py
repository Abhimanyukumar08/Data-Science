# addtion
import numpy as np

x = np.arange(0,10)
y= np.arange(10,20)
print(x+y)
print(x.sum())


'''see the more operations from this website
https://www.tutorialspoint.com/numpy/numpy_arithmetic_operations.htm '''

print(np.full((3,10),True))

a = np.array([1,1,2,3,4,5,6,7,9,8])

b = np.array([0,2,1,3,4,8,9])

print(np.intersect1d(a,b))
print(a[-7])
print(a[(a>-5) & (a<=10)])
