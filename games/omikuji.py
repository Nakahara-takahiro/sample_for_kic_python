import tkinter as tk
import time
import random as rd

class Fortune():
    def __init__(self, canvas, x, y, color, tag):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.color = color
        self.tag = tag
    
    def create_fortune_box(self): #くじ箱を作る
        self.canvas.create_polygon([self.x, self.y], [self.x+20, self.y-25], [self.x+80, self.y-25], [self.x+100, self.y], 
                                   [self.x+100, self.y+100], [self.x+80, self.y+125], [self.x+20, self.y+125], [self.x, self.y+100], 
                                   fill=self.color, tag=self.tag)
        self.create_fortune_text()
    
    def create_fortune_text(self):#おみくじの文字を表示
        return self.canvas.create_text(self.x+50, self.y+50, text='お\nみ\nく\nじ', font=('Helvetica', 18, 'bold'), fill='white', tag=self.tag)

    def draw_lots(self):#くじ箱の動き
        sleep_time = 0.03
        movex = [0, -5, 0, 5]
        movey = [5, 0, -5, 0]
        for i in range(40):
            self.canvas.move(self.tag, movex[i % 4], movey[i % 4])
            time.sleep(sleep_time)
            self.canvas.update()

        self.result_lots()
    
    def result_lots(self):#結果を表示
        result_number=rd.randint(0, 27)

        result_texts = ['大\n吉', '吉', '吉', '中\n吉', '中\n吉', '中\n吉', '小\n吉','小\n吉','小\n吉','小\n吉',
                        '末\n吉','末\n吉','末\n吉','末\n吉','末\n吉', '凶','凶','凶','凶','凶','凶',
                        '大\n凶', '大\n凶', '大\n凶', '大\n凶', '大\n凶', '大\n凶', '大\n凶']
        result_colors = ['yellow', 'orange', 'orange', 'pink', 'pink', 'pink', 'green', 'green', 'green', 'green',
                    'blue', 'blue', 'blue', 'blue', 'blue', 'white', 'white', 'white', 'white', 'white', 'white',
                    'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray']
        self.canvas.create_polygon([self.x+25, self.y-50], [self.x+75, self.y-50], [self.x+75, self.y-25], [self.x+25, self.y-25], fill=result_colors[result_number], tag='lot')
        self.canvas.create_text(self.x+150, self.y, text=result_texts[result_number], font=('Helvetiaca', 30, 'bold'), fill=result_colors[result_number], tag='resultText')

class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        self.width=self.height=300
        self.button_click=True

        self.canvas = tk.Canvas(master, width=self.width, height=self.height, bg='black')#キャンバスの作成
        self.canvas.pack()

        self.omikuji = Fortune(self.canvas, 100, 90, 'red', 'omikuji')#インスタンスomikujiの生成
        self.omikuji.create_fortune_box()

        self.draw_button = tk.Button(text='くじを引く', command=self.draw_button_click, width=10)#くじを引くボタンの作成
        self.draw_button.place(x=110, y=250)
    
    def draw_button_click(self):#ボタンが押されたら
        if self.button_click:
            self.button_click=False
            self.canvas.delete('lot')
            self.canvas.delete('resultText')
            self.omikuji.draw_lots()
            self.button_click=True

def main():
    win = tk.Tk()
    app = Application(master=win)
    app.mainloop()

if __name__ == '__main__':
    main()