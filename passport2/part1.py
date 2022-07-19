from djitellopy import Tello
import time

# SSID = "TELLO-F1C58F"

drone = Tello()

drone.connect()
time.sleep(15)
drone.streamon()
drone.takeoff()
drone_frame = drone.get_frame_read()
actual_frame = drone_frame.frame
time.sleep(10)

drone.land()