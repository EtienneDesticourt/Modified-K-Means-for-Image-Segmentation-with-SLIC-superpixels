'''
Created on Nov 10, 2014
@author: Etienne
'''

from ImageProcessor import ImageProcessor
from Segmenter import Segmenter
import matplotlib.pyplot as plt


IP = ImageProcessor()
imgSpace = IP.process("5.jpg")
S = Segmenter()
K = 30 #number of clusters
errorThreshold = 0.0000001
clusters = S.segment(K, imgSpace, errorThreshold)

superPixels = []
for k in xrange(K):
    superPixel = imgSpace[clusters==k]
    superPixels.append(superPixel)
#     print superPixel.shape
    rgb = (1.0/(K))*(K-k)
#     print rgb
    plt.plot(superPixel[:,3],superPixel[:,4], color=(1-rgb,0,rgb))



# plt.axis([0,640,0,480])
plt.show()