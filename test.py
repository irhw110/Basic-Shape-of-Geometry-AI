import cv2
import numpy as np


img = cv2.imread('shapes/segilima_beraturan.png')
img2 = cv2.imread('shapes/segilima_beraturan.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(gray,150,255,cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)


for i in contours:
    img = cv2.imread('shapes/segilima_beraturan.png')
    
    size = cv2.contourArea(i)
    print(size)
    rect = cv2.minAreaRect(i)
    print(rect)
    if size <200000:
        gray = np.float32(gray)
        mask = np.zeros(gray.shape, dtype="uint8")
        cv2.fillPoly(mask, [i], (255,255,255))
        dst = cv2.cornerHarris(mask,5,3,0.04)
        ret, dst = cv2.threshold(dst,0.1*dst.max(),255,0)
        dst = np.uint8(dst)
        ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst)
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
        corners = cv2.cornerSubPix(gray,np.float32(centroids),(5,5),(-1,-1),criteria)
        
        if rect[2] == 0 and len(corners) == 5:
            x,y,w,h = cv2.boundingRect(i)
            if w == h or w == h +3: #Just for the sake of example
                print('Square corners: ')
                for i in range(1, len(corners)):
                    print(corners[i])
            else:
                print('Rectangle corners: ')
                for i in range(1, len(corners)):
                    print(corners[i])
        if len(corners) == 5 and rect[2] != 0:
            print('Rombus corners: ')
            for i in range(1, len(corners)):
                print(corners[i])
        if len(corners) == 4:
            print('Triangle corners: ')
            for i in range(1, len(corners)):
                print(corners[i])
        if len(corners) == 6:
            print('Pentagon corners: ')
            for i in range(1, len(corners)):
                print(corners[i])

        img[dst>0.1*dst.max()]=[0,0,255]
        cv2.imshow('image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows