from tkinter.font import BOLD
import matplotlib.pyplot as plt
import numpy as np
import math

x = np.linspace(-math.pi, math.pi, 100)
plt.plot(x, (np.sin(x)*np.sin(x))/x, 'g.') 
#plt.axis('square')
plt.title('$sin^2(x)/x$', fontdict={'fontsize':22, 'fontweight':BOLD})
plt.show()