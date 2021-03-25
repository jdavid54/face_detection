# https://opencv.org/
# https://www.youtube.com/watch?v=R7B8sSByZGQ

import cv2

trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def show(img):
    cv2.imshow('Detector', img)
    cv2.waitKey()

pix = 'phong_beo.jpg'
pix = 'lincoln.jpeg'
pix = 'marilyn.jpeg'
pix = 'girl16.jpeg'
#pix = 'obama2.jpeg'
#pix = 'kahlo.jpeg'
#pix = 'trump.jpeg'
#pix = 'guy04.jpeg'
#pix = 'ford.jpeg'
#pix = 'woman02.jpeg'
#pix = 'baby01.jpeg'
#pix = 'multi02.jpeg'
pix = 'qazi_aaron3.png'
pix = 'multi03.png'
#pix = 'phong_beo.jpg'


img = cv2.imread(pix)
show(img)

# make it gray
grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
show(grayscaled_img)

# detect faces
face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)
# box coordinates that contains the face 
print(face_coordinates)

#cv2.rectangle(img, (155, 158), (124, 124),(0,255,0),2)
for (x,y,w,h) in face_coordinates:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0),2)
#cv2.rectangle(img, face_coordinates, (0,255,0),2)
show(img)
print('Code completed')
