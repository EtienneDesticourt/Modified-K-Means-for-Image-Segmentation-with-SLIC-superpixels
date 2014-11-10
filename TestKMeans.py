'''
Created on Nov 10, 2014
@author: Etienne
'''


import numpy as np
import matplotlib.pyplot as plt
from Classifier import Classifier



X = []

#First blob
for x in xrange(2,6):
    for y in xrange(8,12):
        X.append([x,y])
        
#Second blob
for x in xrange(10,15):
    for y in xrange(2,6):
        X.append([x,y])
        
X = np.array(X)
k = 2

C = Classifier()
for i in xrange(1000):
    clusters = C.clusterize(X, k)

X1 = X[clusters==0]
X2 = X[clusters==1]

plt.plot(X1.T[0],X1.T[1],"ro")
plt.plot(X2.T[0],X2.T[1],"bx")
plt.axis([0,20,0,15])
plt.show()
