from djitellopy import Tello
import cv2
import keyboard
import pygame

running = True

width = 320
height = 240

drone = Tello()
drone.connect()

drone.streamoff()
drone.streamon()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    frame_read = drone.get_frame_read()
    myFrame = frame_read.frame
#    img = cv2.resize(myFrame, (width, height))

    cv2.imshow("MyResult", myFrame)

    if keyboard
