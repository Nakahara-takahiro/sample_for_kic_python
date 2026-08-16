# life_simple.py
# ------------------------------------------
# クリックでセルをON/OFF
# スペースキーで再生 / 停止
# 0.5秒ごとに次の世代へ進む
# ------------------------------------------

import tkinter as tk
import random

# ===== 基本設定 =====
H, W = 20, 30        # 行と列
CELL = 20            # セル1つの大きさ（px）
INTERVAL = 500       # 更新間隔（ミリ秒）＝0.5秒

# ===== データ作成 =====
def new_board():
    """H×Wの盤面（すべて0）を作る"""
    return [[0 for _ in range(W)] for _ in range(H)]

def count_neighbors(b, r, c):
    """セル(r,c)の周囲の生セル数を数える"""
    n = 0
    for dr in (-1,0,1):
        for dc in (-1,0,1):
            if dr == 0 and dc == 0:  # 自分自身は除く
                continue
            n += b[(r+dr)%H][(c+dc)%W]  # トーラス境界（端はつながる）
    return n

def step(b):
    """次の世代を計算して返す"""
    nb = new_board()
    for r in range(H):
        for c in range(W):
            n = count_neighbors(b, r, c)
            if b[r][c] == 1 and n in (2,3):
                nb[r][c] = 1   # 生存
            elif b[r][c] == 0 and n == 3:
                nb[r][c] = 1   # 誕生
    return nb

# ===== 描画関数 =====
def draw():
    """盤面を画面に表示"""
    canvas.delete("all")
    for r in range(H):
        for c in range(W):
            if board[r][c] == 1:
                x0, y0 = c*CELL, r*CELL
                canvas.create_rectangle(x0, y0, x0+CELL, y0+CELL, fill="black", outline="")
    # グリッド線
    for r in range(H+1):
        canvas.create_line(0, r*CELL, W*CELL, r*CELL, fill="#cccccc")
    for c in range(W+1):
        canvas.create_line(c*CELL, 0, c*CELL, H*CELL, fill="#cccccc")

# ===== 操作関数 =====
def toggle_cell(event):
    """クリックしたマスを反転"""
    c = event.x // CELL
    r = event.y // CELL
    if 0 <= r < H and 0 <= c < W:
        board[r][c] ^= 1  # 0→1、1→0
        draw()

def toggle_pause(event=None):
    """スペースキーで開始/停止切り替え"""
    global paused
    paused = not paused

def update():
    """自動で次の世代に進める"""
    global board
    if not paused:
        board = step(board)
    draw()
    root.after(INTERVAL, update)  # 0.5秒ごとに繰り返す

# ===== メイン処理 =====
root = tk.Tk()
root.title("ライフゲーム")

canvas = tk.Canvas(root, width=W*CELL, height=H*CELL, bg="white")
canvas.pack()

# クリックとキー操作を登録
canvas.bind("<Button-1>", toggle_cell)
root.bind("<space>", toggle_pause)

# 盤面を作ってスタート
board = new_board()
paused = True  # 初期状態は停止

draw()
update()
root.mainloop()
