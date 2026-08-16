"""
疑似3Dレースゲーム - オーバルコース
操作方法:
  ↑キー: 加速
  ↓キー: ブレーキ
  ←→キー: ステアリング
  ESCキー: 終了
"""

import pygame
import math
import sys

# 初期化
pygame.init()

# 定数
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# 色定義
SKY_BLUE = (135, 206, 235)
GRASS_GREEN = (34, 139, 34)
ROAD_GRAY = (100, 100, 100)
ROAD_DARK = (80, 80, 80)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GRAY = (120, 120, 120)

# ゲーム設定
ROAD_WIDTH = 2000
CAMERA_HEIGHT = 1000
DRAW_DISTANCE = 300
SEGMENT_LENGTH = 200

# プレイヤー設定
MAX_SPEED = 200
ACCELERATION = 50
DECELERATION = 40
BRAKE_POWER = 80
STEERING_SPEED = 2.0


class Segment:
    """道路セグメント"""
    def __init__(self, index, curve=0, y=0):
        self.index = index
        self.curve = curve  # カーブの強さ
        self.y = y  # 高さ
        self.z = index * SEGMENT_LENGTH  # Z座標（前後位置）
        
        # ワールド座標（ミニマップ用）
        self.world_x = 0
        self.world_y = 0
        self.angle = 0
        
        # 描画用
        self.clip = 0
        self.color = ROAD_GRAY if (index // 3) % 2 == 0 else ROAD_DARK


class Circuit:
    """サーキットコース"""
    def __init__(self):
        self.segments = []
        self.total_length = 0
        
    def create_oval_track(self):
        """オーバルトラックを生成（小学校の校庭のような形）"""
        # ストレート1（ホームストレート）
        for i in range(50):
            self.segments.append(Segment(len(self.segments), curve=0))
        
        # コーナー1（右カーブ）
        for i in range(40):
            self.segments.append(Segment(len(self.segments), curve=0.015))
        
        # ストレート2（バックストレート）
        for i in range(50):
            self.segments.append(Segment(len(self.segments), curve=0))
        
        # コーナー2（右カーブ）
        for i in range(40):
            self.segments.append(Segment(len(self.segments), curve=0.015))
        
        self.total_length = len(self.segments) * SEGMENT_LENGTH
        self._calculate_world_coordinates()
    
    def _calculate_world_coordinates(self):
        """ミニマップ用のワールド座標を計算"""
        x, y = 0, 0
        angle = 0
        
        for seg in self.segments:
            seg.world_x = x
            seg.world_y = y
            seg.angle = angle
            
            # 次のセグメントの位置を計算
            x += math.cos(angle) * SEGMENT_LENGTH
            y += math.sin(angle) * SEGMENT_LENGTH
            
            # 角度の更新（カーブの影響）
            angle += seg.curve * SEGMENT_LENGTH
    
    def get_segment(self, z):
        """Z座標からセグメントを取得"""
        index = int(z / SEGMENT_LENGTH) % len(self.segments)
        return self.segments[index]


class Player:
    """プレイヤー"""
    def __init__(self, circuit):
        self.circuit = circuit
        self.z = 0  # コース上の位置
        self.x = 0  # 横位置（-1.0 ~ 1.0）
        self.speed = 0
        self.lap = 0
        self.lap_start_z = 0
        
    def update(self, dt, keys):
        """プレイヤーの状態を更新"""
        # 加速・減速
        if keys[pygame.K_UP]:
            self.speed += ACCELERATION * dt
        elif keys[pygame.K_DOWN]:
            self.speed -= BRAKE_POWER * dt
        else:
            # 自然減速
            if self.speed > 0:
                self.speed -= DECELERATION * dt
            elif self.speed < 0:
                self.speed += DECELERATION * dt
        
        # 速度制限
        self.speed = max(-MAX_SPEED / 2, min(MAX_SPEED, self.speed))
        
        # 前進
        old_z = self.z
        self.z += self.speed * dt
        
        # ラップカウント
        if old_z < self.circuit.total_length and self.z >= self.circuit.total_length:
            self.lap += 1
            self.lap_start_z = self.z
        
        # コース範囲内に収める
        while self.z >= self.circuit.total_length:
            self.z -= self.circuit.total_length
        while self.z < 0:
            self.z += self.circuit.total_length
        
        # カーブの影響（何もしないとコースアウト）
        segment = self.circuit.get_segment(self.z)
        self.x += segment.curve * self.speed * 0.001 * dt
        
        # ステアリング
        if keys[pygame.K_LEFT]:
            self.x -= STEERING_SPEED * dt
        if keys[pygame.K_RIGHT]:
            self.x += STEERING_SPEED * dt
        
        # コース幅制限とコースアウト判定
        if abs(self.x) > 1.0:
            self.x = max(-1.0, min(1.0, self.x))
            self.speed *= 0.5  # コースアウトで減速
    
    def get_world_position(self):
        """ミニマップ用のワールド座標を取得"""
        segment_index = int(self.z / SEGMENT_LENGTH) % len(self.circuit.segments)
        seg = self.circuit.segments[segment_index]
        next_seg = self.circuit.segments[(segment_index + 1) % len(self.circuit.segments)]
        
        # セグメント内の進行度
        progress = (self.z % SEGMENT_LENGTH) / SEGMENT_LENGTH
        
        # 補間
        world_x = seg.world_x * (1 - progress) + next_seg.world_x * progress
        world_y = seg.world_y * (1 - progress) + next_seg.world_y * progress
        
        # 横方向のオフセット
        angle = seg.angle
        world_x += math.cos(angle + math.pi/2) * self.x * 20
        world_y += math.sin(angle + math.pi/2) * self.x * 20
        
        return world_x, world_y, seg.angle


class Minimap:
    """ミニマップ"""
    def __init__(self, circuit, position, size):
        self.circuit = circuit
        self.x, self.y = position
        self.width, self.height = size
        
        # コースの範囲を計算
        all_x = [seg.world_x for seg in circuit.segments]
        all_y = [seg.world_y for seg in circuit.segments]
        
        self.min_x = min(all_x)
        self.max_x = max(all_x)
        self.min_y = min(all_y)
        self.max_y = max(all_y)
        
        # スケール計算
        margin = 1.2
        world_width = (self.max_x - self.min_x) * margin
        world_height = (self.max_y - self.min_y) * margin
        
        self.scale = min(self.width / world_width, self.height / world_height)
    
    def world_to_minimap(self, world_x, world_y):
        """ワールド座標をミニマップ座標に変換"""
        center_x = (self.min_x + self.max_x) / 2
        center_y = (self.min_y + self.max_y) / 2
        
        map_x = self.x + self.width/2 + (world_x - center_x) * self.scale
        map_y = self.y + self.height/2 + (world_y - center_y) * self.scale
        
        return int(map_x), int(map_y)
    
    def draw(self, screen, player):
        """ミニマップを描画"""
        # 背景
        pygame.draw.rect(screen, (40, 40, 40), (self.x, self.y, self.width, self.height))
        pygame.draw.rect(screen, WHITE, (self.x, self.y, self.width, self.height), 2)
        
        # コースライン
        points = []
        for seg in self.circuit.segments:
            map_x, map_y = self.world_to_minimap(seg.world_x, seg.world_y)
            points.append((map_x, map_y))
        
        if len(points) > 2:
            pygame.draw.lines(screen, GRAY, True, points, 2)
        
        # プレイヤー位置
        player_world_x, player_world_y, angle = player.get_world_position()
        player_map_x, player_map_y = self.world_to_minimap(player_world_x, player_world_y)
        
        # プレイヤーの向き（三角形）
        arrow_length = 8
        p1_x = player_map_x + math.cos(angle) * arrow_length
        p1_y = player_map_y + math.sin(angle) * arrow_length
        p2_x = player_map_x + math.cos(angle + 2.5) * arrow_length * 0.5
        p2_y = player_map_y + math.sin(angle + 2.5) * arrow_length * 0.5
        p3_x = player_map_x + math.cos(angle - 2.5) * arrow_length * 0.5
        p3_y = player_map_y + math.sin(angle - 2.5) * arrow_length * 0.5
        
        pygame.draw.polygon(screen, RED, [
            (int(p1_x), int(p1_y)),
            (int(p2_x), int(p2_y)),
            (int(p3_x), int(p3_y))
        ])


class Game:
    """ゲームメイン"""
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("疑似3Dレースゲーム - オーバルコース")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)
        
        # コース生成
        self.circuit = Circuit()
        self.circuit.create_oval_track()
        
        # プレイヤー
        self.player = Player(self.circuit)
        
        # ミニマップ
        self.minimap = Minimap(self.circuit, position=(600, 20), size=(180, 180))
        
    def project_3d(self, segment, camera_x, camera_y, camera_z, camera_curve):
        """3D座標を2D画面座標に投影"""
        # カメラからの相対位置
        z = segment.z - camera_z
        
        if z <= 0:
            return None
        
        # スケール計算（遠近法）
        scale = CAMERA_HEIGHT / z
        
        # 画面座標
        # カーブの累積を考慮
        curve_offset = (segment.curve - camera_curve)
        x = SCREEN_WIDTH / 2 + scale * curve_offset * SCREEN_WIDTH
        y = SCREEN_HEIGHT / 2 + scale * (camera_y - segment.y)
        w = scale * ROAD_WIDTH
        
        return {
            'x': x,
            'y': y,
            'w': w,
            'scale': scale,
            'clip': segment.clip
        }
    
    def draw_segment(self, segment_proj, prev_proj, color):
        """セグメントを台形として描画"""
        if not segment_proj or not prev_proj:
            return
        
        # 台形の座標
        x1 = segment_proj['x']
        y1 = segment_proj['y']
        w1 = segment_proj['w']
        
        x2 = prev_proj['x']
        y2 = prev_proj['y']
        w2 = prev_proj['w']
        
        # 画面外チェック
        if y1 > SCREEN_HEIGHT or y2 < 0:
            return
        
        # Y座標をクリップ
        y1 = max(0, min(SCREEN_HEIGHT, y1))
        y2 = max(0, min(SCREEN_HEIGHT, y2))
        
        # 草地（背景）
        if y1 != y2:
            points_grass = [
                (0, int(y2)),
                (SCREEN_WIDTH, int(y2)),
                (SCREEN_WIDTH, int(y1)),
                (0, int(y1))
            ]
            pygame.draw.polygon(self.screen, GRASS_GREEN, points_grass)
        
        # 道路
        points_road = [
            (int(x2 - w2), int(y2)),
            (int(x2 + w2), int(y2)),
            (int(x1 + w1), int(y1)),
            (int(x1 - w1), int(y1))
        ]
        
        # ポリゴンが有効かチェック
        if w1 > 0 and w2 > 0 and y1 != y2:
            pygame.draw.polygon(self.screen, color, points_road)
            
            # 中央ライン（点線）
            line_w1 = w1 / 20
            line_w2 = w2 / 20
            if segment_proj['clip'] % 4 < 2:  # 点線効果
                points_line = [
                    (int(x2 - line_w2), int(y2)),
                    (int(x2 + line_w2), int(y2)),
                    (int(x1 + line_w1), int(y1)),
                    (int(x1 - line_w1), int(y1))
                ]
                pygame.draw.polygon(self.screen, YELLOW, points_line)
    
    def draw_3d_view(self):
        """疑似3D視点を描画"""
        # 空
        pygame.draw.rect(self.screen, SKY_BLUE, (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT // 2))
        
        # 地面
        pygame.draw.rect(self.screen, GRASS_GREEN, (0, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT // 2))
        
        # カメラ位置
        camera_z = self.player.z
        camera_x = self.player.x
        camera_y = CAMERA_HEIGHT
        
        # 現在のセグメント
        base_segment = self.circuit.get_segment(camera_z)
        
        # カーブの累積計算
        camera_curve = 0
        
        # 遠くから手前に描画
        prev_proj = None
        
        for n in range(DRAW_DISTANCE, 0, -1):
            current_z = camera_z + n * SEGMENT_LENGTH
            segment = self.circuit.get_segment(current_z)
            segment.clip = n
            
            # カーブの累積を更新
            if n < DRAW_DISTANCE:
                camera_curve += segment.curve
            
            proj = self.project_3d(segment, camera_x, camera_y, camera_z, camera_curve)
            
            if proj and prev_proj:
                self.draw_segment(proj, prev_proj, segment.color)
            
            if proj:
                prev_proj = proj
    
    def draw_ui(self):
        """UI描画"""
        # 速度表示
        speed_text = self.font.render(f"SPEED: {int(abs(self.player.speed))} km/h", True, WHITE)
        self.screen.blit(speed_text, (20, 20))
        
        # ラップ表示
        lap_text = self.font.render(f"LAP: {self.player.lap + 1}", True, WHITE)
        self.screen.blit(lap_text, (20, 60))
        
        # 横位置インジケーター（コースアウト警告）
        if abs(self.player.x) > 0.7:
            warning_text = self.font.render("WARNING: COURSE OUT!", True, RED)
            self.screen.blit(warning_text, (SCREEN_WIDTH // 2 - 150, 100))
        
        # 操作説明
        controls = [
            "UP: Accelerate",
            "DOWN: Brake",
            "LEFT/RIGHT: Steer",
            "ESC: Quit"
        ]
        for i, text in enumerate(controls):
            control_text = self.small_font.render(text, True, WHITE)
            self.screen.blit(control_text, (20, SCREEN_HEIGHT - 100 + i * 25))
        
        # ミニマップ
        self.minimap.draw(self.screen, self.player)
        
        # ミニマップラベル
        minimap_label = self.small_font.render("MINIMAP", True, WHITE)
        self.screen.blit(minimap_label, (self.minimap.x, self.minimap.y - 20))
    
    def run(self):
        """メインループ"""
        running = True
        
        while running:
            dt = self.clock.tick(FPS) / 1000.0
            
            # イベント処理
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
            
            # キー入力
            keys = pygame.key.get_pressed()
            
            # 更新
            self.player.update(dt, keys)
            
            # 描画
            self.draw_3d_view()
            self.draw_ui()
            
            pygame.display.flip()
        
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    game = Game()
    game.run()