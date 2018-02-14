import matplotlib.pyplot as plt
import numpy as np

x = np.arange(4)
y = [1.0, 2.0, 4.0, 6.0]

barlist = plt.bar(x, y, edgecolor='white')
barlist[0].set_color('#e57373')
barlist[1].set_color('#ef5350')
barlist[2].set_color('#f44336')
barlist[3].set_color('#e53935')
        
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_color('black')
ax.spines['left'].set_color('black')
ax.spines['left'].set_linewidth(4.0)
ax.spines['bottom'].set_linewidth(4.0)

plt.xticks(())
plt.yticks(())

plt.xlim(-1, 4)
plt.ylim(-0.5, 8)

plt.show()