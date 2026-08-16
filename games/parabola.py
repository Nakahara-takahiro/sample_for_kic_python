import pygame
import math

# 画面の設定
pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("放物線投射シミュレーション")

# 色の設定
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# 重力加速度
gravity = 0.9

# 球体の初期設定
ball_radius = 10
ball_x = 100
ball_y = screen_height - ball_radius
ball_speed_x = 10
ball_speed_y = -15

# 球体の描画関数
def draw_ball(x, y):
    pygame.draw.circle(screen, red, (int(x), int(y)), ball_radius)

# ゲームループ
running = True
while running:
    # イベント処理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 球体の移動
    ball_x += ball_speed_x
    ball_speed_y += gravity
    ball_y += ball_speed_y

    # 球体が地面に当たった場合
    if ball_y + ball_radius > screen_height:
        ball_y = screen_height - ball_radius
        ball_speed_y = -ball_speed_y * 0.8  # 反発係数0.8

    # 画面をクリア
    screen.fill(black)

    # 球体を描画
    draw_ball(ball_x, ball_y)

    # 画面更新
    pygame.display.flip()

    # フレームレートを設定
    pygame.time.Clock().tick(60)

# Pygameを終了
pygame.quit()