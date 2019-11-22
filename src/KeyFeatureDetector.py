import cv2 as cv
import numpy as np

class KeyFeatureDetector():

    def __init__(self,file):
        self._file = file
        self._image = None
        self._image_gray = None
        self._corners = []

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
            approx = cv.approxPolyDP(contour, 0.001 * peri, True)
            self._image = cv.drawContours(self._image, [approx], 0, (0,255,0), 3)
            
            print(approx)
            
    
    def showImage(self):
            cv.imshow('image', self._image)
            cv.waitKey(0)
            cv.destroyAllWindows

if __name__ == "__main__":
    Detector = KeyFeatureDetector('shapes/segitiga_lancip.png')
    Detector.readFile()
    Detector.detectCorner()
    Detector.showImage()