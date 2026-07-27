import turtle
import random

# ---------- 画面の設定 ----------
screen = turtle.Screen()
screen.title("スネークゲーム スコア: 0")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)  # 自動更新をオフにして自分で制御する

# ---------- ヘビの頭 ----------
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# ---------- 食べ物 ----------
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# ---------- ヘビの胴体 ----------
segments = []
score = 0

# ---------- 方向を変える関数 ----------
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

# ---------- ヘビを動かす関数 ----------
def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    if head.direction == "down":
        head.sety(head.ycor() - 20)
    if head.direction == "left":
        head.setx(head.xcor() - 20)
    if head.direction == "right":
        head.setx(head.xcor() + 20)

# ---------- キー操作の登録 ----------
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")

# ---------- メインループ ----------
while True:
    screen.update()

    # 壁に当たったらゲームオーバー
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        head.goto(0, 0)
        head.direction = "stop"
        for seg in segments:
            seg.goto(1000, 1000)
        segments.clear()
        score = 0
        screen.title("スネークゲーム スコア: 0")

    # 食べ物に当たったら胴体を伸ばす
    if head.distance(food) < 20:
        x = random.randint(-14, 14) * 20
        y = random.randint(-14, 14) * 20
        food.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("green")
        new_segment.penup()
        segments.append(new_segment)

        score += 1
        screen.title("スネークゲーム スコア: " + str(score))

    # 胴体を1つ前の胴体の位置に移動（後ろから順番に）
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        segments[0].goto(head.xcor(), head.ycor())

    move()

    # 自分の胴体に当たったらゲームオーバー
    for seg in segments:
        if seg.distance(head) < 20:
            head.goto(0, 0)
            head.direction = "stop"
            for s in segments:
                s.goto(1000, 1000)
            segments.clear()
            score = 0
            screen.title("スネークゲーム スコア: 0")

    turtle.time.sleep(0.1)
    
