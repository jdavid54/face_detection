import cv2
import numpy as np

img = cv2.imread('multi03.png')
print(img.shape)
cv2.imshow('Group', img)
cropped = img[200:350, 150:750]  #xtop,xbottom, yleft,yright

resized = cv2.resize(img, (img.shape[1]//2, img.shape[0]//2), interpolation=cv2.INTER_CUBIC)
img = resized
img = cropped
cv2.imshow('Group cropped', cropped)

# gray
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Group in gray', gray)

#blur
blur = cv2.GaussianBlur(img, (7,7), cv2.BORDER_DEFAULT)  # kernel must be odd number
cv2.imshow('Group blur', blur)

# canny
canny = cv2.Canny(img, 125,175)
cv2.imshow('Group in canny', canny)
# canny fropm blur
cannyblur = cv2.Canny(blur, 125,175)
cv2.imshow('Group in cannyblur', cannyblur)

#dilate edges
dilated = cv2.dilate(cannyblur, (7,7), iterations=3)
cv2.imshow('Group in cannyblur dilated', dilated)
# eroded
eroded = cv2.dilate(cannyblur, (7,7), iterations=3)
cv2.imshow('Group in cannyblur eroded', eroded)


cv2.waitKey(0)