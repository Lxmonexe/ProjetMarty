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


# my_marty.walk(20, 'auto', 0 , -25, 1500, None);

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

def calibrate_yellow(marty):
    valeurHex = marty.get_color_sensor_hex("left");
    valeurRGB = hex_to_rgb(valeurHex);
    return valeurRGB;
    
def calibrate_green(marty):
    valeurHex = marty.get_color_sensor_hex("left");
    valeurRGB = hex_to_rgb(valeurHex);
    return valeurRGB;

def calibrate_pink(marty):
    valeurHex = marty.get_color_sensor_hex("left");
    valeurRGB = hex_to_rgb(valeurHex);
    return valeurRGB;

def calibrate_red(marty):
    valeurHex = marty.get_color_sensor_hex("left");
    valeurRGB = hex_to_rgb(valeurHex);
    return valeurRGB;

def calibrate_cyan(marty):
    valeurHex = marty.get_color_sensor_hex("left");
    valeurRGB = hex_to_rgb(valeurHex);
    return valeurRGB;

def calibrate_blue(marty):
    valeurHex = marty.get_color_sensor_hex("left");
    valeurRGB = hex_to_rgb(valeurHex);
    return valeurRGB;

def calibrate_black(marty):
    valeurHex = marty.get_color_sensor_hex("left");
    valeurRGB = hex_to_rgb(valeurHex);
    return valeurRGB;

def color_sensor(yellow, green, pink, red, blue, cyan, black, marty):
    colorHEX = marty.get_color_sensor_hex("left");
    colorRGB = hex_to_rgb(colorHEX);
    if ((is_within_uncertainty(colorRGB[0], yellow[0], 10)) and (is_within_uncertainty(colorRGB[1], yellow[1], 10)) and (is_within_uncertainty(colorRGB[2], yellow[2], 10))):
        return "yellow";
    elif ((is_within_uncertainty(colorRGB[0], green[0], 10)) and (is_within_uncertainty(colorRGB[1], green[1], 10)) and (is_within_uncertainty(colorRGB[2], green[2], 10))):
        return "green";
    elif ((is_within_uncertainty(colorRGB[0], pink[0], 10)) and (is_within_uncertainty(colorRGB[1], pink[1], 10)) and (is_within_uncertainty(colorRGB[2], pink[2], 10))):
        return "pink";
    elif ((is_within_uncertainty(colorRGB[0], red[0], 10)) and (is_within_uncertainty(colorRGB[1], red[1], 10)) and (is_within_uncertainty(colorRGB[2], red[2], 10))):
        return "red";
    elif ((is_within_uncertainty(colorRGB[0], blue[0], 10)) and (is_within_uncertainty(colorRGB[1], blue[1], 10)) and (is_within_uncertainty(colorRGB[2], blue[2], 10))):
        return "blue";
    elif ((is_within_uncertainty(colorRGB[0], cyan[0], 10)) and (is_within_uncertainty(colorRGB[1], cyan[1], 10)) and (is_within_uncertainty(colorRGB[2], cyan[2], 10))):
        return "cyan";
    elif ((is_within_uncertainty(colorRGB[0], black[0], 10)) and (is_within_uncertainty(colorRGB[1], black[1], 10)) and (is_within_uncertainty(colorRGB[2], black[2], 10))):
        return "black";
    else:
        return "not defined";



def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    rgb_color = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    return rgb_color

def is_within_uncertainty(value, central_value, uncertainty):
    lower_bound = central_value - uncertainty
    upper_bound = central_value + uncertainty
    return lower_bound <= value <= upper_bound


