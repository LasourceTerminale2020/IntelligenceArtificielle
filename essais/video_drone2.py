from djitellopy import Tello
import cv2

width = 320
height = 240

drone = Tello()
drone.connect()


print(drone.get_battery())

drone.streamoff()
drone.streamon()

while True:
    frame_read = drone.get_frame_read()
    myFrame = frame_read.frame
    img = cv2.resize(myFrame, (width, height))
       
    cv2.imshow("MyResult", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break