import pygame
import sys

# Pygameの初期化
pygame.init()

# 画面設定
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Count Up Game")

# 色の定義
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# フォント設定
font = pygame.font.Font(None, 36)

class CountUpGame:
    def __init__(self):
        self.player1_count = 0
        self.player2_count = 0
        self.player1_last_key = None
        self.player2_last_key = None
        self.game_started = False
        self.game_over = False
        self.winner = None

    def reset(self):
        self.__init__()

    def update(self, event):
        if not self.game_started:
            # ゲームスタート
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.game_started = True
            return

        if self.game_over:
            # ゲーム終了後のリセット
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.reset()
            return

        # プレイヤー1の入力処理
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                if self.player1_last_key != pygame.K_a:
                    self.player1_count += 1
                    self.player1_last_key = pygame.K_a
                else:
                    self.player1_count -= 0.5
            elif event.key == pygame.K_s:
                if self.player1_last_key != pygame.K_s:
                    self.player1_count += 1
                    self.player1_last_key = pygame.K_s
                else:
                    self.player1_count -= 0.5

            # プレイヤー2の入力処理
            if event.key == pygame.K_k:
                if self.player2_last_key != pygame.K_k:
                    self.player2_count += 1
                    self.player2_last_key = pygame.K_k
                else:
                    self.player2_count -= 0.5
            elif event.key == pygame.K_l:
                if self.player2_last_key != pygame.K_l:
                    self.player2_count += 1
                    self.player2_last_key = pygame.K_l
                else:
                    self.player2_count -= 0.5

        # 勝利判定
        if self.player1_count >= 200:
            self.game_over = True
            self.winner = "Player 1"
        elif self.player2_count >= 200:
            self.game_over = True
            self.winner = "Player 2"

    def draw(self, screen):
        screen.fill(WHITE)

        if not self.game_started:
            start_text = font.render("Press SPACE to start", True, BLACK)
            screen.blit(start_text, (WIDTH//2 - start_text.get_width()//2, HEIGHT//2))
        elif self.game_over:
            winner_text = font.render(f"{self.winner} Wins!", True, BLACK)
            restart_text = font.render("Press SPACE to restart", True, BLACK)
            screen.blit(winner_text, (WIDTH//2 - winner_text.get_width()//2, HEIGHT//2 - 50))
            screen.blit(restart_text, (WIDTH//2 - restart_text.get_width()//2, HEIGHT//2 + 50))
        else:
            # プレイヤー1のプログレスバー
            pygame.draw.rect(screen, RED, (50, 100, self.player1_count * 3.5, 30))
            player1_text = font.render(f"Player 1: {int(self.player1_count)}", True, BLACK)
            screen.blit(player1_text, (50, 50))

            # プレイヤー2のプログレスバー
            pygame.draw.rect(screen, BLUE, (50, 200, self.player2_count * 3.5, 30))
            player2_text = font.render(f"Player 2: {int(self.player2_count)}", True, BLACK)
            screen.blit(player2_text, (50, 250))

            # 操作説明
            keys_text1 = font.render("Player 1: A, S", True, BLACK)
            keys_text2 = font.render("Player 2: K, L", True, BLACK)
            screen.blit(keys_text1, (50, 300))
            screen.blit(keys_text2, (50, 350))

# メインゲームループ
def main():
    game = CountUpGame()
    clock = pygame.time.Clock()

    # メインループ
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            game.update(event)

        game.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()