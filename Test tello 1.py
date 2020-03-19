from easytello import tello
import time

drone = tello.Tello() #déclarer le drone

drone.streamon() #début de la caméra
drone.takeoff() #décolage du drone
time.sleep(5) #pause de 5 secondes
drone.land() #attérisage du drone
