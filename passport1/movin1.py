from djitellopy import Tello
import time

# SSID = "TELLO-F1C58F"

drone = Tello()

drone.connect()
drone.takeoff()
time.sleep(2)
drone.land()