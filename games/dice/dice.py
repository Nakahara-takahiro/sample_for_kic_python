import tkinter
import random


#プログラムで使う設定値を定義する（はじまり）//////////////////////////////////////////////////
#画面幅高さ
WIDTH = 300
HEIGHT = 300

#画面中央の座標
CENTER_X = WIDTH/2
CENTER_Y = HEIGHT/2

#目のセンター座標を指定する
CENTER_POINT = [[CENTER_X - WIDTH/6, CENTER_Y - HEIGHT/6], #1の場所の○のセンター座標
               [CENTER_X + WIDTH/6, CENTER_Y - HEIGHT/6], #2の場所の○のセンター座標
               [CENTER_X - WIDTH/6, CENTER_Y],            #3の場所の○のセンター座標
               [CENTER_X, CENTER_Y],                      #4の場所の○のセンター座標
               [CENTER_X + WIDTH/6, CENTER_Y],            #5の場所の○のセンター座標
               [CENTER_X - WIDTH/6, CENTER_Y + HEIGHT/6], #6の場所の○のセンター座標
               [CENTER_X + WIDTH/6, CENTER_Y + HEIGHT/6]] #7の場所の○のセンター座標

#1～6の数字に対応した目を配列で指定する
POINT_NUM =[[3], [0,6], [0, 3, 6], [0, 1, 5, 6], [0, 1, 3, 5, 6], [0, 1, 2, 4, 5, 6]]

#プログラムで使う設定値を定義（おわり）//////////////////////////////////////////////////////


#プログラムで使う関数を定義（はじまり）///////////////////////////////////////////////////////
#サイコロを表示する関数
def num_circle(num):

    if num==1:
        color='red'
    else:
        color='black'
        
    canvas.delete('all')
    canvas.create_rectangle(CENTER_X-100, CENTER_Y-100, \
                        CENTER_X+100, CENTER_Y+100, fill='white')

    for pin in POINT_NUM[num-1]:
        canvas.create_oval(CENTER_POINT[pin][0]-20, CENTER_POINT[pin][1]-20,
                           CENTER_POINT[pin][0]+20, CENTER_POINT[pin][1]+20,
                           fill=color, outline=color)

# ボタンが押された時の処理をする関数
def dice():
    # ランダムな整数を生成して、表示する
    num_circle(random.randint(1,6))
#プログラムで使う関数を定義（おわり）/////////////////////////////////////////////////////////



#プログラム本文（はじまり）//////////////////////////////////////////////////////////////////
if __name__ == '__main__':
    app = tkinter.Tk()
    canvas = tkinter.Canvas(app, width=WIDTH, height=HEIGHT)
    canvas.pack()

    # ボタンの設定
    Btn = tkinter.Button(text='サイコロをふる', font=('', '12'), command=dice)
    Btn.pack()

    app.mainloop()
#プログラム本文（おわり）/////////////////////////////////////////////////////////////////////
