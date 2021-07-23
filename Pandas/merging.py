import numpy as np
import pandas as pd

df1 = pd.DataFrame({'a':[2,3,4],"b":[5,6,7],"key1":[1,2,5]})
df2 = pd.DataFrame({'c':[6,0,1],"b":[9,16,4],"key1":[1,2,5]})


print(pd.merge(df1,df2, how='outer',on='key1'))
