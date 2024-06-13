from threading import Thread
# from Interface import *
from martyController import *

class Controller:

    tab1 = []
    tab2 = []
    tabFinal = []

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

    
    def acquisition_controller(self, NBMarty):
        if(NBMarty == 1):
            self.tab1 = self.marty.auto()
            print(self.tab1)
        elif(NBMarty == 2):
            self.tab2 = self.marty.auto()
            print(self.tab2)
        else:
            print("Error")

    def merge_tab(self):
        for i in range(0, len(self.tab1)):
            if(self.tab1[i] == self.tab2[i]):
                self.tabFinal.append(self.tab1[i])
            elif((self.tab1[i] != self.tab2[i]) & (self.tab1[i] == "#000000")):
                self.tabFinal.append(self.tab2[i])
            elif((self.tab1[i] != self.tab2[i]) & (self.tab2[i] == "#000000")):
                self.tabFinal.append(self.tab1[i])
        self.marty.celebrate()
    
    def auto_controller(self, speed):
        i = 0
        while self.tabFinal[i] != "#ed1c24":
            if((self.tabFinal[i] == "#03E600") | (self.tabFinal[i] == "#67FAFF")):
                self.marty.towardAuto(speed)
                if(i == 0):
                    i = 5
                elif(i == 1):
                    i = 4
                elif(i == 2):
                    i = 3
                elif(i == 3):
                    i = 8
                elif(i == 4):
                    i = 7
                elif(i == 5):
                    i = 6
            elif(self.tabFinal[i] == "#FFF44A"):
                self.marty.backwardAuto(speed)
                if(i == 3):
                    i = 2
                elif(i == 4):
                    i = 1
                elif(i == 6):
                    i = 5
                elif(i == 7):
                    i = 4
                elif(i == 8):
                    i = 3
            elif(self.tabFinal[i] == "#FF5EEB"):
                self.marty.leftAuto(speed)
                if(i == 2):
                    i = 1
                elif(i == 3):
                    i = 4
                elif(i == 4):
                    i = 5
                elif(i == 7):
                    i = 6
                elif(i == 8):
                    i = 7
            elif(self.tabFinal[i] == "#004F71"):
                self.marty.rightAuto(speed)
                if(i == 1):
                    i = 2
                elif(i == 4):
                    i = 3
                elif(i == 5):
                    i = 4
                elif(i == 6):
                    i = 7
                elif(i == 7):
                    i = 8                  
        self.marty.dance()


                
        