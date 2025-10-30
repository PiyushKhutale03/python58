import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints)
plt.show()

#Marker
y1points = np.array([3, 8, 1, 10])

plt.plot(y1points, marker = 'o')
plt.show()