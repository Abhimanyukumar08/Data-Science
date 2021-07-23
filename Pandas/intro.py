import numpy as np
import pandas as pd

x=['a','b','c','d','e']
x2 = ['a','b','c','d','f']
y=[1,2,3,4,5]
z={1:'a',2:'b',3:'c',4:'d',5:'e'}

# creating the series 

# print(pd.Series(x,y))
# print(pd.Series(y,x))

# arithemetic operations on series

a = pd.Series(y,x)
b = pd.Series(y,x2)
print(a,"\n",b)
# it will the add data with equal index 
print(a+b)
#if the index does match then it will return nan

#indexing and slicing
print(a["d"])
print(a[2])
print(a[2:4])
print(b["c":]) 

