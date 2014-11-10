'''
Created on Nov 10, 2014
@author: Etienne
'''

import random
import numpy as np

class Classifier:
    def __init__(self):
        pass
    def pickMeans(self,X,k):
        means = []
        mini = X.min(axis = 0)
        maxi = X.max(axis = 0)
        for i in xrange(k):
            randX = random.randrange(mini[0],maxi[0])
            randY = random.randrange(mini[1],maxi[1])
            means.append(  [randX,randY]  )
        return np.array(means)
    def calcMeans(self,X,clusters,k):
        means = []
        for i in xrange(k):
            length = len(X) or 1
            means.append( sum(X[clusters==i])/length )
        return np.array( means )
    def clusterize(self,X,k):
        means = self.pickMeans(X,k)
        lastMeans = np.zeros(means.shape)
        c = 0
        print means, lastMeans
        while not np.equal(means,lastMeans).all():
            c += 1
            print c
            lastMeans = means
            distances = []
            for i in xrange(k):
                distance = np.linalg.norm(X - means[i],axis=1)
                distances.append( distance )
            distances = np.column_stack(distances)
            clusters = distances.argmin(axis=1)
            means = self.calcMeans(X,clusters,k)
            
        return clusters
            
            
            