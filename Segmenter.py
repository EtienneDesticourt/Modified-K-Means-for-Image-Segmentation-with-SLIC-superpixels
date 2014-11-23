'''
Created on Nov 10, 2014
@author: Etienne
SLIC implementation (modified K-Means). 
'''

from math import sqrt
import numpy as np


class Segmenter:
    def __init__(self):
        pass
    
    def calcGridInterval(self, spaceShape, K):        
        N = spaceShape[0] # spaceShape : (width*height, len(labxy))
        S = sqrt(N/K) #gridInterval
        return S
    
    
    def pickCenters(self, K, S, imgSpace, imgSize):
        centers = []
        rangeX = int(round(imgSize[0]/S))
        rangeY = int(round(imgSize[1]/S))
        S = int(S)
        for x in xrange( rangeX ):
            for y in xrange( rangeY ):
                index = y*S + x*imgSize[1]*S
                centers.append(imgSpace[index])
        return np.array(centers)
    def calcMeans(self, imgSpace, clusters, K):
        means = []
        for i in xrange(K):
            length = len(imgSpace[clusters==i]) or 1
            average = sum(imgSpace[clusters==i])/length #Center doesn't actually have to be in imgSpace so it's alrigt to do labxy average
            means.append( average ) 
        return np.array( means )
    
    
    def calcDistance(self, gridInterval, rectangle, center, compactness=10.):
        #We're going to calc the norm of this difference
        dif = rectangle - center
        lab = dif[:,0:3]
        xy = dif[:,3:5]
        
        dLAB = np.linalg.norm(lab, axis=1)
        dXY = np.linalg.norm(xy, axis=1)
        dFinal = dLAB + (compactness/gridInterval)*dXY
        return dFinal
    def reshapeDistance(self, distance, indexes, imgShape):
        #We calculated the distance for a single rectangle in the image
        #We want the distance vector to be imgSpace shaped to compare it 
        #to the distances of other rectangles easily (some rectangles will overlap)
        rows = imgShape[0]
        fullDist = np.zeros(rows)
        #Fill indexes corresponding with rectangle with corresponding distances
        fullDist[indexes] = distance
        #Fill rest with huge value so corresponding clusters will never be chosen by argmin
        fullDist[np.invert(indexes)] = 100000000. #TODO set value depending on imgShape
        return fullDist
    def calcAllDistances(self, imgSpace, centers, K, S):
        distances = []
        for k in xrange(K):
            center = centers[k]            
            indexes = self.calcRectIndexes(imgSpace, center, S)
            rectangle = imgSpace[indexes]
            #Calc distance of rectangle from center
            distance = self.calcDistance(S, rectangle, center)
            distance = self.reshapeDistance(distance, indexes, imgSpace.shape)#set distance to the shape of imgSpace
            #Add distance to rest for comparison
            distances.append(distance)
        distances = np.column_stack(distances)
        return distances
    
    
    def calcRectIndexes(self, imgSpace, center, S):
        #get 2S*2S rectangle coords around center
        x0,y0 = center[3:5] - S #3-5 : x,y
        x1,y1 = center[3:5] + S
        #Extract rectangle
        xRange = np.logical_and( imgSpace[:,3] >= x0,
                                 imgSpace[:,3] < x1)
        yRange = np.logical_and( imgSpace[:,4] >= y0,
                                 imgSpace[:,4] < y1)
        indexes = np.logical_and(xRange,yRange)
        return indexes
    
    
    def segment(self, K, imgSpace, imgSize, errorThreshold):
        #imgSpace is rows of l,a,b,x,y
        S = self.calcGridInterval(imgSpace.shape, K)
        centers = self.pickCenters(K, S, imgSpace, imgSize)
        if centers.shape[0] != K: #Because of the way we calculate S and then pick the first centers
            K = centers.shape[0]  #We can't always pick the appropriate number of clusters
            print "Number of clusters changed to fit grid interval constraints, new K:",K
             
        error = errorThreshold+1
        while error>errorThreshold:            
            distances = self.calcAllDistances(imgSpace, centers, K, S)
            
            clusters = distances.argmin(axis=1)
            newCenters = self.calcMeans(imgSpace, clusters, K)
            #Paper says l1 distance, but we'll do the sum of the l1 distances and set our distance as a number rather than an array
            error = sum( sum( abs(newCenters - centers)[3:5] ) ) 
            print error
            centers = newCenters
            
        return clusters
        
    def enforceConnectivity(self, imgSpace, K, clusters):
        pass
            
            
            
            
            