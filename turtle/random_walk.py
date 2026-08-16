from turtle import *
import random

wn = Screen()
tur = Turtle()
tur.goto(0, 0)

def random_walk(kame, n):
    for n in range(n):
        kame.forward(random.randrange(10, 60))
        kame.left(random.randrange(20, 180))
    
random_walk(tur, 30)
    
done()