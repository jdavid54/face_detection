import cv2
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')

#cv2.imshow('Blank',blank)

# paint it with color
#blank[:] = 0,0,255
#cv2.imshow('Color',blank)

#rectangle
cv2.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), -1)
#cv2.imshow('Rect',blank)

#circle
cv2.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,255,255), cv2.FILLED)
#cv2.imshow('Circle',blank)

#line
cv2.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255,0,0), 3)
#cv2.imshow('Line',blank)
#text
cv2.putText(blank, 'Text', (300,300), cv2.FONT_HERSHEY_TRIPLEX, 1.0, (255,255,0), 2)
cv2.imshow('Text',blank)


cv2.waitKey(0)