from turtle import *

def move(x, y):
    up()
    goto(x, y)
    down()
  
def tree(length, level):
    if level > 0:
        x, y = position()
        a = heading()
        # draw left node
        left(18)
        forward(length)
        tree(length-10, level-1)

        # draw right node
        move(x, y)
        setheading(a)
        right(18)
        forward(length)
        tree(length-10, level-1)

#tracer(0)
move(0, -100)
setheading(90)
tree(60, 5)
done()