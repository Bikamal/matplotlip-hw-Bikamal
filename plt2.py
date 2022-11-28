import matplotlib.pyplot as plt
from matplotlib.pyplot import*
import numpy as np
from numpy import*




plt.title("Best fit line using regression method")

plt.xlabel("x-axis")
plt.ylabel("y-axis")

xpoints = np.array([0.02, 0.6])
ypoints = np.array([0.02, 0.6])

plt.plot(xpoints, ypoints, color='r')

x=np.array([0.02, 0.08, 0.12, 0.14, 0.2, 0.25, 0.28, 0.3, 0.32, 0.36, 0.38, 0.4, 0.405, 0.42, 0.43, 0.44, 0.45, 0.47, 0.5, 0.53, 0.6])
y=np.array([0.02, 0.105, 0.1, 0.13, 0.2, 0.18, 0.205, 0.22, 0.32, 0.3, 0.4, 0.41, 0.3, 0.4, 0.5, 0.4, 0.505, 0.58, 0.595, 0.5, 0.6])
plt.plot(x, y, 'o', color='skyblue')


plt.xlim(0,0.62)
plt.ylim(0,0.62)


plt.show()