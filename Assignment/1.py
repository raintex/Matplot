import matplotlib.pyplot as plt
import numpy as np
from tkinter.font import BOLD

# Plotting y = x^4 * e^-2x

x = np.linspace(0, 50, 1000)
y = ((x * x * x * x) * np.exp(-2 * x))

plt.plot(x, y)
plt.xlim([0, 50])
plt.xlabel('x axis', fontdict = {'fontsize':15})
plt.ylabel('y axis', fontdict = {'fontsize':15})
plt.legend(["y vs. x"])
plt.title("$ y(x) = x^4.e^{-2x} $", fontdict = {'fontsize':15})

plt.show()