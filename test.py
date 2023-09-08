import cv2
import os
import pytesseract
from PIL import Image


IMG = 'test2.png'


def read_image():
    text = pytesseract.image_to_string(IMG, lang='eng')
    print(text)


def read_image_grayscale():
    image = cv2.imread(IMG)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # cv2.threshold(gray, 0,255,cv2.THRESH_BINARY| cv2.THRESH_OTSU)[1]
    cv2.medianBlur(gray, 3)

    filename = f"{IMG}_gray.jpg"
    cv2.imwrite(filename, gray)
    text = pytesseract.image_to_string(Image.open(filename), lang='eng')
    os.remove(filename)
    print(text)

    # cv2.imshow("Image Input", image)
    # cv2.imshow("Output In Grayscale", gray)
    # cv2.waitKey(0)


read_image()
print('-' * 30)
# read_image_grayscale()