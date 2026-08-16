from turtle import *
colormode(255)
color((255,140,0), (50, 205, 50))
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()