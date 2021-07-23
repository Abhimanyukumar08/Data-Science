import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# we will use subplot to plot multiple graphs in 
# it contains 3  parameters 1st(row) 2md(col) 3rd(number of graphs)

x = np.linspace(1,10,20)
y = x*x
z = x+y
plt.subplot(3,2,1)
plt.plot(x,x)
plt.subplot(3,2,2)
plt.plot(x,z)
plt.subplot(3,2,3)
plt.plot(y,z)
plt.subplot(3,2,4)
plt.plot(y,x)
plt.subplot(3,2,5)
plt.subplot(3,2,6)
plt.plot(z,y)
#tight_layout is used to separate the differnet graph and clearly understandable
plt.tight_layout()
plt.show()
