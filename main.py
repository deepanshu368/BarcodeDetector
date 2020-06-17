from decode import decode
from webscraping import getInfo
from detector import detector
import cv2
import sys


def main():
    img_file = sys.argv[1]
    img = cv2.imread(img_file)
    list_of_boxes = detector(img_file)
    result = open("result.txt", 'w')

    for box in list_of_boxes:
        target_img = img[box[0]:box[1]][box[2]:box[3]]
        barcode = decode(target_img)
        data = getInfo(barcode)
        result.write(str(data) + '\n')


if __name__ == "__main__":
    main()
