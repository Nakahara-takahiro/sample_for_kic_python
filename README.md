# sample_for_kic_python
光都ICTクラブで使っているPythonのサンプルプログラム

# 使い方
* 用途ごとのディレクトリにサンプルプログラムを入れています。
* プログラミングクラブの説明用として作ったプログラムです。
* PC上のPython（3系）で動かす前提です。

```
python games/life_game.py
```

* pygameを使うプログラムは、事前にインストールが必要です。

```
pip install pygame
```

# ディレクトリの説明
| ディレクトリ | 説明 |
|---------|--------|
|basics|Pythonの基礎教材（03〜08章）。`mondai/` は練習問題|
|games|tkinter / turtle / pygame で作ったゲーム|
|turtle|タートルグラフィックス。フラクタルや模様を描くプログラム|
|data|データ処理・Webスクレイピング・CSVの読み書き|
|office|Wordファイル（docx）の読み書き|

# 主なサンプルプログラム

## tkinterの練習用
| ファイル | 説明 |
|---------|--------|
|[games/life_game.py](games/life_game.py)|ライフゲーム|
|[games/dice/dice.py](games/dice/dice.py)|サイコロ|
|[games/block-ball.py](games/block-ball.py)|ブロック崩し|
|[games/omikuji.py](games/omikuji.py)|おみくじ|
|[games/window.py](games/window.py)|電卓のウィンドウを作るサンプル|

## turtleの練習用
| ファイル | 説明 |
|---------|--------|
|[games/snake_game.py](games/snake_game.py)|スネークゲーム|
|[turtle/koch.py](turtle/koch.py)|コッホ曲線|
|[turtle/tree.py](turtle/tree.py)|樹形図|
|[turtle/flower.py](turtle/flower.py)|花の模様|
|[turtle/random_walk.py](turtle/random_walk.py)|ランダムウォーク|

## pygameの練習用
| ファイル | 説明 |
|---------|--------|
|[games/star_get_game.py](games/star_get_game.py)|星キャッチゲーム|
|[games/fruits_slot.py](games/fruits_slot.py)|フルーツスロット|
|[games/race.py](games/race.py)|レースゲーム|
|[games/maze_game.py](games/maze_game.py)|迷路ゲーム|
|[games/whack-a-mole_game.py](games/whack-a-mole_game.py)|モグラたたき|
|[games/mine_sweeper/main.py](games/mine_sweeper/main.py)|マインスイーパ|
|[games/parabola.py](games/parabola.py)|放物線のシミュレーション|

## データ処理の練習用
| ファイル | 説明 |
|---------|--------|
|[data/scraping_sample.py](data/scraping_sample.py)|Webページから情報を取り出すサンプル|
|[data/kabuka.py](data/kabuka.py)|株価の計算問題|
|[office/do.py](office/do.py)|Wordファイルを読み込むサンプル|

# 注意
* `games/pygame_tkinter` は、クラブで作ったゲームをまとめたディレクトリです。
* 市販教材のダウンロード素材は、著作権のためこのリポジトリには含めていません。

# ライセンス
ライセンスについてはLICENSE参照のこと
