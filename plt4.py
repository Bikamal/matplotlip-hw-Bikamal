import matplotlib.pyplot as plt
from matplotlib.pyplot import*
import numpy as np
from numpy import*

y = np.array([27.7, 24.6, 16.5, 20, 9.2, 2])
mylabels = ["India", "UK", "Germany", "USA", " South Korea", "Australia"]
myexplode = [0, 0, 0, 0.3, 0, 0]

plt.pie(y, labels = mylabels, explode = myexplode,  autopct='%1.1f%%',shadow= True)
plt.show() 