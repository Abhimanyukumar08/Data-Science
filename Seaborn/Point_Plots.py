import seaborn as sns
import matplotlib.pyplot as plt

#getting the data from the file
diamond = sns.load_dataset('diamonds')
#print(diamond)
# to stating data
print(diamond.head())

# now we will plot the data
# 1.dist plot
# sns.displot(diamond['price'])
# plt.show()

# rug plot
# sns.rugplot(diamond['price'])
# plt.show()

#kde plot
sns.kdeplot(diamond['price'])
plt.show()