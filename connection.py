from martypy import Marty


def connect(wifi, ip):
    marty = Marty(wifi, ip)
    print("Connected to Marty!")
    return marty

def disconnect(marty):
    marty.close()
    print("Disconnected from Marty!")
