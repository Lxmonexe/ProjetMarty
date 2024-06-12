from tokenize import String
from martypy import Marty
from mathsColor import *
import time

class MartyController: 
    
    def __init__(self, type, ip) -> None:
        self.marty = None
        self.yellow = None 
        self.green = None
        self.pink = None
        self.red = None
        self.blue = None 
        self.cyan = None
        self.black = None
        self.type = type
        self.ip = ip

    def connect(self):
        self.marty = Marty(self.type, self.ip)
        if(self.marty.is_conn_ready()):
            print("Connected to self.marty!")
       
    def disconnect(self):
        self.marty.close()
        if not (self.marty.is_conn_ready()):
            print("Disconnected from self.marty!")

    def isConnect(self):
        return self.marty.is_conn_ready()

    def toward(self, speed=1500):
        self.marty.walk(2,"auto",0,25,speed)
        self.marty.walk(2,"auto",0,12,speed)
    
    def backward(self, speed=1500):
        self.marty.walk(2,"auto",0,-25,speed)
        self.marty.walk(1,"auto",0,-12,speed)
        
    def left(self, speed=1500):
        self.marty.walk(15,"auto",4.5,0,speed)
        self.marty.stand_straight()

    def right(self, speed=1500):
        self.marty.walk(15,"auto",-4.5,0,speed)
        self.marty.stand_straight()

    def stop(self):
        self.marty.stop()

    def calibrate_yellow(self):
        valeurHex = self.marty.get_color_sensor_hex("left")
        valeurRGB = hex_to_rgb(valeurHex)
        self.yellow = valeurRGB
    
    def calibrate_green(self):
        valeurHex = self.marty.get_color_sensor_hex("left")
        valeurRGB = hex_to_rgb(valeurHex)
        self.green = valeurRGB

    def calibrate_pink(self):
        valeurHex = self.marty.get_color_sensor_hex("left")
        valeurRGB = hex_to_rgb(valeurHex)
        self.pink = valeurRGB

    def calibrate_red(self):
        valeurHex = self.marty.get_color_sensor_hex("left")
        valeurRGB = hex_to_rgb(valeurHex)
        self.red = valeurRGB

    def calibrate_cyan(self):
        valeurHex = self.marty.get_color_sensor_hex("left")
        valeurRGB = hex_to_rgb(valeurHex)
        self.cyan = valeurRGB

    def calibrate_blue(self):
        valeurHex = self.marty.get_color_sensor_hex("left")
        valeurRGB = hex_to_rgb(valeurHex)
        self.blue = valeurRGB

    def calibrate_black(self):
        valeurHex = self.marty.get_color_sensor_hex("left")
        valeurRGB = hex_to_rgb(valeurHex)
        self.black = valeurRGB

    def color_sensor(self):
        colorHEX = self.marty.get_color_sensor_hex("left")
        colorRGB = hex_to_rgb(colorHEX)
        if ((is_within_uncertainty(colorRGB[0], self.yellow[0], 10)) and (is_within_uncertainty(colorRGB[1], self.yellow[1], 10)) and (is_within_uncertainty(colorRGB[2], self.yellow[2], 10))):
            return "#FFF44A"
        elif ((is_within_uncertainty(colorRGB[0], self.green[0], 10)) and (is_within_uncertainty(colorRGB[1], self.green[1], 10)) and (is_within_uncertainty(colorRGB[2], self.green[2], 10))):
            return "#03E600"
        elif ((is_within_uncertainty(colorRGB[0], self.pink[0], 10)) and (is_within_uncertainty(colorRGB[1], self.pink[1], 10)) and (is_within_uncertainty(colorRGB[2], self.pink[2], 10))):
            return "#FF5EEB"
        elif ((is_within_uncertainty(colorRGB[0], self.red[0], 10)) and (is_within_uncertainty(colorRGB[1], self.red[1], 10)) and (is_within_uncertainty(colorRGB[2], self.red[2], 10))):
            return "#ed1c24"
        elif ((is_within_uncertainty(colorRGB[0], self.blue[0], 10)) and (is_within_uncertainty(colorRGB[1], self.blue[1], 10)) and (is_within_uncertainty(colorRGB[2], self.blue[2], 10))):
            return "#004F71"
        elif ((is_within_uncertainty(colorRGB[0], self.cyan[0], 10)) and (is_within_uncertainty(colorRGB[1], self.cyan[1], 10)) and (is_within_uncertainty(colorRGB[2], self.cyan[2], 10))):
            return "#67FAFF"
        elif ((is_within_uncertainty(colorRGB[0], self.black[0], 10)) and (is_within_uncertainty(colorRGB[1], self.black[1], 10)) and (is_within_uncertainty(colorRGB[2], self.black[2], 10))):
            return "#000000"
        else:
            return "not defined"

    def angry(self):
        self.marty.disco_color("red")
        self.marty.eyes("angry",500)
        time.sleep(1)
        self.marty.eyes("normal",1000)
        self.marty.disco_off()

    def excited(self):
        self.marty.disco_color("yellow")
        self.marty.eyes("excited",500) 
        time.sleep(2)
        self.marty.eyes("normal",1000)
        self.marty.disco_off()

    def celebrate(self):
        self.marty.celebrate()

    def dance(self):
        self.marty.dance()

    def get_battery(self):
        return self.marty.get_battery_remaining()


