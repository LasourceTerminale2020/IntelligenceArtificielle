# coding: utf-8
#
# 21/03/2020

import cv2
import numpy as np
import sys
from math import sqrt

# screen center: video resolution divided by 2 
center_X = 1280/2
center_Y = 720/2

# creating cascade for face recognition
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# webcam to capture video
cap = cv2.VideoCapture(0)

while True:

    
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # text caracteristics to dislplay info 
    txt_font = cv2.FONT_HERSHEY_SIMPLEX
    txt_color = (250,250,250)


    for (x,y,w,h) in faces:

        # face center coordinates 
        face_center_X = ((x+w)+x)/2
        face_center_Y = ((y+h)+y)/2

        # display a rectangle on the face and a circle in the center
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.circle(img,(int(face_center_X), int(face_center_Y)), 12, (0,0,250), 1)

        # vector distances:
        DISTANCE_TO_CENTER = sqrt(((center_X - face_center_X)**2)+((center_Y - face_center_Y)**2))
        X_DISTANCE = center_X - face_center_X
        Y_DISTANCE = center_Y - face_center_Y

        # display information about the vectors
        if DISTANCE_TO_CENTER > 60:
            
            if X_DISTANCE > 0:
                cv2.putText(img, "x axis: go left: {}".format(X_DISTANCE), (10,20), txt_font, 1, txt_color, 2 )
            
            elif X_DISTANCE < 0:
                cv2.putText(img, "x axis: go right: {}".format(X_DISTANCE), (10,20), txt_font, 1, txt_color, 2 )
            
            else:
                cv2.putText(img, "x axis: okay: {}".format(X_DISTANCE), (10,20), txt_font, 1, txt_color, 2 )
            
            if Y_DISTANCE > 0:
                cv2.putText (img, "y axis: go down: {}".format(Y_DISTANCE), (10, 50), txt_font, 1, txt_color, 2 )
            
            elif Y_DISTANCE < 0:
                cv2.putText (img, "y axis: go up: {}".format(Y_DISTANCE), (10, 50), txt_font, 1, txt_color, 2 )

            else:
                cv2.putText (img, "y axis: okay: {}".format(Y_DISTANCE), (10, 40), txt_font, 1, txt_color, 2 )
        
        else:
            cv2.putText (img, "OKAY", (10, 40), txt_font, 1, txt_color, 2 )

    cv2.circle(img, (int(center_X), int(center_Y)),12, (250,250,0), 1)
        
    # display image
    cv2.imshow('img',img)
    
    # press escape to stop the program :)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

# close cv2 features
cap.release()
cv2.destroyAllWindows()