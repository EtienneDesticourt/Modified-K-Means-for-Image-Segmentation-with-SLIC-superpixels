
from skimage import io,color
import numpy as np

class ImageProcessor:
    def __init__(self):
        pass
    def process(self, path):
        rgbImg = io.imread(path)
        io.show()
        labImg = color.rgb2lab(rgbImg)
#         Viewer = ImageViewer(rgbImg)
#         Viewer.show()
        #broadcast image into 5D space
        width = labImg.shape[0]
        height = labImg.shape[1]
        newSpace = np.vstack(labImg) # gives us a (width*height, 3) array
        X = np.linspace(0,width,width*height)# for each X coordinate there are #height Y coordinates
        X = np.rint(X) # so we distribute those #width X coords linearly incrementing by one each #heightth element
        Y = np.tile( np.arange(height),width ) #Y is simply 0 to #height repeated #width times
        coordVects = np.vstack( (X,Y) ).T
        newSpace = np.hstack( (newSpace,coordVects) ) # (width*height, 5) array
        print labImg.shape
        print newSpace.shape
        return newSpace

