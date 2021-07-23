import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


x = np.linspace(1,10,20)
y = x*x
z = x+y

fig = plt.figure()
axes = fig.add_axes([0.1,0.1,0.8,0.8])
axes.set_xlabel("x-axis")
axes.set_ylabel("y-axis")
axes.set_title("hello")
# with stylling
# axes.plot(x,y, color='b' , linewidth = 5 , alpha = 1, linestyle = '--',  )
#markers
axes.plot(x,y, marker='o', markerfacecolor = 'green', markersize = 10)
#limits
axes.set_xlim(0,5)
axes.set_ylim(0,60)
plt.show()

#creating multigraph and labelling
# fig = plt.figure()
# axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
# axes2 = fig.add_axes([0.5,0.5,0.2,0.3])
# axes1.set_xlabel("x-axis")
# axes1.set_ylabel("y-axis")
# axes1.set_title("outer")
# axes2.set_xlabel("x-axis")
# axes2.set_ylabel("y-axis")
# axes2.set_title("inner")
# plt.show()


#subploting
# fig , axes = plt.subplots(1,2)
# axes[0].plot(x,y)
# axes[1].plot(y,x)

# axes[0].set_xlabel("x-axis")
# axes[1].set_xlabel("x-axis")
# axes[0].set_ylabel("y-axis")
# axes[1].set_ylabel("y-axis")
# axes[0].set_title("graph")
# axes[1].set_title("graph")
# plt.tight_layout()
# plt.show()

#figure size
# fig = plt.figure(figsize=(10,9))
# axes = fig.add_axes([0.1,0.1,0.8,0.8])
# axes.plot(x,y)
# plt.show()