import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = np.linspace(0,10,20)
y = x*x
z = x+y
print(y,"\n",z)
# to plot the values
# plt.plot(x,y)
#labelling the  graph
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("first graph")
#multiple line in single graph
plt.plot(x,y,z,y, label = 'legend')
plt.legend()
plt.show()
