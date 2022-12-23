import io
import matplotlib.pyplot as plt
import numpy as np

with io.open(r"C:\Users\Rajath\Downloads\altitude.txt", mode="r", encoding="utf-8") as f:
    data = f.read().split(' ')
n = len(data)
dataavg = []

for i in range(0, n-1000, 1000):
    t = 0
    for j in range(1000):
      t += float(data[(i+j)])
    avg = t/100
    dataavg.append(avg)

plt.plot(dataavg,'.')
plt.xlabel('x axis', fontdict = {'fontsize':15})
plt.ylabel('y axis', fontdict = {'fontsize':15})
plt.legend(["altitude vs. x"])
plt.title("Altitude Plot")
plt.show()