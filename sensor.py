from martypy import Marty
from typing import Union, get_origin, get_args

my_marty = Marty("wifi", "192.168.0.101");
batteryRemaining = my_marty.get_battery_remaining();
print(batteryRemaining);

# my_marty.walk(2);
distanceSensor = my_marty.get_distance_sensor();

print(type(distanceSensor));
print(distanceSensor);

status = my_marty.get_power_status();
itr = 0;
lenght = len(status);
names = status.keys();
values = status.values();

# return the status values of the robot
for name, value in status.items():
    print(name + " = " + str(value));

robotStatus = my_marty.get_robot_status();

for nme, val in robotStatus.items():
    print(nme + " = " + str(val));


my_marty.walk(30, 'auto', 0 , -25, 1500, None);

# Foot sensor 
leftSensor = my_marty.get_ground_sensor_reading("left");
rightSensor = my_marty.get_ground_sensor_reading("right");
print(leftSensor);
print(rightSensor);

leftGroundSensor = my_marty.get_obstacle_sensor_reading("left");
rightGroundSensor = my_marty.get_obstacle_sensor_reading("right");
print(leftGroundSensor);
print(rightGroundSensor);


# print(get_origin(distanceSensor));
# print(get_args(distanceSensor));

# flt = isinstance(distanceSensor, type(Union));
# i = isinstance(distanceSensor, type(int));

# print(flt);
# print(i);

# for value in distanceSensor:
#     print(value);

