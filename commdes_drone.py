from easytello import tello 
import pygame
my_drone = tello.Tello()
my_drone.takeoff()

pygame.init()


vel=10


run= True

while run:

    keys= pygame.key.get_pressed()
    
    if keys [pygame.K_T]:
        run= False
    
    if keys [pygame.K_LEFT]:
        my_drone.left(vel)

    if keys [pygame.K_RIGHT]:
        my_drone.right(vel)
    
    if keys [pygame.K_UP]:
        my_drone.forward(vel)

    if keys[pygame.K_DOWN]:
        my_drone.back(vel)

    if keys [pygame.K_Z]:
        my_drone.up(vel)

    if keys [pygame.K_S]:
        my_drone.down(vel)

    if keys [pygame.K_Q]:
        my_drone.ccw (vel)
    
    if keys [pygame.K_D]:
        my_drone.cw (vel)


my_drone.land()

quit()
