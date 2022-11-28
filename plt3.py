import matplotlib.pyplot as plt
from matplotlib.pyplot import*
import numpy as np
from numpy import*


x = np.arange(0,50, 0.13)   # start,stop,step
y = np.sin(x)
z = np.cos(x)

plt.plot(x,y,z)

x1=np.arange(-17*np.pi,17*np.pi,0.13)
y1=np.sin(x1)
z1=np.cos(x1)
plt.plot(x1,y1,z1)

#x2=np.arange(-0.5*np.pi,17*np.pi,0.13)
#z2=np.cos(x2)

#plt.plot(x2,z2)


plt.xlim(0,50)
plt.ylim(-1.1,1.1)



plt.grid()

plt.show()


