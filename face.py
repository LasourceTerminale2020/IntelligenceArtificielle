# coding: utf-8
#
# 21/03/2020

import cv2
import numpy as np
import sys
from math import sqrt

center_X = 1280/2
center_Y = 720/2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)


    for (x,y,w,h) in faces:

        face_center_X = ((x+w)+x)/2
        face_center_Y = ((y+h)+y)/2

        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.circle(img,(int(face_center_X), int(face_center_Y)), 12, (0,0,250), 1)

        if sqrt(((center_X - face_center_X)**2)+((center_Y - face_center_Y)**2)) > 60:
            
            if center_X - face_center_X > 0:
                cv2.putText(img, "x axis: go right", (10,20), cv2.FONT_HERSHEY_SIMPLEX, 1, (250,250,250), 2 )
            
            elif center_X - face_center_X < 0:
                cv2.putText(img, "x axis: go left", (10,20), cv2.FONT_HERSHEY_SIMPLEX, 1, (250,250,250), 2 )
            
            else:
                cv2.putText(img, "x axis: okay", (10,20), cv2.FONT_HERSHEY_SIMPLEX, 1, (250,250,250), 2 )
            
            if center_Y - face_center_Y > 0:
                cv2.putText (img, "y axis: go down", (10, 40),cv2.FONT_HERSHEY_SIMPLEX, 1, (250,250,250), 2 )
            
            elif center_Y - face_center_Y < 0:
                cv2.putText (img, "y axis: go up", (10, 40),cv2.FONT_HERSHEY_SIMPLEX, 1, (250,250,250), 2 )

            else:
                cv2.putText (img, "y axis: okay", (10, 40),cv2.FONT_HERSHEY_SIMPLEX, 1, (250,250,250), 2 )
        
        else:
            cv2.putText (img, "OKAY", (10, 40),cv2.FONT_HERSHEY_SIMPLEX, 1, (250,250,250), 2 )

    cv2.circle(img, (int(center_X), int(center_Y)),12, (250,250,0), 1)
        
        
    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()