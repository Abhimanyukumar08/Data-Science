import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


x = np.linspace(0,10,20)
y = x*x
z = x+y

#simple plot
plt.plot(x,y)
plt.show()
#dotted or scatter
plt.scatter(x,y)
#historgram
plt.hist(x,y)
#bar graph
plt.bar(x,y)
#fill 
plt.fill(x,y)
plt.show()
