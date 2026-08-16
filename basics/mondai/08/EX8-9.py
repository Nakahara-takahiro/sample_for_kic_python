import tkinter as tk
import random

card_im = ["h01.gif" , "h02.gif" , "h03.gif" , "h04.gif" , "h05.gif" , "h06.gif", "h07.gif", "h08.gif", "h09.gif", "h10.gif", "h11.gif", "h12.gif", "h13.gif"]

mform = tk.Tk()
canvas  = tk.Canvas(mform, width = 300, height = 300)
canvas.pack()

def draw_card():
    global im
    canvas.delete("all")
    i = random.randint(0 , 12)
    im = tk.PhotoImage(file = card_im[i])
    canvas.create_image(150, 150, image = im)

btn1 = tk.Button(mform, text = "カードを引く！",  font=("" , "20"), command = draw_card)
btn1.pack()

mform.mainloop()
