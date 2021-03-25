import cv2
import numpy as np

img = cv2.imread('multi03.png')
#cv2.imshow('Original', img)

img = cv2.resize(img, (img.shape[1]//2, img.shape[0]//2), interpolation=cv2.INTER_CUBIC)
#cv2.imshow('Original', img)
print(img.shape)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', gray)
print(gray.shape)

# canny
canny = cv2.Canny(gray, 125,175)
cv2.imshow('Canny', canny)

#find contours from canny
contours, hierarchies = cv2.findContours(canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
print(f'{len(contours)} contours found!')

'''
# or find contours from threshold
ret, thresh = cv2.threshold(gray, 125, 255, cv2.THRESH_BINARY)
contours, hierarchies = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
print(f'{len(contours)} contours found!')
cv2.imshow('Threshold', thresh)
'''
blank = np.zeros(img.shape, dtype='uint8')
#cv2.imshow('Blank',blank)
print(blank.shape)

cv2.drawContours(blank, contours, -1, (0,0,255), 1)
cv2.imshow('Contours drawn',blank)

cv2.waitKey(0)