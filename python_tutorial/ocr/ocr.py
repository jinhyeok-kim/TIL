from PIL import Image
import pytesseract, keyboard
import path
import os

pytesseract.pytesseract.tesseract_cmd = path.tesseract_path

# print(pytesseract.image_to_string(Image.open('ab.jpeg')))

config = ('-l eng --oem 1 --psm 3')

im = cv2.imread('ab.jpeg', cv2.IMREAD_COLOR)

# print(pytesseract.image_to_string(im, config= config))