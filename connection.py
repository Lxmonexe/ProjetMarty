from martypy import Marty


def connect(wifi, ip):
    marty = Marty(wifi, ip)
    if(marty.is_conn_ready()):
        print("Connected to Marty!")
    return marty

def disconnect(marty):
    marty.close()
    if not (marty.is_conn_ready()):
        print("Disconnected from Marty!")

def isConnect(marty):
    return marty.is_conn_ready()
