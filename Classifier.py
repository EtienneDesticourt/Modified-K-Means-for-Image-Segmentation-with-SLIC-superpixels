'''
Created on Nov 10, 2014
@author: Etienne
Basic K-Means implementation.
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
            length = len(X[clusters==i]) or 1
            means.append( sum(X[clusters==i])/length )
        return np.array( means )
    def clusterize(self,X,k):
        means = self.pickMeans(X,k)
        lastMeans = np.zeros(means.shape)
        try:
            while not np.equal(means,lastMeans).all():
                lastMeans = means
                distances = []
                for i in xrange(k):
                    distance = np.linalg.norm(X - means[i],axis=1) #returns float vector
                    distances.append(distance)
                distances = np.column_stack(distances)  #stack vectors horizontally              
                clusters = distances.argmin(axis=1) #returns vector of indexes of smallest column element
                means = self.calcMeans(X,clusters,k)
        except ValueError, e:
            print "Error"
            print means
            print lastMeans
            print clusters
            print "-----------------------"      
        #Each element of the clusters vector correspond with the index of the cluster
        return clusters
            
            
            