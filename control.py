from martypy import Marty

def toward(marty: Marty,speed=1500):
    marty.walk(2,"auto",0,25,speed)
    marty.stand_straight()

def backward(marty: Marty,speed=1500):
   
    marty.walk(2,"auto",0,-25,speed)
    marty.stand_straight()

def left(marty: Marty,speed=1500):
    marty.walk(10,"auto",4.5,0,speed)
    marty.stand_straight()

def right(marty: Marty, speed=1500):
    marty.walk(10,"auto",-4.5,0,speed)
    marty.stand_straight()
