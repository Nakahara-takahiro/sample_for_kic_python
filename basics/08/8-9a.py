import tkinter as tk
import random

dice_im = ["d01.gif" , "d02.gif" , "d03.gif" , "d04.gif" , "d05.gif" , "d06.gif"]

mform = tk.Tk()
canvas  = tk.Canvas(mform, width = 300, height = 300)
canvas.pack()

def load_dice():
    global im
    canvas.delete("all")
    i = random.randint(0 , 5)
    im = tk.PhotoImage(file = dice_im[i])
    canvas.create_image(150, 150, image = im)

btn1 = tk.Button(mform, text = "サイコロをふる！",  font=("" , "20"), command = load_dice)
btn1.pack()

mform.mainloop()
