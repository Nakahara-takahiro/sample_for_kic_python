from turtle import *

def leaf(n, pencolor, brushcolor):
    def cir():
        for i in range(9):
            forward(n)
            right(10)

    a = heading()
    color(brushcolor)
    begin_fill()
    cir()
    right(90)
    cir()
    end_fill()

    setheading(a)
    color(pencolor)
    cir()
    right(90)
    cir()

def flower(x, y, size, color_set):
    up()
    goto(x, y)
    down()
    setheading(90)
    color(color_set[0])
    forward(size * 2)
    right(30)
    leaf(size, color_set[0], color_set[0])
    setheading(90)
    forward(size * 14)

    for i in range(9):
        leaf(size, color_set[1], color_set[2])
        right(10)
  
tracer(0)
flower(-100, -120, 7, ("lightgreen",  "mistyrose", "yellow"))
flower(0,    -120, 4, ("greenyellow", "lemonchiffon", "orange"))
flower(100,  -120, 8, ("palegreen", "paleturquoise", "pink"))
done()