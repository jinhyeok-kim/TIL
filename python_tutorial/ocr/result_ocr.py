from PIL import Image
import pytesseract, keyboard
import path
import os
import path

pytesseract.pytesseract.tesseract_cmd = path.tesseract_path
config = ('-l eng --oem 1 --psm 3')

print(pytesseract.image_to_string(Image.open('result.png'), config= config))