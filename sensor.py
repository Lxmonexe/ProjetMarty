import threading
import time
from martypy import Marty
from typing import Union, get_origin, get_args

my_marty = Marty("usb", "COM3")


battery_level = 0 # Initialisation de la variable partagée
previous_battery_level = 0  
battery_lock = threading.Lock()

def monitor_battery():
    global battery_level
    global previous_battery_level
    while True:
        with battery_lock:
            battery_level = my_marty.get_battery_remaining()
            if battery_level > previous_battery_level:
                previous_battery_level = battery_level
                return battery_level
        time.sleep(1)

# Crée et démarre le thread avec la fonction de rappel
battery_thread = threading.Thread(target=monitor_battery)
battery_thread.daemon = True  # Pour que le thread se termine lorsque le programme principal se termine
battery_thread.start()

monitor_battery()

# try:
#     while True:
#         time.sleep(1)
# except KeyboardInterrupt:
#     print("Programme terminé.")

# # my_marty.walk(2);
# distanceSensor = my_marty.get_distance_sensor();

# print(type(distanceSensor));
# print(distanceSensor);

# status = my_marty.get_power_status();
# itr = 0;
# lenght = len(status);
# names = status.keys();
# values = status.values();

# # return the status values of the robot
# for name, value in status.items():
#     print(name + " = " + str(value));

# robotStatus = my_marty.get_robot_status();

# for nme, val in robotStatus.items():
#     print(nme + " = " + str(val));


# my_marty.walk(30, 'auto', 0 , -25, 1500, None);

# # Foot sensor 
# leftSensor = my_marty.get_ground_sensor_reading("left");
# rightSensor = my_marty.get_ground_sensor_reading("right");
# print(leftSensor);
# print(rightSensor);

# leftGroundSensor = my_marty.get_obstacle_sensor_reading("left");
# rightGroundSensor = my_marty.get_obstacle_sensor_reading("right");
# print(leftGroundSensor);
# print(rightGroundSensor);


# # print(get_origin(distanceSensor));
# # print(get_args(distanceSensor));

# # flt = isinstance(distanceSensor, type(Union));
# # i = isinstance(distanceSensor, type(int));

# # print(flt);
# # print(i);

# # for value in distanceSensor:
# #     print(value);

