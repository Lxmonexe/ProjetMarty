from martypy import Marty
import time

def angry(marty):
    marty.disco_color("red")
    marty.eyes("angry",500)
    time.sleep(1)
    marty.eyes("normal",1000)
    marty.disco_off()

def excited(marty):
    marty.disco_color("yellow")
    marty.eyes("excited",500) 
    time.sleep(2)
    marty.eyes("normal",1000)
    marty.disco_off()

def celebrate(marty):
    marty.celebrate()

def dance(marty):
    marty.dance()
