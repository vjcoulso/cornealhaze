from skimage import io
import numpy as np
import matplotlib.pyplot as plt
import sys


with open(sys.argv[1], 'r') as im1:
	im1 = io.imread('movie.tif')
	y = []
	for i in range(im1.shape[0]):
    		y.append(im1[i,:,:].mean())

x = [*range(0, im1.shape[0], 1)]
np.savetxt('filename', np.vstack((x,y)).T, delimiter=', ')
plt.plot(x,y)
plt.savefig('haze.png')