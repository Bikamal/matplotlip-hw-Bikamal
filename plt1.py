import matplotlib.pyplot as plt
from matplotlib.pyplot import*
import numpy as np
from numpy import*



x = np.array(['13', '16', '22', '1', '4', '28', '4', '8', '10', '20', '22', '19', '5', '24', '7', '25', '25', '13', '27', '2',  '7', '8', '24', '15', '25', '18', '6', '26', '14', '9'])
y = np.array([44, 48, 65, 68, 68, 10, 83, 20, 35, 87, 70, 88, 88, 12, 59, 65, 40, 85, 46, 89, 80, 38, 25, 76, 72, 9, 20, 80, 70, 80])



plt.title("This is title")

plt.xlabel("x-axis")
plt.ylabel("y-axis")

plt.plot(x, y, linestyle='solid', linewidth = 1,
         marker='^', markerfacecolor='blue', markersize=5)

plt.ylim(10,90,10)
plt.xticks(x)



plt.grid()
plt.show()