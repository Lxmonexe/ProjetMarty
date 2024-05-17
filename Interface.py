from connection import *
from control import *
from emotion import *
# from PyQt6.QtCore import Qt, QSize
# from PyQt6.QtGui import QPixmap
# from PyQt6 import QtCore
# from PyQt6.QtWidgets import (
#     QMainWindow,
#     QApplication,
#     QWidget,
#     QLabel,
#     QPushButton,
#     QMenuBar,
#     QStatusBar
# )

# class Ui_MainWindow:
#     def setupUi(self, MainWindow):
#         if MainWindow.objectName() == "":
#             MainWindow.setObjectName("MainWindow")
#         MainWindow.resize(1030, 711)
#         self.centralwidget = QWidget(MainWindow)
#         self.centralwidget.setObjectName("centralwidget")

#         self.label_2 = QLabel(self.centralwidget)
#         self.label_2.setObjectName("label_2")
#         self.label_2.setGeometry(220, 560, 101, 101)
#         self.label_2.setPixmap(QPixmap("C:/Users/em153068/Downloads/fleche.png"))
#         self.label_2.setScaledContents(True)

#         self.pushButton_3 = QPushButton(self.centralwidget)
#         self.pushButton_3.setObjectName("pushButton_3")
#         self.pushButton_3.setGeometry(220, 360, 101, 101)
#         self.pushButton_3.pressed.connect(self.forward_button_pressed)

#         self.pushButton_5 = QPushButton(self.centralwidget)
#         self.pushButton_5.setObjectName("pushButton_5")
#         self.pushButton_5.setGeometry(130, 200, 158, 23)

#         self.pushButton_6 = QPushButton(self.centralwidget)
#         self.pushButton_6.setObjectName("pushButton_6")
#         self.pushButton_6.setGeometry(320, 460, 101, 101)

#         self.pushButton_7 = QPushButton(self.centralwidget)
#         self.pushButton_7.setObjectName("pushButton_7")
#         self.pushButton_7.setGeometry(120, 460, 101, 101)

#         self.pushButton_8 = QPushButton(self.centralwidget)
#         self.pushButton_8.setObjectName("pushButton_8")
#         self.pushButton_8.setGeometry(220, 560, 101, 101)

#         MainWindow.setCentralWidget(self.centralwidget)

#         self.pushButton_8.raise_()
#         self.menubar = QMenuBar(MainWindow)
#         self.menubar.setObjectName("menubar")
#         self.menubar.setGeometry(0, 0, 1030, 21)
#         MainWindow.setMenuBar(self.menubar)
#         self.statusbar = QStatusBar(MainWindow)
#         self.statusbar.setObjectName("statusbar")
#         MainWindow.setStatusBar(self.statusbar)

#         self.retranslateUi(MainWindow)

#         QtCore.QMetaObject.connectSlotsByName(MainWindow)

#     def retranslateUi(self, MainWindow):
#         MainWindow.setWindowTitle(QApplication.translate("MainWindow", "MainWindow", None))
#         self.label_2.setText(QApplication.translate("MainWindow", "", None))
#         self.pushButton_3.setText(QApplication.translate("MainWindow", "Forward", None))
#         self.pushButton_5.setText(QApplication.translate("MainWindow", "Automatique", None))
#         self.pushButton_6.setText(QApplication.translate("MainWindow", "Right", None))
#         self.pushButton_7.setText(QApplication.translate("MainWindow", "Left", None))
#         self.pushButton_8.setText(QApplication.translate("MainWindow", "Backward", None))

#     def forward_button_pressed(self):
#         print("Forward button pressed")
        
# class MainWindow(QMainWindow, Ui_MainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setupUi(self)

# if __name__ == "__main__":
#     import sys
#     app = QApplication(sys.argv)
#     MainWindow = MainWindow()
#     MainWindow.show()
#     sys.exit(app.exec())

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6 import QtCore
from PyQt6.QtWidgets import (
    QMainWindow,
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QMenuBar,
    QStatusBar
)
MARTY: Marty 
class Ui_MainWindow:
   
    def setupUi(self, MainWindow):
        if MainWindow.objectName() == "":
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1030, 711)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        #Bouton arrière
        self.Backward_icon = QLabel(self.centralwidget)
        self.Backward_icon.setObjectName("Backward_icon")
        self.Backward_icon.setGeometry(110, 560, 101, 101)
        self.Backward_icon.setPixmap(QPixmap("./Interface/bas.png"))
        self.Backward_icon.setScaledContents(True)

        self.Backward = QPushButton(self.centralwidget)
        self.Backward.setObjectName("Backward")
        self.Backward.setGeometry(110, 560, 101, 101)
        self.Backward.setFlat(True)
        self.Backward.pressed.connect(self.backward_button_pressed)

        #Bouton avant
        self.Forward_icon = QLabel(self.centralwidget)
        self.Forward_icon.setObjectName("Forward_icon")
        self.Forward_icon.setGeometry(110, 360, 101, 101)
        self.Forward_icon.setPixmap(QPixmap("./Interface/haut.png"))
        self.Forward_icon.setScaledContents(True)

        self.Forward = QPushButton(self.centralwidget)
        self.Forward.setObjectName("Forward")
        self.Forward.setGeometry(110, 360, 101, 101)
        self.Forward.setFlat(True)
        self.Forward.pressed.connect(self.forward_button_pressed)

        #Bouton Gauche
        self.Left_icon = QLabel(self.centralwidget)
        self.Left_icon.setObjectName("Left_icon")
        self.Left_icon.setGeometry(10, 460, 101, 101)
        self.Left_icon.setPixmap(QPixmap("./Interface/gauche.png"))
        self.Left_icon.setScaledContents(True)

        self.Left = QPushButton(self.centralwidget)
        self.Left.setObjectName("Left")
        self.Left.setGeometry(10, 460, 101, 101)
        self.Left.setFlat(True)
        self.Left.pressed.connect(self.left_button_pressed)

        #Bouton Droite
        self.Right_icon = QLabel(self.centralwidget)
        self.Right_icon.setObjectName("Right_icon")
        self.Right_icon.setGeometry(210, 460, 101, 101)
        self.Right_icon.setPixmap(QPixmap("./Interface/droite.png"))
        self.Right_icon.setScaledContents(True)

        self.Right = QPushButton(self.centralwidget)
        self.Right.setObjectName("Right")
        self.Right.setGeometry(210, 460, 101, 101)
        self.Right.setFlat(True)
        self.Right.pressed.connect(self.right_button_pressed)

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
        self.Dance.setGeometry(910, 10, 101, 101)
        self.Dance.pressed.connect(self.dance_button_pressed)

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
        if(isConnect(MARTY)):
            backward(MARTY)
        else:
            print("You need to be connected !")
        

    def forward_button_pressed(self):
        if(isConnect(MARTY)):
            toward(MARTY)
        else:
            print("You need to be connected !")
     
    
    def left_button_pressed(self):
        if(isConnect(MARTY)):
            left(MARTY)
        else:
            print("You need to be connected !")
        
    
    def right_button_pressed(self):
        if(isConnect(MARTY)):
            right(MARTY)
        else:
            print("You need to be connected !")

    def auto_button_clicked(self):
        print("Auto button clicked")

    def connexion_button_clicked(self):
        global MARTY 
        MARTY = connect("wifi","192.168.0.101")
        
    def deconnexion_button_clicked(self):
        disconnect(MARTY)
        

    def dance_button_pressed(self):
        if(isConnect(MARTY)):
            dance(MARTY)
        else:
            print("You need to be connected !")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
