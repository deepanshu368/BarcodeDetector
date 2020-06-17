import numpy as np
import argparse
import imutils
import cv2

def detector(img):
    image = cv2.imread(img)
    gray_scale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    max_val = float('-inf')

    for angle in np.arange(0, 360, 45):
        gray = imutils.rotate(gray_scale, angle)

        ddepth = cv2.cv.CV_32F if imutils.is_cv2() else cv2.CV_32F
        gradX = cv2.Sobel(gray, ddepth=ddepth, dx=1, dy=0, ksize=-1)
        gradY = cv2.Sobel(gray, ddepth=ddepth, dx=0, dy=1, ksize=-1)

        gradient = cv2.subtract(gradX, gradY)
        gradient = cv2.convertScaleAbs(gradient)

        blurred = cv2.blur(gradient, (3, 3))

        if (blurred.sum() > max_val):
            max_val = blurred.sum()
            best_blurred = blurred
            best_angle = angle


    (_, thresh) = cv2.threshold(best_blurred, 225, 255, cv2.THRESH_BINARY)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (35, 35))

    closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    closed = cv2.erode(closed, None, iterations = 4)
    closed = cv2.dilate(closed, None, iterations = 4)

    cnts = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    image = imutils.rotate(image, best_angle)

    list_of_boxes = []
    
    for ct in cnts:
        if (cv2.contourArea(ct) <= 2000):
            continue

        rect = cv2.minAreaRect(ct)
        box = cv2.cv.BoxPoints(rect) if imutils.is_cv2() else cv2.boxPoints(rect)
        box = np.int0(box)

        cv2.drawContours(image, [box], -1, (0, 255, 0), 3)
        minX = box[0][0]
        maxX = box[2][0]
        minY = box[1][1]
        maxY = box[0][1]
        list_of_boxes.append([minX, maxX, minY, maxY])

    return list_of_boxes