import cv2
import numpy as np

img = cv2.imread('multi03.png')
cv2.imshow('Original', img)

def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv2.warpAffine(img, transMat, dimensions)

def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2, height//2)
        print(rotPoint)
    rotMat = cv2.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)    
    return cv2.warpAffine(img, rotMat, dimensions)

translated = translate(img, 100, 100)
cv2.imshow('Translated', translated)

rotated = rotate(img, 45)
cv2.imshow('Rotated', rotated)

# resizing
(height, width) = img.shape[:2]
resized = cv2.resize(img, (width//2, height//2), interpolation=cv2.INTER_CUBIC)
cv2.imshow('Resized', resized)

#flip
flip = cv2.flip(img, 1) #0 : vertically, 1: horizontally, -1:hor+vert
cv2.imshow('Flip', flip)

# cropping
cropped = img[200:350, 150:750]  #xtop,xbottom, yleft,yright
cv2.imshow('Cropped', cropped)

cv2.waitKey(0)