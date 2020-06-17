import cv2
import numpy as np

def detector(filename):
    img = cv2.imread(filename)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    distance = cv2.cornerHarris(img_gray, 2, 3, 0.04)

    distance = cv2.dilate(distance, None)

    threshold = 0.02 * distance.max()

    img[distance > threshold] = [0, 0, 255]
    cv2.imshow('img', img)
    
    cv2.waitKey(0)


detector('IMG_5171.JPG')
