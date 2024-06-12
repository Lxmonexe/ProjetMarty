from threading import Thread
# from Interface import *
from martyController import *

class Controller:

    tab1 = []
    tab2 = []

    def __init__(self, wifi, ip):
        self.marty = None
        self.wifi = wifi
        self.ip = ip

    def connect_controller(self):
        self.marty = MartyController(self.wifi, self.ip)
        t = Thread(target=self.marty.connect())
        t.start()

    def disconnect_controller(self):
        t = Thread(target=self.marty.disconnect())
        t.start()

    def isConnect_controller(self):
        t = Thread(target=self.marty.isConnect())
        t.start()

    def toward_controller(self, speed=1500):
        t = Thread(target=self.marty.toward(speed))
        t.start()

    def backward_controller(self, speed=1500):
        t = Thread(target=self.marty.backward(speed))
        t.start()
        
    def left_controller(self, speed=1500):
        t = Thread(target=self.marty.left(speed))
        t.start()

    def right_controller(self, speed=1500):
        t = Thread(target=self.marty.right(speed))
        t.start()

    def stop_controller(self):
        t = Thread(target=self.marty.stop())
        t.start()

    def calibrate_yellow_controller(self):
        t = Thread(target=self.marty.calibrate_yellow())
        t.start()

    def calibrate_green_controller(self):
        t = Thread(target=self.marty.calibrate_green())
        t.start()

    def calibrate_pink_controller(self):
        t = Thread(target=self.marty.calibrate_pink())
        t.start()

    def calibrate_red_controller(self):
        t = Thread(target=self.marty.calibrate_red())
        t.start()

    def calibrate_cyan_controller(self):
        t = Thread(target=self.marty.calibrate_cyan())
        t.start()

    def calibrate_blue_controller(self):
        t = Thread(target=self.marty.calibrate_blue())
        t.start()

    def calibrate_black_controller(self):
        t = Thread(target=self.marty.calibrate_black())
        t.start()

    def color_sensor_controller(self):
        t = Thread(target=self.marty.color_sensor())
        t.start()

    def angry_controller(self):
        t = Thread(target=self.marty.angry())
        t.start()

    def excited_controller(self):
        t = Thread(target=self.marty.excited())
        t.start()

    def celebrate_controller(self):
        t = Thread(target=self.marty.celebrate())
        t.start()

    def dance_controller(self):
        t = Thread(target=self.marty.dance())
        t.start()

    def get_battery_controller(self):
        return self.marty.get_battery()

    def auto_controller(self):
        t = Thread(target=self.marty.auto())
        t.start()
    
    def auto_controller(self, NBMarty):
        if(NBMarty == 1):
            self.tab1 = self.marty.auto()
        elif(NBMarty == 2):
            self.tab2 = self.marty.auto()
        else:
            print("Error")
         
        