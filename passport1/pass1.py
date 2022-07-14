# from djitellopy import Tello
from djitellopy import Tello

# SSID = "TELLO-F1C58F"

drone = Tello()

# drone.connect_to_wifi("TELLO-F1C58F", "")
drone.connect()


# while(True):
print(drone.get_battery())
# drone.sleep()



