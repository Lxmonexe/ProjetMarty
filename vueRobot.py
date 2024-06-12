from martyController import *

marty = MartyController("usb", "COM3")
marty.connect()

tab = marty.auto()

for i in range(0, len(tab)):
    print(tab[i])
    