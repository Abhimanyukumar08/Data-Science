'''Here we learn about the data analysis in data frames by using group by'''

import numpy as np
import pandas as pd

# there is a person who is selling fruits
p = {'items':['apple','apple','orange','orange','guns','guns'],'days':['monday','tuesday','wednesday','thursday','friday','saturday'],'sales':[123,440,300,100,7,13]}
df = pd.DataFrame(p)
print(df)
print('\n\n')

#now use groupby clause to calculate the mean sales
print(df.groupby('items').mean())

#total sum 
print(df.groupby('items').sum())
#standard addition
print(df.groupby('items').std())
#max & min
print(df.groupby('items').max())
print(df.groupby('items').min())

#info about the table 
print(df.groupby('items').describe())
print(df.groupby('items').describe().transpose())


