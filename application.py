from Interface import *
from martyController import *

def connect(wifi, ip):
     MartyController.connect(wifi, ip)

def disconnect():
    MartyController.disconnect()

def isConnect():
    MartyController.isConnect()

def toward(speed=1500):
    MartyController.toward(speed)

def backward(speed=1500):
    MartyController.backward()
    
def left(speed=1500):
    MartyController.left(speed)

def right(speed=1500):
    MartyController.right(speed)

def stop():
    MartyController.stop()

def calibrate_yellow():
    MartyController.calibrate_yellow()

def calibrate_green():
    MartyController.calibrate_green()

def calibrate_pink():
    MartyController.calibrate_pink()

def calibrate_red():
    MartyController.calibrate_pink()

def calibrate_cyan():
    MartyController.calibrate_cyan()

def calibrate_blue():
    MartyController.calibrate_blue()

def calibrate_black():
    MartyController.calibrate_black()

def color_sensor(yellow, green, pink, red, blue, cyan, black):
    MartyController.color_sensor(yellow, green, pink, red, blue, cyan, black)

def angry():
    MartyController.angry()

def excited():
    MartyController.excited()

def celebrate():
    MartyController.celebrate()

def dance():
    MartyController.dance()

def get_battery():
    MartyController.get_battery()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    timerMove = QtCore.QTimer()
    timerResize = QtCore.QTimer()
    timerMove.timeout.connect(ui.action)
    timerMove.timeout.connect(ui.keyboard)
    timerResize.timeout.connect(lambda: ui.resize(MainWindow))
    timerMove.start(100)  #CHANGER MILLISECONDE APPELER FONCTION DEPLACMENT
    timerResize.start(5)
    sys.exit(app.exec())