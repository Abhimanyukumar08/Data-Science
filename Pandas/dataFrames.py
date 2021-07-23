import numpy as np
import pandas as pd

'''CREATING DATA FRAMES'''


# first make the lists of datas
A = [1,2,3,4]
B = [5,6,7,8]
C = [9,10,11,12]
D = [13,14,15,16]
E = [17,18,19,20]
#now systax to create data frames

df = pd.DataFrame([A,B,C,D,E],['a','b','c','d','e'],['w','x','y','z'])
#to create DF follow the sequence 1.all lists,2.row nmae,3.coloum name
print(df)


# adding extra column in the DF

df['p'] = df['y'] + df['z']
print(df)


''' remove any row or column'''

#row
df.drop('e',inplace = True)
#column , we have to paas axis because x-axis=0 & y-axis=1
df.drop('p',axis=1,inplace=True)
print(df)

'''Accessing the element in the dataframe'''

#column
print(df['y'])

#row
print(df.loc['b'])
# numeric index row
print(df.iloc[2])
# access any particular element
print(df.loc['c','x'])


'''Conditional Selection'''

#suppose we want the values that are greater than 4
print(df>4)   #gives the boolean values
print(df[df>4]) #gives the float values 

#retrive the values of any particular row or column
print(df[df['w'] > 3]) #give the rows output
print(df[df['w']>10][['w','x']])




