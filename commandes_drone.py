# coding: utf-8
#
# 12/03/2020

from djitellopy import tello 
import pygame
import cv2

drone = Tello()
drone.connect()

print(drone.get_battery())

drone.streamoff()
drone.streamon()


drone.takeoff()

pygame.init()


vel=10

print(drone.get_battery())

drone.streamoff()
drone.streamon()

run= True

while run:

    frame_read = drone.get_frame_read()
    myFrame = frame_read.frame

    cv2.imshow("MyResult", myFrame)

    keys= pygame.key.get_pressed()
    
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break    
    
    if keys [pygame.K_LEFT]:
        drone.send_rc_control(-vel, 0, 0, 0)

    if keys [pygame.K_RIGHT]:
        drone.send_rc_control(vel, 0, 0, 0)
    
    if keys [pygame.K_UP]:
        drone.send_rc_control(0, vel, 0, 0)

    if keys[pygame.K_DOWN]:
        drone.send_rc_control(0, -vel, 0, 0)

    if keys [pygame.K_z]:
        drone.send_rc_control(0, 0, vel, 0)

    if keys [pygame.K_s]:
        drone.send_rc_control(0, 0, -vel, 0)

    if keys [pygame.K_q]:
        drone.send_rc_control(0, 0, 0, -vel)
    
    if keys [pygame.K_d]:
        drone.send_rc_control(0, 0, 0, vel)


my_drone.land()

cap.release()
cv2.destroyAllWindows()

quit()
