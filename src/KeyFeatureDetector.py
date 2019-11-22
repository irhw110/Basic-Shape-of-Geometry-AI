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

            gray = np.float32(self._image_gray)
            mask = np.zeros(gray.shape, dtype="uint8")
            cv.fillPoly(mask, [contour], (255,255,255))
            dst = cv.cornerHarris(mask,5,3,0.04)
            ret, dst = cv.threshold(dst,0.1*dst.max(),255,0)
            dst = np.uint8(dst)
            ret, labels, stats, centroids = cv.connectedComponentsWithStats(dst)
            criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 100, 0.001)
            corners = cv.cornerSubPix(gray,np.float32(centroids),(5,5),(-1,-1),criteria)

            for i in range(1, len(corners)):
                print(corners[i])

            self._image[dst>0.1*dst.max()]=[0,0,255]
            cv.imshow('image', self._image)
            cv.waitKey(0)
            cv.destroyAllWindows

if __name__ == "__main__":
    Detector = KeyFeatureDetector('../shapes/segilima_beraturan.png')
    Detector.readFile()
    Detector.detectCorner()