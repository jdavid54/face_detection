import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread('multi03.png')
#cv2.imshow('Original', img)
img = cv2.resize(img, (img.shape[1]//2, img.shape[0]//2), interpolation=cv2.INTER_CUBIC)

#plt.imshow(img)  # show in RGB colors an image in BGR
#plt.show()

#gray
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', gray)

#hsv
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('HSV', hsv)

#lab
lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
cv2.imshow('LAB', lab)

rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow('RGB',rgb)

plt.imshow(rgb)
#plt.show()





cv2.waitKey(0)
