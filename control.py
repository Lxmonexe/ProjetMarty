from martypy import Marty

def toward(marty: Marty,speed=1500):
    marty.walk(2,"auto",0,25,speed)
    marty.walk(2,"auto",0,12,speed)
    

def backward(marty: Marty,speed=1500):
   
    marty.walk(2,"auto",0,-25,speed)
    marty.walk(1,"auto",0,-12,speed)
    

def left(marty: Marty,speed=1500):
    marty.walk(15,"auto",4.5,0,speed)
    marty.stand_straight()

def right(marty: Marty, speed=1500):
    marty.walk(15,"auto",-4.5,0,speed)
    marty.stand_straight()

def stop(marty: Marty):
    marty.stop()
