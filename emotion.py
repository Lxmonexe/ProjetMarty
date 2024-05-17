from martypy import Marty
import time

def angry(marty):
    marty.eyes("angry",500)
    time.sleep(1)
    marty.eyes("normal",1000)

def excited(marty):
    marty.eyes("excited",500)
    time.sleep(1)
    marty.eyes("normal",1000)

def celebrate(marty):
    marty.celebrate()

def dance(marty):
    marty.dance()
