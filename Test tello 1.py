from djitellopy import Tello
import cv2

width = 320
height = 240
startcounter = 1 #0 for flight 1 for testing

drone = Tello()
drone.connect()
drone.for_back_velocity = 0
drone.left_right_velocity = 0
drone.up_down_velocity = 0
drone.speed = 0

print(drone.get_battery())

drone.streamoff()
drone.streamon()

while True:
    frame_read = drone.get_frame_read()
    myFrame = frame_read.frame
    img = cv2.resize(myFrame, (width, height))

    if startcounter == 0:
        drone.takeoff()
        drone.move_left(20)
        drone.rotate_clockwise(90)
        startcounter = 1
    #velocity
    #if drone.send_rc_control:
    #   drone.send_rc_control(drone.left_right_velocity, drone.for_back_velocity, drone.up_down_velocity, drone.yaw_velocity)
    cv2.imshow("MyResult", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        drone.land()
        break
