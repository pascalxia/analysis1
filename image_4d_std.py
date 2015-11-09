# Compatibility with Python 3
from __future__ import print_function, division

# Standard imports of libraries
import numpy as np
import matplotlib.pyplot as plt
import nibabel as nib

# Interactive graphs for matplotlib at the IPython prompt
plt.ion()

# Load image object using nibabe
img = nib.load('ds114_sub009_t2r1.nii')

# Get image array data from image object
data = img.get_data()
data.shape

# Get the 1st volume and show shape
v1 = data[..., 0]
v1.shape

# Matplotlib display of the center slice, slicing over the 3rd dimension
plt.figure()
plt.imshow(v1[..., 15], cmap='gray')

# Standard deviation across all voxels for 1st volume
np.std(v1)

# Get the second 3D volume.
# Show the central slice (over the 3rd dimension).
# Get the standard deviation across all voxels
v2 = data[..., 1]
v2.shape
plt.figure()
plt.imshow(v2[..., 15], cmap='gray')
np.std(v2)

# Get the third 3D volume.
# Show the central slice (over the 3rd dimension).
# Get the standard deviation across all voxels
v3 = data[..., 1]
v3.shape
plt.figure()
plt.imshow(v3[..., 15], cmap='gray')
np.std(v3)

# Get standard deviation for each volume; then plot the values
sdList = [data[...,i].std() for i in range(data.shape[3])]
plt.figure()
plt.plot(sdList)

plt.figure()
plt.plot(sdList[1:])