import matplotlib.pyplot as plt
from matplotlib.pyplot import*
import numpy as np
from numpy import*
from mpl_toolkits import mplot3d


fig = plt.figure()
ax = plt.axes(projection='3d')

zline = np.linspace(0, 15, 1000)
xline = np.sin(zline)
yline = np.cos(zline)
ax.plot3D(xline, yline, zline, 'gray')