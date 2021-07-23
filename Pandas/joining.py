'''Joining of different data frames'''

import numpy as np
import pandas as pd

x1 = {'a':[3,5,7,],'b':[12,5,3]}
y1 = {'c':[9,0,10],'d':[15,7,8]}

x = pd.DataFrame(x1 , index=['p1','p2','p3'])
y = pd.DataFrame(y1 , index=['p1','p2','p3'])

# joining

print(x.join(y))
print(x.join(y,how='inner'))


