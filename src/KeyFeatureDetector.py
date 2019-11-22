import cv2 as cv
import numpy as np
import math

class KeyFeatureDetector():

    def __init__(self,file):
        self._file = file
        self._image = None
        self._image_gray = None
        self._corners = np.array(list())
        self._angle = np.array(list())

    def readFile(self):
        self._image = cv.imread(self._file)
        self._image_gray = cv.cvtColor(self._image, cv.COLOR_BGR2GRAY)

    def detectCorner(self):
        if(True):
            ret,thresh = cv.threshold(self._image_gray,150,255,cv.THRESH_BINARY)
            contours, hierarchy = cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)

            contour = contours[0]
            size = cv.contourArea(contour)
            rect = cv.minAreaRect(contour)

            peri = cv.arcLength(contour, True)
            self._corners = cv.approxPolyDP(contour, 0.001 * peri, True)
            self._image = cv.drawContours(self._image, [self._corners], 0, (0,255,0), 3)
            
            for i in range(0,self._corners.shape[0]):

                vA = self._corners[i] - self._corners[(i-1)%self._corners.shape[0]]
                vB = self._corners[i] - self._corners[(i+1)%self._corners.shape[0]]

                dotProduct = vA[0].dot(vB[0])
                magVA = np.linalg.norm(vA[0])
                magVB = np.linalg.norm(vB[0])
                
                angleMag = math.degrees(np.arccos(dotProduct/(magVA*magVB)))
                self._angle = np.append(self._angle,angleMag)

            
    
    def showImage(self):
            print(self._corners)
            print(self._angle)
            cv.imshow('image', self._image)
            cv.waitKey(0)
            cv.destroyAllWindows

if __name__ == "__main__":
    Detector = KeyFeatureDetector('shapes/square.png')
    Detector.readFile()
    Detector.detectCorner()
    Detector.showImage()