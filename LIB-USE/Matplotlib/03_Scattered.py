import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,3,100)

fig, ax = plt.subplots()

ax.scatter(x,x**2,label="Sqr",s=10,marker='v', facecolor='C1', edgecolor='k')
# ax.plot(x,'v')

ax.legend() 

plt.show()



