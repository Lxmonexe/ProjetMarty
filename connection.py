from martypy import Marty


def connect(marty):
    marty = Marty("wifi", "192.168.0.100")
    print("Connected to Marty!")

def disconnect(marty):
    marty = Marty.close()
    print("Disconnected from Marty!")
