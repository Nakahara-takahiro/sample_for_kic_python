from turtle import *


t = Turtle()
bgcolor('lightblue')
t.pencolor('pink')
t.speed(0)

for i in range(190):
    t.circle(190-i, 90)
    t.left(90)
    t.circle(190-i, 90)
    t.left(18)

done()