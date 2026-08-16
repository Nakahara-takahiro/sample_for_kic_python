import tkinter
# メインウィンドウを生成する
root = tkinter.Tk()
# ウィンドウのタイトルを設定する
root.title("電卓サンプルプログラム")
# ウィンドウのサイズを設定する
root.geometry("400x600")
button_text = [['C', 'CA', '√', 'BS'],
               ['7', '8', '9', '÷'],
               ['4', '5', '6', '×'],
               ['1', '2', '3', '-'],
               ['0', '.', '=', '+']]

lab = tkinter.Label( root, text = "0", font=('',28),\
                     height= 2, width=15,\
                     relief="groove",anchor='e' )
lab.grid(row=0, column=0, columnspan=4 )

for i in range(5):
    for j in range(4):
        button = tkinter.Button(\
            root, \
            text=button_text[i][j],\
            width=10,\
            height=5)
        button.grid(row=i+1, column=j )

#button.pack()
# tkinterのイベントを処理する
root.mainloop()