import turtle
import random

# ウィンドウの設定
window = turtle.Screen()
window.title("Turtle Graphics")
window.bgcolor("white")

# タートルの設定
pen = turtle.Turtle()
pen.speed(10)  # 描画速度 (1 から 10 までの値)

# 円を重ねて複雑な模様を作成
num_angle = random.randrange(12, 37)
circle_size = random.randrange(50, 101)
angle_change = 360 / num_angle

for _ in range(num_angle):
    pen.right(angle_change)
    pen.circle(circle_size)

# 塗りつぶしの色をランダムに設定
pencolor = (random.random(), random.random(), random.random())
fillcolor = (random.random(), random.random(), random.random())
pen.color(pencolor, fillcolor)

# 塗りつぶしを開始
pen.begin_fill()

# 円を重ねて複雑な模様を作成
for _ in range(num_angle):
    pen.right(angle_change)
    pen.circle(circle_size)

# 塗りつぶしを終了
pen.end_fill()

# 終了処理
window.exitonclick()
