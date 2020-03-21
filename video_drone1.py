from djitellopy import Tello
import cv2

drone = Tello() #déclarer le drone
drone.connect()
drone.streamon()

print(drone.get_battery())

cap = cv2.VideoCapture("udp://0.0.0.0:11111")


while True:
    ret, frame = cap.read()
    print(ret)
    frame = drone.get_frame_read().frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()