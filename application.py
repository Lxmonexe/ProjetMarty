from Interface import *

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    timer = QtCore.QTimer()
    timer.timeout.connect(ui.action)
    timer.start(2000) #CHANGER MILLISECONDE APPELER FONCTION DEPLACMENT
    sys.exit(app.exec())
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())