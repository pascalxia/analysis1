# Compatibility with Python 3
from __future__ import print_function, division

# Interactive graphs for matplotlib at the IPython prompt
# %matplotlib

# Standard imports of libraries
import numpy as np
import matplotlib.pyplot as plt

pixel_values = np.loadtxt('camera.txt')

M = 512
N = 512

img = pixel_values.reshape(M,N).T

fig1 = plt.figure()
plt.imshow(img, cmap='gray')
plt.show()

fig2 = plt.figure()
plt.plot(img[300,])

thresh = 0.2
fig3 = plt.figure()
plt.imshow(img>thresh, cmap='gray')