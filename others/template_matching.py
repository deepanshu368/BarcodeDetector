import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("IMG_5171.JPG")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

template_barcode = cv2.imread("UPCImage300.jpg", 0)

w, h = template_barcode.shape[::-1]

res = cv2.matchTemplate(img_gray, template_barcode, cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where(res >= threshold)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)


cv2.imshow("img", img)

cv2.waitKey(0)

