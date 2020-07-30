# -*- coding: utf-8 -*-

import cv2
import numpy as np

img = cv2.imread('a.jpeg')
dst = 'result.png'

# Gray Scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Enlarge 2x
height, width = gray.shape
gray_enlarge = cv2.resize(gray, (2*width, 2*height), interpolation=cv2.INTER_LINEAR)

# Denoising
denoised = cv2.fastNlMeansDenoising(gray_enlarge, h=10, searchWindowSize=21, templateWindowSize=7)

# Thresholding
gray_pin = 196
ret, thresh = cv2.threshold(denoised, gray_pin, 255, cv2.THRESH_BINARY)

# inverting
thresh[260:2090] = ~thresh[260:2090]

result = np.hstack((gray_enlarge, thresh))

cv2.imwrite(dst, result)