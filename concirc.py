from tkinter.font import BOLD
import numpy as np
import matplotlib.pyplot as plt
 
theta = np.arange( 0 , 2 * np.pi , 0.001 )
 
r = 1
for i in range(20) :
    a = r * np.cos( theta )
    b = r * np.sin( theta ) 
 
    plt.plot(a,b)
    plt.axis('square')
    r = r + 1  
 
plt.title('Concentric Circles', fontdict={'fontsize':22, 'fontweight':BOLD})
plt.show()
