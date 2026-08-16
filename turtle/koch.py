from turtle import *

def koch(length, level):
    if level == 0:
        forward(length)
    else:
        n = length / 3
        w = level - 1
        koch(n, w)
        left(60)
        koch(n, w)
        right(120)
        koch(n, w)
        left(60)
        koch(n, w)

#tracer(0)
koch(300, 4)
done()