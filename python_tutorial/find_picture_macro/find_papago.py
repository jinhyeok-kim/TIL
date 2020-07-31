import pyautogui as pag
from PIL import Image
import pytesseract, keyboard
import path
from cv2 import *

pag.FAILSAFE = False
pytesseract.pytesseract.tesseract_cmd = path.tesseract_path

checkX = 0
checkY = 0

# papago = pag.locateOnScreen('abc.png')

# print(papago)
papago = pag.locateOnScreen('abc.png', grayscale=True, confidence=0.4)
print(papago)
 
pag.moveTo(papago.left, papago.top)

# while True:  # making a loop
#     try:  # used try so that if user pressed other than the given key error will not be shown
#         if keyboard.is_pressed('q'):  # if key 'q' is pressed 
#             print('You Pressed A Key!')
#             break  # finishing the loop
#         else:
#             papago = pag.locateOnScreen('abc.png', confidence=0.5)
#             print(papago)

#             startX = papago.left
#             startY = papago.top+191

#             print(startX)
#             print(startY)

#             if checkX != startX and checkY != startY:
#                 pag.screenshot('abcddd.png', region=(startX, startY, 870, 270))
#                 print(pytesseract.image_to_string(Image.open('abcddd.png')))
#                 checkX = startX
#                 checkY = startY
#             pass
#     except:
#         break  # if user pressed a key other than the given key the loop will break






# im2 = pag.screenshot();


# temp = pytesseract.image_to_string(im2)
# temp = pytesseract.image_to_string(Image.open('abcddd.png'))
# print(pytesseract.image_to_string(Image.open('abcddd.png'), lang='kor'))

# print(temp.splitlines())
# pag.moveTo(papago.left, papago.top+191)
# pag.moveTo(papago.left + 847, papago.top+191 +267)
# pag.moveTo(i)
# pag.click(i);