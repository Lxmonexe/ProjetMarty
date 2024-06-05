from connection import *
from control import *
from emotion import *
from sensor import *
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QPalette, QColor
from PyQt6 import QtCore
import sys
import keyboard
from PyQt6.QtWidgets import (
    QMainWindow,
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QMenuBar,
    QProgressBar,
    QSlider,
    QFrame,
    QStatusBar
)
MARTY: Marty 
class Ui_MainWindow:

    ipAddress = "192.168.0.101"
    isConnected = False
    state = "test"
    kstate = "ktest"
    emotion = "etest"
    pink = [255, 94, 235]
    red = [237, 28, 36]
    yellow = [255, 244, 74]
    green = [3, 230, 0]
    cyan = [103, 250, 255]
    blue = [0, 79, 113]
    black = [0, 0, 0]
    color = "#FFFFFF"

    def setupUi(self, MainWindow):
        if MainWindow.objectName() == "":
            MainWindow.setObjectName("MainWindow")
        MainWindow.setStyleSheet("background-color: #FEEFAD;") #jaune pale
        MainWindow.setStyleSheet("background-color: #FDDE55;") #jaune chaud
        MainWindow.setStyleSheet("background-color: #68D2E8;") #bleu cyan
        MainWindow.setStyleSheet("background-color: #03AED2;") #bleu mer
        MainWindow.resize(1536, 793)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #Bouton arrière
        self.Backward_icon = QLabel(self.centralwidget)
        self.Backward_icon.setObjectName("Backward_icon")
        self.Backward_icon.setGeometry(110, MainWindow.size().height()-140, 100, 100)
        self.Backward_icon.setPixmap(QPixmap("./Interface/bas.png"))
        self.Backward_icon.setScaledContents(True)

        self.Backward = QPushButton(self.centralwidget)
        self.Backward.setObjectName("Backward")
        self.Backward.setGeometry(110, MainWindow.size().height()-140, 100, 100)
        self.Backward.setFlat(True)
        self.Backward.pressed.connect(self.backward_button_pressed)
        self.Backward.released.connect(self.backward_button_released)

        #Bouton avant
        self.Forward_icon = QLabel(self.centralwidget)
        self.Forward_icon.setObjectName("Forward_icon")
        self.Forward_icon.setGeometry(110, MainWindow.size().height()-340, 100, 100)
        self.Forward_icon.setPixmap(QPixmap("./Interface/haut.png"))
        self.Forward_icon.setScaledContents(True)

        self.Forward = QPushButton(self.centralwidget)
        self.Forward.setObjectName("Forward")
        self.Forward.setGeometry(110, MainWindow.size().height()-340, 100, 100)
        self.Forward.setFlat(True)
        self.Forward.pressed.connect(self.forward_button_pressed)
        self.Forward.released.connect(self.forward_button_released)

        #Bouton Gauche
        self.Left_icon = QLabel(self.centralwidget)
        self.Left_icon.setObjectName("Left_icon")
        self.Left_icon.setGeometry(10, MainWindow.size().height()-240, 100, 100)
        self.Left_icon.setPixmap(QPixmap("./Interface/gauche.png"))
        self.Left_icon.setScaledContents(True)

        self.Left = QPushButton(self.centralwidget)
        self.Left.setObjectName("Left")
        self.Left.setGeometry(10, MainWindow.size().height()-240, 100, 100)
        self.Left.setFlat(True)
        self.Left.pressed.connect(self.left_button_pressed)
        self.Left.released.connect(self.left_button_released)

        #Bouton Droite
        self.Right_icon = QLabel(self.centralwidget)
        self.Right_icon.setObjectName("Right_icon")
        self.Right_icon.setGeometry(210, MainWindow.size().height()-240, 100, 100)
        self.Right_icon.setPixmap(QPixmap("./Interface/droite.png"))
        self.Right_icon.setScaledContents(True)

        self.Right = QPushButton(self.centralwidget)
        self.Right.setObjectName("Right")
        self.Right.setGeometry(210, MainWindow.size().height()-240, 100, 100)
        self.Right.setFlat(True)
        self.Right.pressed.connect(self.right_button_pressed)
        self.Right.released.connect(self.right_button_released)
        
        #Indicateur couleur
        self.indicateur = QFrame(self.centralwidget)
        self.indicateur.setGeometry(QtCore.QRect(880, 90, 370, 20))
        self.indicateur.setStyleSheet("background-color: #FFFFFF; border: 0px solid black;")

        self.frame = QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(880, 20, 370, 70))
        self.frame.setStyleSheet("background-color: #FEEFAD; border: 0px solid black;")

        #Bouton Pink
        self.Pink = QPushButton("", self.centralwidget)    
        self.Pink.setStyleSheet("background-color: #FF5EEB;") 
        self.Pink.setObjectName("Red")
        self.Pink.setGeometry(self.frame.pos().x() + 10, self.frame.pos().y() + 10, 50, 50)
        self.Pink.clicked.connect(self.Pink_button_clicked)

        #Bouton Red
        self.Red = QPushButton("", self.centralwidget)    
        self.Red.setStyleSheet("background-color: #ed1c24;") 
        self.Red.setObjectName("Red")
        self.Red.setGeometry(self.Pink.pos().x() + 50, self.frame.pos().y() + 10, 50, 50)
        self.Red.clicked.connect(self.Red_button_clicked)
        
        #Bouton Yellow
        self.Yellow = QPushButton("", self.centralwidget)    
        self.Yellow.setStyleSheet("background-color: #FFF44A;") 
        self.Yellow.setObjectName("Red")
        self.Yellow.setGeometry(self.Red.pos().x()+50, self.Red.pos().y(), 50, 50)
        self.Yellow.clicked.connect(self.Yellow_button_clicked)

        #Bouton Green
        self.Green = QPushButton("", self.centralwidget)    
        self.Green.setStyleSheet("background-color: #03E600;") 
        self.Green.setObjectName("Red")
        self.Green.setGeometry(self.Yellow.pos().x()+50, self.Red.pos().y(), 50, 50)
        self.Green.clicked.connect(self.Green_button_clicked)
        
        # Bouton Cyan
        self.Cyan = QPushButton("", self.centralwidget)    
        self.Cyan.setStyleSheet("background-color: #67FAFF;") 
        self.Cyan.setObjectName("Red")
        self.Cyan.setGeometry(self.Green.pos().x()+50, self.Red.pos().y(), 50, 50)
        self.Cyan.clicked.connect(self.Cyan_button_clicked)
        
        # Bouton Blue
        self.Blue = QPushButton("", self.centralwidget)    
        self.Blue.setStyleSheet("background-color: #004F71;") 
        self.Blue.setObjectName("Red")
        self.Blue.setGeometry(self.Cyan.pos().x()+50, self.Red.pos().y(), 50, 50)
        self.Blue.clicked.connect(self.Blue_button_clicked)

        # Bouton Black
        self.Black = QPushButton("", self.centralwidget)    
        self.Black.setStyleSheet("background-color: #000000;") 
        self.Black.setObjectName("Red")
        self.Black.setGeometry(self.Blue.pos().x()+50, self.Red.pos().y(), 50, 50)
        self.Black.clicked.connect(self.Black_button_clicked)

        # #Bouton angry
        self.Angry_icon = QLabel(self.centralwidget)
        self.Angry_icon.setObjectName("Angry_icon")
        self.Angry_icon.setGeometry(MainWindow.size().width() - 250, 10, 100, 100)
        self.Angry_icon.setPixmap(QPixmap("./Interface/angry.jpg"))
        self.Angry_icon.setScaledContents(True)

        self.Angry = QPushButton(self.centralwidget)
        self.Angry.setObjectName("Angry")
        self.Angry.setGeometry(MainWindow.size().width() - 250, 10, 100, 100)
        self.Angry.setFlat(True)
        self.Angry.clicked.connect(self.angry_button_clicked)

        #Bouton excited
        self.Excited_icon = QLabel(self.centralwidget)
        self.Excited_icon.setObjectName("Excited_icon")
        self.Excited_icon.setGeometry(MainWindow.size().width() - 150, 10, 100, 100)
        self.Excited_icon.setPixmap(QPixmap("./Interface/excited.png"))
        self.Excited_icon.setScaledContents(True)

        self.Excited = QPushButton(self.centralwidget)
        self.Excited.setObjectName("Excited")
        self.Excited.setGeometry(MainWindow.size().width() - 150, 10, 100, 100)
        self.Excited.setFlat(True)
        self.Excited.clicked.connect(self.excited_button_clicked)

        #Bouton automatique
        self.Auto = QPushButton(self.centralwidget)
        self.Auto.setObjectName("Auto")
        self.Auto.setGeometry(40, 120, 158, 23)
        self.Auto.clicked.connect(self.auto_button_clicked)

        #Bouton connexion
        self.Connexion_icon = QLabel(self.centralwidget)
        self.Connexion_icon.setObjectName("Connexion_icon")
        self.Connexion_icon.setGeometry(20, 10, 101, 101)
        self.Connexion_icon.setPixmap(QPixmap("./Interface/connexion.png"))
        self.Connexion_icon.setScaledContents(True)

        self.Connexion = QPushButton(self.centralwidget)
        self.Connexion.setObjectName("Connexion")
        self.Connexion.setGeometry(20, 10, 101, 101)
        self.Connexion.setFlat(True)
        self.Connexion.clicked.connect(self.connexion_button_clicked)

        #Bouton deconnexion
        self.Deconnexion_icon = QLabel(self.centralwidget)
        self.Deconnexion_icon.setObjectName("Deconnexion_icon")
        self.Deconnexion_icon.setGeometry(120, 10, 101, 101)
        self.Deconnexion_icon.setPixmap(QPixmap("./Interface/deconnexion.png"))
        self.Deconnexion_icon.setScaledContents(True)

        self.Deconnexion = QPushButton(self.centralwidget)
        self.Deconnexion.setObjectName("Deconnexion")
        self.Deconnexion.setGeometry(120, 10, 101, 101)
        self.Deconnexion.setFlat(True)
        self.Deconnexion.clicked.connect(self.deconnexion_button_clicked)
        
        #Bouton Dance
        self.Dance = QPushButton(self.centralwidget)
        self.Dance.setObjectName("Dance")
        self.Dance.setGeometry(110, MainWindow.size().height()-240, 100, 100)
        self.Dance.pressed.connect(self.dance_button_pressed)
        self.Dance.released.connect(self.dance_button_released)

        #Curseur de vitesse
        self.CurseurVitesse = QSlider(self.centralwidget)
        self.CurseurVitesse.setObjectName("CurseurVitesse")
        self.CurseurVitesse.setGeometry(QtCore.QRect(400, 40, 411, 22))
        self.CurseurVitesse.setMinimum(1000)
        self.CurseurVitesse.setMaximum(5000)
        self.CurseurVitesse.setSingleStep(1)
        self.CurseurVitesse.setSliderPosition(1500)
        self.CurseurVitesse.setOrientation(Qt.Orientation.Horizontal)
        self.CurseurVitesse.setStyleSheet("QSlider::handle:horizontal {width: 15;border-radius: 5px; margin: -8px; background-color: #FEEFAD; } QSlider::groove:horizontal {border: 2px solid #FEEFAD; height: 1px; background-color: #FEEFAD; } QSlider:add-page:horizontal {background-color: #68D2E8;}")

        #Barre de batterie
        self.Battery = QProgressBar(self.centralwidget)
        self.Battery.setObjectName("Batterie")
        self.Battery.setGeometry(QtCore.QRect(MainWindow.size().width() - 150, MainWindow.size().height() - 50, 118, 23))
        self.Battery.setValue(70)
        self.Battery.setStyleSheet("QProgressBar {border: 2px solid #FEEFAD; border-radius: 0px #FEEFAD; text-align: center; color: black; font-weight: bold; } QProgressBar::chunk {width: 10px; background-color: #FEEFAD; width: 20px;}")
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(0, 0, 1030, 21)
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QApplication.translate("MainWindow", "MainWindow", None))
        self.Auto.setText(QApplication.translate("MainWindow", "Automatique", None))
        self.Dance.setText(QApplication.translate("MainWindow", "Dance", None))
        self.Connexion.setText(QApplication.translate("MainWindow", "", None))
        self.Deconnexion.setText(QApplication.translate("MainWindow", "", None))

    def backward_button_pressed(self):
        self.state = "backward"

    def backward_button_released(self):
        self.state = "idle"

    def forward_button_pressed(self):
        self.state = "forward"

    def forward_button_released(self):
        self.state = "idle"

    def left_button_pressed(self):
        self.state = "left"

    def left_button_released(self):
        self.state = "idle"

    def right_button_pressed(self):
        self.state = "right"

    def right_button_released(self):
        self.state = "idle"

    def Pink_button_clicked(self):
        self.pink = calibrate_pink(MARTY)
        print("Pink button clicked")

    def Red_button_clicked(self):
        self.red = calibrate_red(MARTY)
        print("Red button clicked")

    def Yellow_button_clicked(self):
        self.yellow = calibrate_yellow(MARTY)
        print("Yellow button clicked")
    
    def Green_button_clicked(self):
        self.green = calibrate_green(MARTY)
        print("Green button clicked")

    def Cyan_button_clicked(self):
        self.cyan = calibrate_cyan(MARTY)
        print("Cyan button clicked")
    
    def Blue_button_clicked(self):
        self.blue = calibrate_blue(MARTY)
        print("Blue button clicked")
    
    def Black_button_clicked(self):
        self.black = calibrate_black(MARTY)
        print("Black button clicked")

    def angry_button_clicked(self):
        angry(MARTY)

    def excited_button_clicked(self):
        excited(MARTY)

    def auto_button_clicked(self):
        print("Auto button clicked")

    def connexion_button_clicked(self):
        global MARTY 
        MARTY = connect("usb", "COM3")
        self.Connexion_icon.setPixmap(QPixmap("./Interface/connexion_on.png"))
        self.isConnected = True
        
    def deconnexion_button_clicked(self):
        disconnect(MARTY)
        self.Connexion_icon.setPixmap(QPixmap("./Interface/connexion.png"))

    def dance_button_pressed(self):
        self.state = "dance"

    def dance_button_released(self):
        self.state = "idle"

    def keyboard(self):
        if keyboard.is_pressed('z') and self.kstate == "idle": 
            self.kstate = "forward"
            toward(MARTY, self.CurseurVitesse.value())
        elif keyboard.is_pressed('s') and self.kstate == "idle": 
            self.kstate = "backward"
            backward(MARTY, self.CurseurVitesse.value())
        elif keyboard.is_pressed('q') and self.kstate == "idle": 
            self.kstate = "left"
            left(MARTY, self.CurseurVitesse.value())
        elif keyboard.is_pressed('d') and self.kstate == "idle": 
            self.kstate = "right"
            right(MARTY, self.CurseurVitesse.value())
        else:
            self.kstate = "idle"

    def resize(self):
        self.Backward_icon.setGeometry(110, MainWindow.size().height()-140, 100, 100)
        self.Backward.setGeometry(110, MainWindow.size().height()-140, 100, 100)

        self.Forward_icon.setGeometry(110, MainWindow.size().height()-340, 100, 100)
        self.Forward.setGeometry(110, MainWindow.size().height()-340, 100, 100)

        self.Left_icon.setGeometry(10, MainWindow.size().height()-240, 100, 100)
        self.Left.setGeometry(10, MainWindow.size().height()-240, 100, 100)

        self.Right_icon.setGeometry(210, MainWindow.size().height()-240, 100, 100)
        self.Right.setGeometry(210, MainWindow.size().height()-240, 100, 100)
        
        self.indicateur.setStyleSheet("background-color: 'color'; border: 0px solid black;")

        self.Angry_icon.setGeometry(MainWindow.size().width() - 250, 10, 100, 100)
        self.Angry.setGeometry(MainWindow.size().width() - 250, 10, 100, 100)
        
        self.Excited_icon.setGeometry(MainWindow.size().width() - 150, 10, 100, 100)
        self.Excited.setGeometry(MainWindow.size().width() - 150, 10, 100, 100)

        self.Dance.setGeometry(110, MainWindow.size().height()-240, 100, 100)
        self.Battery.setGeometry(QtCore.QRect(MainWindow.size().width() - 150, MainWindow.size().height() - 50, 118, 23)) 
        if(self.isConnected):  
            self.color = color_sensor(self.yellow, self.green, self.pink, self.red, self.blue, self.cyan, self.black, MARTY)
            self.indicateur.setStyleSheet("background-color: " + self.color + "; border: 0px solid black;")

    def action(self):
        if self.state == "idle":
            stop(MARTY)
        if self.state == "forward":
            toward(MARTY, self.CurseurVitesse.value())
        if self.state == "backward":
            backward(MARTY, self.CurseurVitesse.value())
        if self.state == "left":
            left(MARTY, self.CurseurVitesse.value())
        if self.state == "right":
            right(MARTY, self.CurseurVitesse.value())
        if self.state == "dance":
            dance(MARTY)

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
    timerResize.timeout.connect(ui.resize)
    timerMove.start(100)  #CHANGER MILLISECONDE APPELER FONCTION DEPLACMENT
    timerResize.start(5)
    sys.exit(app.exec())

