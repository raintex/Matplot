from tkinter.font import BOLD
import numpy as np
import matplotlib.pyplot as plt
 
theta = np.linspace( 0 , 2 * np.pi , 5 )
 
r = 10
 
a = r * np.cos( theta )
b = r * np.sin( theta ) 
 
figure, axes = plt.subplots( 1 )
 
axes.plot( a, b )
axes.set_aspect( 1 )
 
plt.title('Circle', fontdict={'fontsize':22, 'fontweight':BOLD})
plt.show()