import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,3,100)

fig, ax = plt.subplots()

ax.plot(x,x**2,label="Sqr",marker='x',color='red')
ax.plot(x,x**3,label="Cube",linewidth=3, linestyle='--' )
ax.plot(x,x**x,label="exp of x")

# linestyle '-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted'

ax.legend() 

plt.show()



