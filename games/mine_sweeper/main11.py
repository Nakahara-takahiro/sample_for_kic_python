import pygame
from os import walk
import random

pygame.init()

#タイルの設定
row_num = 20
col_num = 20
tile_size = 30
bomb_num = 50

#ウインドウの作成
screen_width = col_num * tile_size
screen_height = row_num * tile_size
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('mine sweeper')

#色の設定
BLACK =(0, 0, 0)
WHITE = (255, 255 ,255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#FPSの設定
FPS = 60
clock = pygame.time.Clock()

game_over = False
game_clear = False

#フォントの設定
font = pygame.font.SysFont(None, 100)
game_over_text = font.render('Game Over...', True, BLUE, GREEN)
game_clear_text = font.render('Game Clear', True, RED, GREEN)
reset_text = font.render('click to reset', True, BLACK, GREEN)

timer = 0

run = True
while run :
    
    #イベントの取得
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
    #更新
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()






