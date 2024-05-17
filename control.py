from martypy import Marty

def toward(marty: Marty,speed=1500):
    marty.walk(2,"auto",0,25,speed)

def backward(marty: Marty,speed=1500):
    marty.walk(40,"auto",4.5,25,speed)
    marty.walk(2,"auto",0,25,speed)

def left(marty: Marty,speed=1500):
    marty.stand_straight()
    marty.walk(20,"auto",4.5,25,speed)

def right(marty: Marty, speed=1500):
    marty.stand_straight()
    marty.walk(20,"auto",-4.5,25,speed)
