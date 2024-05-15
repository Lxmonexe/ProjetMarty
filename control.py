from martypy import Marty

def toward(marty):
    marty.walk()

def backward(marty):
    marty.walk(40,"auto",4.5)
    marty.walk(10)

def left(marty):
    marty.stand_straight()
    marty.walk(20,"auto",4,5)

def right(marty):
    marty.stand_straight()
    marty.walk(20,"auto",-4.5)

my_marty = Marty("wifi","192.168.0.2")
toward(my_marty)
backward(my_marty)