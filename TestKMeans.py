'''
Created on Nov 10, 2014
@author: Etienne
'''


import numpy as np
import matplotlib.pyplot as plt




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


plt.plot(X.T[0],X.T[1],"ro")
plt.axis([0,20,0,15])
plt.show()
