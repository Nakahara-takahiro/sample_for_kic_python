import pygame
import sys
import random

# 初期化
pygame.init()

# 画面サイズ
WIDTH, HEIGHT = 500, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("スクロール付きレースゲーム")

# 色
WHITE = (255, 255, 255)
RED = (200, 0, 0)
GRAY = (50, 50, 50)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 200)

# プレイヤーの車
car_width, car_height = 50, 80
car_x = WIDTH // 2 - car_width // 2
car_y = HEIGHT - car_height - 20
car_speed = 5

# 障害物
obstacle_width, obstacle_height = 50, 80
obstacles = []
obstacle_speed = 5
spawn_interval = 60  # フレームごと（1秒に約1回）

# 背景スクロール
road_y = 0
road_speed = 5

# 時計
clock = pygame.time.Clock()
frame_count = 0

while True:
    # イベント処理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # キー入力
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_x > 120:  # 道路の左端制限
        car_x -= car_speed
    if keys[pygame.K_RIGHT] and car_x < WIDTH - 120 - car_width:  # 道路の右端制限
        car_x += car_speed

    # 背景スクロール
    road_y += road_speed
    if road_y >= HEIGHT:
        road_y = 0

    # 障害物生成
    frame_count += 1
    if frame_count % spawn_interval == 0:
        obs_x = random.randint(130, WIDTH - 130 - obstacle_width)
        obs_y = -obstacle_height
        obstacles.append([obs_x, obs_y])

    # 障害物移動
    for obs in obstacles:
        obs[1] += obstacle_speed

    # 古い障害物を削除
    obstacles = [obs for obs in obstacles if obs[1] < HEIGHT]

    # 描画
    screen.fill(GRAY)  # 背景色

    # 道路
    pygame.draw.rect(screen, (30, 30, 30), (100, 0, WIDTH - 200, HEIGHT))
    # 中央線（スクロール対応）
    for i in range(0, HEIGHT * 2, 60):
        pygame.draw.rect(screen, YELLOW, (WIDTH // 2 - 5, i + road_y, 10, 30))

    # プレイヤー車
    pygame.draw.rect(screen, RED, (car_x, car_y, car_width, car_height))

    # 障害物
    for obs in obstacles:
        pygame.draw.rect(screen, BLUE, (obs[0], obs[1], obstacle_width, obstacle_height))

    # 衝突判定
    car_rect = pygame.Rect(car_x, car_y, car_width, car_height)
    for obs in obstacles:
        obs_rect = pygame.Rect(obs[0], obs[1], obstacle_width, obstacle_height)
        if car_rect.colliderect(obs_rect):
            print("GAME OVER!")
            pygame.quit()
            sys.exit()

    # 画面更新
    pygame.display.flip()
    clock.tick(60)
