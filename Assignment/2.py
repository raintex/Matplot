
import matplotlib.pyplot as plt
import numpy as np
from tkinter.font import BOLD

# Plotting y = sin(x), y = cos(x), y = tan(x)

x = np.linspace(-15, 15, 1000)
a = np.sin(x)
b = np.cos(x)
c = np.tan(x)

plt.plot(x,a)
plt.plot(x,b)
plt.plot(x,c)
plt.ylim([-3, 3])
plt.xlim([-10, 10])
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend(["sin", "cos", "tan"])
plt.title(r'$y = \mathrm{sin}(x), y = \mathrm{cos}(x), y = \mathrm{tan}(x)$', fontdict = {'fontsize':15})

plt.show()