# https://opencv.org/
# https://www.youtube.com/watch?v=R7B8sSByZGQ

import cv2

trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def show(img):
    cv2.imshow('Detector', img)
    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        exit = True


webcam = cv2.VideoCapture(0)

exit = False
while True:
    successful_frame_read, frame = webcam.read()
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #show(grayscaled_img)

    # detect faces
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)
    # box coordinates that contains the face 
    #print(face_coordinates)

    #cv2.rectangle(img, (155, 158), (124, 124),(0,255,0),2)
    for (x,y,w,h) in face_coordinates:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0),2)
    #cv2.rectangle(img, face_coordinates, (0,255,0),2)
    cv2.imshow('Detector', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

print('Code completed')
