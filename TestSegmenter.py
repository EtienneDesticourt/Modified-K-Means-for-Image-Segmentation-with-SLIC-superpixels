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
K = 108


#Test pick centers
#Should give S points evenly spaced across the space
gridInterval = S.calcGridInterval(imgSpace.shape, K)
centers = S.pickCenters(K, gridInterval, imgSpace, imgSize)
print centers.shape


# print centers
X0 = centers[:,3]
Y0 = centers[:,4]
# print X,Y
plt.plot(X0,Y0,"rx")


#Test rectangle extraction
indexes = S.calcRectIndexes(imgSpace, centers[12], gridInterval)
rectangle = imgSpace[indexes]

X1 = rectangle[:,3]
Y1 = rectangle[:,4]
plt.plot(X1,Y1,"bx")
plt.plot(X0,Y0,"rx")

#Test distance calculation
distance = S.calcDistance(gridInterval, rectangle, centers[12])
print rectangle.shape
print distance.shape

#Test clustering
distances = S.calcAllDistances(imgSpace, centers, K, gridInterval)
print distances.shape
print distances[0:10,:]





# plt.show()
