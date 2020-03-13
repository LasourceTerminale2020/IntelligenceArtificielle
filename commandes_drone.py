from easytello import tello 
import pygame
my_drone = tello.Tello()
my_drone.takeoff()

pygame.init()


vel=10


run= True

while run:

    keys= pygame.key.get_pressed()
    
    if keys [pygame.K_t]:
        run= False
    
    if keys [pygame.K_LEFT]:
        my_drone.left(vel)

    if keys [pygame.K_RIGHT]:
        my_drone.right(vel)
    
    if keys [pygame.K_UP]:
        my_drone.forward(vel)

    if keys[pygame.K_DOWN]:
        my_drone.back(vel)

    if keys [pygame.K_z]:
        my_drone.up(vel)

    if keys [pygame.K_s]:
        my_drone.down(vel)

    if keys [pygame.K_q]:
        my_drone.ccw (vel)
    
    if keys [pygame.K_d]:
        my_drone.cw (vel)


my_drone.land()

quit()


#test
