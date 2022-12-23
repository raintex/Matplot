import matplotlib.pyplot as plt
import numpy as np
from tkinter.font import BOLD

t = input('Enter the required orbital time period in hours: ')

h = ((((6.67 * (10 ** -11)) * (5.97 * (10 ** 24)) * (float(t) * float(t) * 3600 * 3600)) / (4 * 3.14 * 3.14))**(1/3)) - 6371000
print('Altitude required for T = ',t,' would be ',h,'m')

t = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
hl = []
for i in range(20):
    hl.append(int(((((6.67 * (10 ** -11)) * (5.97 * (10 ** 24)) * (float(t[i]) * float(t[i]) * 3600 * 3600)) / (4 * 3.14 * 3.14))**(1/3)) - 6371000))

print(hl)

plt.plot(t, hl)
plt.xlabel('Time period', fontdict = {'fontsize':15})
plt.ylabel('Altitude', fontdict = {'fontsize':15})
plt.legend(["Altitude"])
plt.title("Altitude vs Time Period graph", fontdict = {'fontsize':15})

plt.show()

