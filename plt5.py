import matplotlib.pyplot as plt
from matplotlib.pyplot import*
import numpy as np
from numpy import*

quantity = np.array([1, 4, 3, 2])
material = ['Butter', 'Egg', 'Flour', 'Sugar']

plt.pie(quantity, labels = material,  autopct='%1.1f%%')


plt.legend(labels= material, loc='upper center', 
           bbox_to_anchor=(0.5, -0.04), ncol=len(quantity))


plt.show() 