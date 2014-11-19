'''
Created on Nov 16, 2014
@author: Etienne
'''


from ImageProcessor import ImageProcessor
from Segmenter import Segmenter
import matplotlib.pyplot as plt

IP = ImageProcessor()
imgSize = IP.getSize("5.jpg")
imgSpace = IP.process("5.jpg")
# print imgSpace[:766,3:5]
S = Segmenter()
K = 27


#Test pick centers
#Should give S points evenly spaced across the space
gridInterval = S.calcGridInterval(imgSpace.shape, K)
centers = S.pickCenters(K, gridInterval, imgSpace, imgSize)
print centers.shape
# print centers
X = centers[:,3]
Y = centers[:,4]
# print X,Y
plt.plot(X,Y,"rx")
plt.show()
