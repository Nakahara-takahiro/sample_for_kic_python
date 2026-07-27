import pygame
import random

# 初期化
pygame.init()

# 画面設定
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Star Catch Game")
clock = pygame.time.Clock()

# 色の設定
WHITE = (255, 255, 255)
YELLOW = (255, 220, 0)
BLUE = (50, 100, 255)
BLACK = (0, 0, 0)

# フォント設定
font = pygame.font.SysFont(None, 40)
star_font = pygame.font.SysFont(None, 80, bold=True)

# カゴ(プレイヤー)の設定
basket = pygame.Rect(WIDTH // 2 - 40, HEIGHT - 40, 40, 20)
basket_speed = 8

# 星(記号)の設定
star = pygame.Rect(random.randint(0, WIDTH - 20), 0, 20, 20)
star_speed = 10

# スコアと時間
score = 0
time_limit = 15  # 秒
start_ticks = pygame.time.get_ticks()

running = True
game_over = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        # キー入力の取得
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and basket.left > 0:
            basket.x -= basket_speed
        if keys[pygame.K_RIGHT] and basket.right < WIDTH:
            basket.x += basket_speed

        # 星を落とす
        star.y += star_speed

        # 星をキャッチしたとき
        if basket.colliderect(star):
            score += 1
            star.x = random.randint(0, WIDTH - 20)
            star.y = 0

        # 星が画面外に落ちたとき(取りこぼし)
        if star.y > HEIGHT:
            star.x = random.randint(0, WIDTH - 20)
            star.y = 0

        # 残り時間の計算
        elapsed = (pygame.time.get_ticks() - start_ticks) // 1000
        remaining = time_limit - elapsed
        if remaining <= 0:
            game_over = True

    # 描画処理
    screen.fill(BLACK)

    if not game_over:
        pygame.draw.rect(screen, BLUE, basket)
        # 星の代わりに「*」の文字を描画する
        screen.blit(star_font.render("*", True, YELLOW), (star.x, star.y))

        score_text = font.render(f"SCORE: {score}", True, WHITE)
        time_text = font.render(f"TIME: {remaining}", True, WHITE)
        screen.blit(score_text, (10, 10))
        screen.blit(time_text, (10, 50))
    else:
        over_text = font.render("GAME OVER", True, WHITE)
        final_text = font.render(f"RESULT: {score}", True, WHITE)
        screen.blit(over_text, (WIDTH // 2 - 100, HEIGHT // 2 - 40))
        screen.blit(final_text, (WIDTH // 2 - 100, HEIGHT // 2 + 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
