from Interface import *

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