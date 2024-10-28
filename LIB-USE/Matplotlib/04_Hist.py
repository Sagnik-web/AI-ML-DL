import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,3,100)

fig, ax = plt.subplots()

n_bins = 20

ax.hist(x, bins=n_bins)

plt.show()



