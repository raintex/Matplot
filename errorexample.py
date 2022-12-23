import numpy as np
import matplotlib.pyplot as plt

# Dataset generation

x = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J')
y = [989.7, 980, 985.9, 978.2, 993.6, 973, 979, 976.1, 986.1, 1000]

x_pos = np.arange(len(x))

y_error = 0.01374

fig = plt.figure(figsize=(10, 5))
#Bar plot

plt.bar(x, y, color='green', width=0.5)
plt.xlabel("Resistor 1 to 10")
plt.ylabel("Average values of resistances ")
plt.title("Error bar")
plt.show()
