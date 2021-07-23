''' There are some more methods other than merge, concate, joining.
So here we are going to see that 

1. apply
2. sum
3. sort_values(by")
4. unique
5. nunique
6. value_counts
7. isnull
'''

import numpy as np
import pandas as pd

x = pd.DataFrame({'a':[1,3,3,4,35],'b':[70,80,9,10,10]})
print(x)
print("\n")
#getting index
print(x.index,"\n")
#getting columns 
print(x.columns,"\n")
#sum function
print(x['a'].sum,"\n")
#apply- it is used to  add some kind of function in to the data 
def inc(x):
    x = x+10
    return x

print(x['b'].apply(inc),"\n")
#  sorting 
print(x.sort_values('b'),"\n")
#unique - it gives the values that are unique  in the column 
print(x['a'].unique())
#nunique - it give only the number of unique values in the column
print(x['b'].nunique(),"\n")

#value counts - it represents that how many times a particular valu occur 
print(x['b'].value_counts())

#isnull
print(x.isnull())
