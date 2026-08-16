from turtle import *

def spiral(size, angle):
    if size < 100:
        forward(size)
        right(angle)
        spiral(size+2, angle)

#tracer(0)
spiral(0, 60)

up()
goto(50, 180)
down()
spiral(0, 70)

done()