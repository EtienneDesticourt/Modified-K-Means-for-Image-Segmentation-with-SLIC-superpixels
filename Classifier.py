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
        mini = min(X)
        maxi = max(X)
        for i in xrange(k):
            means.append( random.randrange(mini,maxi) )
        return np.array(means)
    def calcMean(self,X):
        return sum(X)/len(X)
    def clusterize(self,X,k):
        means = self.pickMeans(X,k)
        lastMeans = means.copy()
        
        while means == lastMeans:
            distances = []
            for i in xrange(k):
                distance = np.linalg.norm(X - means[i],axis=1)
                distances.append( distance )
            distances = np.column_stack(distances)
            clusters = distances.argmin(axis=1)
            