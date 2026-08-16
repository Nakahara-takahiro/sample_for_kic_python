import pygame
from tile import Tile
from os import walk
import random

pygame.init()

#関数---------------------------------------------------------------------------
def set_up():

    #フィールドの作成
    field = []
    for row in range(row_num):
        tile_list = []
        for col in range(col_num):
            tile = Tile((col * tile_size, row * tile_size), images["empty_block"])
            tile_list.append(tile)
        field.append(tile_list)
    
    return field
#-------------------------------------------------------------------------------

#タイルの設定
row_num = 20
col_num = 20
tile_size = 30
bomb_num = 50

#ウィンドウの作成
screen_width = col_num * tile_size
screen_height = row_num * tile_size
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("mine sweeper")

#色の設定
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#FPSの設定
FPS = 60
clock = pygame.time.Clock()

#画像の読み込み
images = {}
path = "assets/img"
for _, __, img_files in walk(path):
    for image in img_files:
        full_path = path + "/" + image
        img = pygame.image.load(full_path)
        img = pygame.transform.scale(img, (tile_size, tile_size))
        images[image.split(".")[0]] = img

field = set_up()

game_over = False
game_clear = False

#フォントの設定
font = pygame.font.SysFont(None, 100)
game_over_text = font.render("Game Over...", True, BLUE, GREEN)
game_clear_text = font.render("Game Clear", True, RED, GREEN)
reset_text = font.render("click to reset", True, BLACK, GREEN)

timer = 0

#メインループ=======================================================================
run = True
while run:

    #背景の塗りつぶし
    screen.fill(WHITE)

    #タイルの描画
    open_num = 0
    for tile_list in field:
        for tile in tile_list:
            if tile.open:
                if tile.bomb:
                    tile.image = images["click_bomb"]
                else:
                    tile.image = images[f"{tile.neighbor_bomb_num}"]
            screen.blit(tile.image, tile.position)

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

#===============================================================================

pygame.quit()

