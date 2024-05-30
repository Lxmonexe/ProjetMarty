from connection import *
from control import *
from emotion import *
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
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
    QStatusBar
)
MARTY: Marty 
class Ui_MainWindow:
    state = "test"
    kstate = "ktest"
    emotion = "etest"
    def setupUi(self, MainWindow):
        if MainWindow.objectName() == "":
            MainWindow.setObjectName("MainWindow")

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

        #Bouton angry
        self.Angry_icon = QLabel(self.centralwidget)
        self.Angry_icon.setObjectName("Right_icon")
        self.Angry_icon.setGeometry(MainWindow.size().width() - 250, 10, 100, 100)
        self.Angry_icon.setPixmap(QPixmap("./Interface/angry.jpg"))
        self.Angry_icon.setScaledContents(True)

        self.Angry = QPushButton(self.centralwidget)
        self.Angry.setObjectName("Right")
        self.Angry.setGeometry(MainWindow.size().width() - 250, 10, 100, 100)
        self.Angry.setFlat(True)
        self.Angry.clicked.connect(self.angry_button_clicked)

        #Bouton excited
        self.Excited_icon = QLabel(self.centralwidget)
        self.Excited_icon.setObjectName("Right_icon")
        self.Excited_icon.setGeometry(MainWindow.size().width() - 150, 10, 100, 100)
        self.Excited_icon.setPixmap(QPixmap("./Interface/excited.png"))
        self.Excited_icon.setScaledContents(True)

        self.Excited = QPushButton(self.centralwidget)
        self.Excited.setObjectName("Right")
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

        #Barre de batterie
        self.Battery = QProgressBar(self.centralwidget)
        self.Battery.setObjectName("Batterie")
        self.Battery.setGeometry(QtCore.QRect(MainWindow.size().width() - 150, MainWindow.size().height() - 50, 118, 23))
        self.Battery.setValue(50)
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

    def angry_button_clicked(self):
        self.emotion = "angry"

    def excited_button_clicked(self):
        self.emotion = "excited"

    def auto_button_clicked(self):
        print("Auto button clicked")

    def connexion_button_clicked(self):
        global MARTY 
        MARTY = connect("wifi","192.168.0.101")

    def deconnexion_button_clicked(self):
        disconnect(MARTY)

    def dance_button_pressed(self):
        self.state = "dance"

    def dance_button_released(self):
        self.state = "idle"

    def keyboard(self):
        if keyboard.is_pressed('z') and self.kstate == "idle": 
            self.kstate = "forward"
        elif keyboard.is_pressed('s') and self.kstate == "idle": 
            self.kstate = "backward"
        elif keyboard.is_pressed('q') and self.kstate == "idle": 
            self.kstate = "left"
        elif keyboard.is_pressed('d') and self.kstate == "idle": 
            self.kstate = "right"
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

        self.Angry_icon.setGeometry(MainWindow.size().width() - 250, 10, 100, 100)
        self.Angry.setGeometry(MainWindow.size().width() - 250, 10, 100, 100)
        
        self.Excited_icon.setGeometry(MainWindow.size().width() - 150, 10, 100, 100)
        self.Excited.setGeometry(MainWindow.size().width() - 150, 10, 100, 100)

        self.Dance.setGeometry(110, MainWindow.size().height()-240, 100, 100)
        self.Battery.setGeometry(QtCore.QRect(MainWindow.size().width() - 150, MainWindow.size().height() - 50, 118, 23))    

    def emotion_state(self):
        if self.emotion == "angry":
            angry(MARTY)
        elif self.emotion == "excited":
            excited(MARTY)

    def action(self):
        # if(isConnect(MARTY)):
            print(self.CurseurVitesse.value()) #☻Pour récupérer la valeur du curseur quand vous voulez changer la vitesse
            if self.state == "idle" and self.kstate == "idle":
                print("idle")
            if self.state == "forward" or self.kstate == "forward":
                print("forward")
                #     angry(MARTY)
            if self.state == "backward" or self.kstate == "backward":
                print("backward")
                #     excited(MARTY)
            if self.state == "left" or self.kstate == "left":
                print("left")
                #left(MARTY)
            if self.state == "right" or self.kstate == "right":
                print("right")
                #right(MARTY)
            if self.state == "dance" or self.kstate == "dance":
                print("dance")
                #dance(MARTY)
        # else:
        #     print("You need to be connected !")

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
    timerMove.timeout.connect(ui.emotion_state)
    timerResize.timeout.connect(ui.resize)
    timerMove.start(100)  #CHANGER MILLISECONDE APPELER FONCTION DEPLACMENT
    timerResize.start(5)
    sys.exit(app.exec())
