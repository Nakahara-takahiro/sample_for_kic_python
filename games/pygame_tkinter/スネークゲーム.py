import pygame
import random
import time


while True:

    # ゲームの初期化
    pygame.init()

    # ゲーム画面のサイズ
    width, height = 300, 300
    screen = pygame.display.set_mode((width, height))

    # フォントの初期化
    pygame.font.init()
    font = pygame.font.SysFont(None, 30)

    # スコアの初期化
    score = 0

    # スネークの初期位置と移動方向
    snake_x = width // 2
    snake_y = height // 2
    snake_dx = 10  # スネークの移動速度を調整
    snake_dy = 0

    # スネークの体の部分を管理するリスト
    snake_body = [(snake_x, snake_y)]

    # エサの位置
    food_x = random.randint(0, width - 10)
    food_y = random.randint(0, height - 10)

    # ゲームループ
    running = True
    game_over = False
    clock = pygame.time.Clock()
    while running:
        clock.tick(15)  # ゲームのフレームレートを設定

        # イベントの処理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake_dy != 10:  # 上方向に移動中は下方向には移動しない
                    snake_dx = 0
                    snake_dy = -10
                elif event.key == pygame.K_DOWN and snake_dy != -10:  # 下方向に移動中は上方向には移動しない
                    snake_dx = 0
                    snake_dy = 10
                elif event.key == pygame.K_LEFT and snake_dx != 10:  # 左方向に移動中は右方向には移動しない
                    snake_dx = -10
                    snake_dy = 0
                elif event.key == pygame.K_RIGHT and snake_dx != -10:  # 右方向に移動中は左方向には移動しない
                    snake_dx = 10
                    snake_dy = 0

        if not game_over:
            # スネークの位置を更新
            snake_x += snake_dx
            snake_y += snake_dy

            # スネークが画面外に出たか判定
            if snake_x < 0 or snake_x >= width or snake_y < 0 or snake_y >= height:
                game_over = True

            # スネークが自分自身に衝突したか判定
            if (snake_x, snake_y) in snake_body[:-1]:
                game_over = True

            # スネークの頭の位置をリストに追加
            snake_body.append((snake_x, snake_y))

            # エサを食べたか判定
            if snake_x > food_x-10 and snake_x < food_x+10 and snake_y > food_y-10 and snake_y < food_y+10:
                # スコアを増加させる
                score += 1

                # 新しいエサの位置を生成
                food_x = random.randint(0, width - 10)
                food_y = random.randint(0, height - 10)
            else:
                # スネークの体の最後の部分を削除
                snake_body = snake_body[1:]

            # 画面をクリア
            screen.fill((0, 0, 0))

            # スネークを描画
            for segment in snake_body:
                pygame.draw.rect(screen, (255, 255, 255), (segment[0], segment[1], 10, 10))

            # エサを描画
            pygame.draw.rect(screen, (255, 0, 0), (food_x, food_y, 10, 10))

            # スコアを描画
            score_text = font.render("Score: " + str(score), True, (255, 255, 255))
            screen.blit(score_text, (10, 10))

            # ゲームオーバー時の処理
            if game_over:
                game_over_text = font.render("Game Over", True, (255, 255, 255))
                screen.blit(game_over_text, (width // 2 - game_over_text.get_width() // 2, height // 2 - game_over_text.get_height() // 2))

            # 画面の更新
            pygame.display.flip()

            # ゲームオーバー時の待機
            if game_over:
                time.sleep(2)
                running = False