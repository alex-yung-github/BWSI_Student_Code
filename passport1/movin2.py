from djitellopy import Tello
import time

# SSID = "TELLO-F1C58F"

drone = Tello()

drone.connect()
time.sleep(15)
drone.takeoff()
drone.move_forward(150)
drone.rotate_clockwise(90)
drone.move_forward(150)
drone.rotate_clockwise(90)
drone.move_forward(150)
drone.rotate_clockwise(90)
drone.move_forward(150)
drone.rotate_clockwise(90)
drone.land()