from turtle import *

def rtriangle(length, level):
    def tri(length):
        for i in range(3):
            forward(length)
            right(120)

    if level > 0:
        tri(length)
        n = length / 2
        up()
        forward(n)
        right(60)
        down()
        rtriangle(n, level-1)

#tracer(0)
rtriangle(150, 5)
done()