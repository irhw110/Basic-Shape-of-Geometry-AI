import cv2 as cv
import numpy as np

class KeyFeatureDetector():

    def __init__(file):
        self._file = file
        self._image = None
        self._image_gray = None

    def readFile():
        self._image = cv2.imread(self.file)
        self._image_gray = cv2.cvtColor(self._image, cv2.COLOR_BGR2GRAY)

        