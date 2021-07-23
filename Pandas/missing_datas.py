import numpy as np
import pandas as pd

d = {'a':[1,2,3,4,5],'b':[6,7,8,9,np.nan],'c':[2,45,6,np.nan,np.nan],'d':[12,7,np.nan,np.nan,np.nan],'e':[5,np.nan,np.nan,np.nan,np.nan]}
print(d) #np.nan used to deifne the missing element
# to convert this dictionary into data frame
df = pd.DataFrame(d)
print(df)

# want to check the rows with the missing values
print(df.dropna(axis=0))
print(df.dropna(axis=1))

# if we want to work with any particular missing values
#like i want the row with atleast 3  values are available then :
print(df.dropna(thresh=3))
print(df.dropna(thresh=4))
print("\n\n\n")
'''Now to fill the null place with some values '''

# suppose we want to fill all the nan values with 1:
print(df.fillna(1))
print("\n")
# replacing the nan value with the average value in it particular row or column
print(df['d'].fillna(value=df['d'].mean()))
print(df.iloc[2,2].fillna(value=df.iloc[2,2].mean()))
