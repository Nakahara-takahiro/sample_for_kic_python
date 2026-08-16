from turtle import *

n = 150
length = 4
angle = 15

speed(0)
color('red', 'yellow')
begin_fill()
for _ in range(n):
    for _ in range(4):
        forward(length)
        left(90)
    left(angle)
    length = length*1.03
end_fill()

done()