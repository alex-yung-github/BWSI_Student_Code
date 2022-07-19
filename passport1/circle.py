from djitellopy import Tello
import time

# SSID = "TELLO-F1C58F"

drone = Tello()

drone.connect()
time.sleep(14)
drone.takeoff()
drone.curve_xyz_speed(25, -25, 0, 25, -150, 0, 15)
drone.curve_xyz_speed(25, -150, 0, 25, -25, 0, 15)
drone.land()