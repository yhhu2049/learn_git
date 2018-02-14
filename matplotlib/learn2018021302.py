# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 15:04:52 2018

@author: hyh
"""

import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-3, 3, 256)
y1 = np.sin(x)
y2 = np.cos(x)
plt.plot(x, y1, 'r',label = 'sine')
plt.plot(x, y2, 'b',label = 'cos')
plt.xlabel('x-axis')
plt.title("Simple Plot")
#plt.xlabel('x-axis')
#plt.title("Simple Plot")
#plt.show()
#plt.savefig('test.png', dpi=300)
#plt.savefig('test', format='png', dpi=300)
#plt.close()

