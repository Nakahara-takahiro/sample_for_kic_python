from turtle import *
 
colormode(255)
 
t = Turtle()
t.speed(10)
for i in range(50):
    r = 255 - i * 2
    g = i * 2
    b = 128 + i * 2
    t.pencolor(r, g, b)
    t.forward(100 + 5 * i)
    t.right(144)

done()