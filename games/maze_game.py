import sys
import random
import time
from collections import deque

import pygame

# --------------- 設定 ---------------
WIDTH, HEIGHT = 960, 720
UI_HEIGHT = 78  # 上部UIの高さ
ROWS, COLS = 21, 31  # 迷路の行・列（奇数推奨）
WALL_THICK = 2  # 壁の線幅

BG_COLOR = (18, 18, 22)
MAZE_BG_COLOR = (28, 28, 36)
WALL_COLOR = (220, 220, 230)
PLAYER_COLOR = (255, 200, 60)
GOAL_COLOR = (80, 220, 120)
VISITED_COLOR = (70, 140, 250, 70)  # RGBA（訪問マスの半透明色）
SOLUTION_COLOR = (255, 100, 100)
HINT_COLOR = (255, 230, 60)

FPS = 60
RANDOM_SEED = None  # Noneで毎回ランダム。数値を入れると再現可能。

# 方向ビット（壁の有無をビットで管理）
N, E, S, W = 1, 2, 4, 8
DIRS = {N: (0, -1), E: (1, 0), S: (0, 1), W: (-1, 0)}
OPPOSITE = {N: S, S: N, E: W, W: E}


# --------------- 日本語フォント検出 ---------------
def choose_japanese_font():
    pygame.font.init()
    candidates = [
        # Windows
        "Meiryo", "Yu Gothic", "YuGothic", "MS Gothic", "MS PGothic",
        # macOS
        "Hiragino Sans", "Hiragino Kaku Gothic ProN",
        # Linux / cross-platform
        "Noto Sans CJK JP", "Noto Sans JP", "IPAGothic", "IPAexGothic",
        "TakaoPGothic", "Source Han Sans",
    ]
    for name in candidates:
        path = pygame.font.match_font(name, bold=False, italic=False)
        if path:
            return path
    return None  # 見つからなければpygame既定フォントにフォールバック


# --------------- 迷路生成（DFSバックトラック：完全迷路＝ループなし） ---------------
def index_of(x, y, cols):
    return y * cols + x


def inside(x, y, cols, rows):
    return 0 <= x < cols and 0 <= y < rows


def generate_maze(cols, rows, seed=None):
    """
    完全迷路（Perfect Maze）を生成します。
    → どの2点間にも経路はただ1つ（ループなし）。よってゴールへの複数経路は発生しません。
    """
    if seed is not None:
        random.seed(seed)
    cell_count = cols * rows
    walls = [N | E | S | W for _ in range(cell_count)]  # 全壁ありで開始
    visited = [False] * cell_count

    stack = []
    cx, cy = 0, 0
    visited[index_of(cx, cy, cols)] = True
    stack.append((cx, cy))

    while stack:
        cx, cy = stack[-1]
        neighbors = []
        for d, (dx, dy) in DIRS.items():
            nx, ny = cx + dx, cy + dy
            if inside(nx, ny, cols, rows) and not visited[index_of(nx, ny, cols)]:
                neighbors.append((d, nx, ny))
        if neighbors:
            d, nx, ny = random.choice(neighbors)
            ci = index_of(cx, cy, cols)
            ni = index_of(nx, ny, cols)
            # 壁を壊す（双方向）
            walls[ci] &= ~d
            walls[ni] &= ~OPPOSITE[d]
            visited[ni] = True
            stack.append((nx, ny))
        else:
            stack.pop()

    return walls


# --------------- 経路探索（BFSで最短経路） ---------------
def neighbors_open(x, y, cols, rows, walls):
    i = index_of(x, y, cols)
    w = walls[i]
    for d, (dx, dy) in DIRS.items():
        if (w & d) == 0:  # その方向に壁がない
            nx, ny = x + dx, y + dy
            if inside(nx, ny, cols, rows):
                yield nx, ny


def shortest_path_bfs(cols, rows, walls, start=(0, 0), goal=None):
    if goal is None:
        goal = (cols - 1, rows - 1)
    sx, sy = start
    gx, gy = goal
    q = deque()
    q.append((sx, sy))
    visited = {(sx, sy): None}

    while q:
        x, y = q.popleft()
        if (x, y) == (gx, gy):
            break
        for nx, ny in neighbors_open(x, y, cols, rows, walls):
            if (nx, ny) not in visited:
                visited[(nx, ny)] = (x, y)
                q.append((nx, ny))

    if (gx, gy) not in visited:
        return []
    # 経路復元
    path = []
    cur = (gx, gy)
    while cur is not None:
        path.append(cur)
        cur = visited[cur]
    path.reverse()
    return path


# --------------- 描画ヘルパ ---------------
def compute_cell_size_and_origin(width, height, ui_h, cols, rows):
    avail_w = width
    avail_h = height - ui_h
    cell = min(avail_w // cols, avail_h // rows)
    maze_w = cell * cols
    maze_h = cell * rows
    x0 = (avail_w - maze_w) // 2
    y0 = ui_h + (avail_h - maze_h) // 2
    return cell, x0, y0, maze_w, maze_h


def cell_rect(x, y, cell, x0, y0):
    return pygame.Rect(x0 + x * cell, y0 + y * cell, cell, cell)


def cell_center(x, y, cell, x0, y0):
    r = cell_rect(x, y, cell, x0, y0)
    return r.centerx, r.centery


# --------------- ゲーム本体 ---------------
class MazeGame:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("迷路ゲーム (Pygame)")
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()

        font_path = choose_japanese_font()
        if font_path:
            self.font = pygame.font.Font(font_path, 22)
            self.large_font = pygame.font.Font(font_path, 46)
        else:
            # フォールバック（日本語は四角になる場合があります）
            self.font = pygame.font.SysFont(None, 22)
            self.large_font = pygame.font.SysFont(None, 46, bold=True)

        self.cols = COLS
        self.rows = ROWS
        self.reset_all(new_maze=True)

    def reset_all(self, new_maze=True):
        # 迷路は毎回自動生成（R/Mでも新規）
        if new_maze:
            self.walls = generate_maze(self.cols, self.rows, seed=RANDOM_SEED)
            self.solution = shortest_path_bfs(self.cols, self.rows, self.walls)
        self.player = [0, 0]
        self.goal = (self.cols - 1, self.rows - 1)
        self.visited_cells = {tuple(self.player)}
        self.moves = 0
        self.start_time = time.time()
        self.cleared = False
        self.show_solution = False
        self.hint_flash = False
        self.hint_timer = 0.0
        self.hint_duration = 0.8  # 秒

        self.cell, self.x0, self.y0, self.maze_w, self.maze_h = compute_cell_size_and_origin(
            WIDTH, HEIGHT, UI_HEIGHT, self.cols, self.rows
        )
        self.visited_overlay = pygame.Surface((self.cell, self.cell), pygame.SRCALPHA)
        self.visited_overlay.fill(VISITED_COLOR)

    def try_move(self, dx, dy):
        if self.cleared:
            return
        x, y = self.player
        # 壁確認
        i = index_of(x, y, self.cols)
        d = None
        for k, (kdx, kdy) in DIRS.items():
            if (kdx, kdy) == (dx, dy):
                d = k
                break
        if d is None:
            return
        if (self.walls[i] & d) != 0:
            return
        nx, ny = x + dx, y + dy
        if not inside(nx, ny, self.cols, self.rows):
            return
        self.player = [nx, ny]
        self.moves += 1
        self.visited_cells.add((nx, ny))
        if (nx, ny) == self.goal:
            self.cleared = True
            self.clear_time = time.time() - self.start_time

    def handle_events(self):
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif ev.type == pygame.KEYDOWN:
                if ev.key in (pygame.K_ESCAPE, pygame.K_q):
                    pygame.quit()
                    sys.exit(0)
                elif ev.key == pygame.K_r:
                    self.reset_all(new_maze=True)  # Rで新しい迷路を自動生成
                elif ev.key == pygame.K_m:
                    self.reset_all(new_maze=True)  # Mも同じく新規生成
                elif ev.key == pygame.K_s:
                    self.show_solution = not self.show_solution
                elif ev.key == pygame.K_h:
                    self.hint_flash = True
                    self.hint_timer = 0.0
                elif ev.key == pygame.K_UP:
                    self.try_move(0, -1)
                elif ev.key == pygame.K_DOWN:
                    self.try_move(0, 1)
                elif ev.key == pygame.K_LEFT:
                    self.try_move(-1, 0)
                elif ev.key == pygame.K_RIGHT:
                    self.try_move(1, 0)

    def update(self, dt):
        if self.hint_flash:
            self.hint_timer += dt
            if self.hint_timer >= self.hint_duration:
                self.hint_flash = False
                self.hint_timer = 0.0

    def draw_ui(self):
        pygame.draw.rect(self.screen, (12, 12, 16), (0, 0, WIDTH, UI_HEIGHT))
        elapsed = 0.0 if self.cleared else (time.time() - self.start_time)

        ttext = f"時間: {elapsed:5.2f} 秒"
        mtext = f"歩数: {self.moves}"
        inst = "矢印:移動  S:解答表示  H:ヒント  R/M:新しい迷路  Q/Esc:終了"

        t_img = self.font.render(ttext, True, (230, 230, 235))
        m_img = self.font.render(mtext, True, (230, 230, 235))
        i_img = self.font.render(inst, True, (180, 180, 190))

        self.screen.blit(t_img, (16, 12))
        self.screen.blit(m_img, (16, 44))
        self.screen.blit(i_img, (320, 28))

    def draw_maze(self):
        # 迷路領域の背景
        pygame.draw.rect(self.screen, MAZE_BG_COLOR, (self.x0, self.y0, self.maze_w, self.maze_h))

        # 訪問マス
        for vx, vy in self.visited_cells:
            r = cell_rect(vx, vy, self.cell, self.x0, self.y0)
            self.screen.blit(self.visited_overlay, r.topleft)

        # 解答経路（任意表示）
        if self.show_solution and self.solution:
            pts = [cell_center(x, y, self.cell, self.x0, self.y0) for (x, y) in self.solution]
            if len(pts) >= 2:
                pygame.draw.lines(self.screen, SOLUTION_COLOR, False, pts, 3)

        # ヒント（次の一手）点滅
        if self.hint_flash and self.solution:
            try:
                idx = self.solution.index(tuple(self.player))
                if idx + 1 < len(self.solution):
                    nx, ny = self.solution[idx + 1]
                    cx, cy = cell_center(nx, ny, self.cell, self.x0, self.y0)
                    phase = (self.hint_timer / self.hint_duration)
                    radius = max(4, int(self.cell * (0.25 + 0.1 * abs(1 - 2 * phase))))
                    pygame.draw.circle(self.screen, HINT_COLOR, (cx, cy), radius, 0)
            except ValueError:
                pass

        # ゴール表示
        gx, gy = self.goal
        gr = cell_rect(gx, gy, self.cell, self.x0, self.y0)
        pad = max(2, self.cell // 8)
        goal_rect = pygame.Rect(gr.x + pad, gr.y + pad, gr.w - 2 * pad, gr.h - 2 * pad)
        pygame.draw.rect(self.screen, GOAL_COLOR, goal_rect, border_radius=6)

        # 壁（残っている壁だけ描画）
        for y in range(self.rows):
            for x in range(self.cols):
                i = index_of(x, y, self.cols)
                w = self.walls[i]
                r = cell_rect(x, y, self.cell, self.x0, self.y0)
                x1, y1, x2, y2 = r.left, r.top, r.right, r.bottom
                if w & N:
                    pygame.draw.line(self.screen, WALL_COLOR, (x1, y1), (x2, y1), WALL_THICK)
                if w & S:
                    pygame.draw.line(self.screen, WALL_COLOR, (x1, y2), (x2, y2), WALL_THICK)
                if w & W:
                    pygame.draw.line(self.screen, WALL_COLOR, (x1, y1), (x1, y2), WALL_THICK)
                if w & E:
                    pygame.draw.line(self.screen, WALL_COLOR, (x2, y1), (x2, y2), WALL_THICK)

        # プレイヤー
        px, py = self.player
        cx, cy = cell_center(px, py, self.cell, self.x0, self.y0)
        radius = max(6, self.cell // 3)
        pygame.draw.circle(self.screen, PLAYER_COLOR, (cx, cy), radius)

        # クリア表示
        if self.cleared:
            overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 140))
            self.screen.blit(overlay, (0, 0))
            msg = f"クリア！  時間: {self.clear_time:.2f} 秒  歩数: {self.moves}"
            m_img = self.large_font.render(msg, True, (255, 255, 255))
            sub = "R/M: 新しい迷路で再挑戦  |  Q/Esc: 終了"
            s_img = self.font.render(sub, True, (230, 230, 235))
            self.screen.blit(m_img, m_img.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 10)))
            self.screen.blit(s_img, s_img.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 36)))

    def run(self):
        while True:
            dt = self.clock.tick(FPS) / 1000.0
            self.handle_events()
            self.update(dt)
            self.screen.fill(BG_COLOR)
            self.draw_ui()
            self.draw_maze()
            pygame.display.flip()


def main():
    game = MazeGame()
    game.run()


if __name__ == "__main__":
    main()