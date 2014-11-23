'''
Created on Nov 10, 2014
@author: Etienne
'''

from ImageProcessor import ImageProcessor
from Segmenter import Segmenter
import matplotlib.pyplot as plt
import numpy as np

path = "lena.bmp"

#Read and process image
IP = ImageProcessor()
img = IP.getImg(path)/256.
imgSize = IP.getSize(path)
imgSpace = IP.process(path)


#Segment image
S = Segmenter()
K = 300 #number of clusters
errorThreshold = 0.01
clusters = S.segment(K, imgSpace, imgSize, errorThreshold)

#Get back clusters into image shape
width, height = imgSize[0],imgSize[1]
clusters = np.flipud(clusters.reshape((width,height)))


#Plot image
#http://stackoverflow.com/questions/15822934/matplotlib-imshow-how-to-plot-points-instead-of-image
# Reduce the data by a factor of 4 (so that we can see the points)
im = img
# generate coordinates for the image. Note that the image is "top down", so the y coordinate goes from high to low.
ys, xs = np.mgrid[im.shape[0]:0:-1, 0:im.shape[1]]
# Scatter plots take 1d arrays of xs and ys, and the colour takes a 2d array,
# with the second dimension being RGB
plt.scatter(xs.flatten(), ys.flatten(), s=4, c=im.flatten().reshape(-1, 3), edgecolor='face')

#Plot Clusters
x = np.linspace(0,width,width)
y = np.linspace(0,height,height)
Xm,Ym = np.meshgrid(y,x)
# c =  plt.contourf(Xm, Ym,clusters, K, cmap='jet')
cont = plt.contour(Xm, Ym, clusters, K, colors='black', linewidth=.5)


plt.show()