import tkinter as tk
import time

mform = tk.Tk()
mform.title("Count Down Timer")
mform.geometry("300x150")
canvas = tk.Canvas(mform , width = 300 , height = 150)
canvas.pack()
canvas.create_oval(5, 50, 80, 130, fill = "#000000" , tag = "syoukyo")

def onSlide(self):
    canvas.delete("kesu")
    canvas.create_text(160 , 35 , text = sld.get() , font = ("",30) , tag = "kesu")

def btnClick():
    global endTime
    endTime = time.time() + sld.get()
    mform.after(50 , genzan) 

def genzan():
    canvas.delete("kesu")

    lapTime = endTime - time.time()
    if lapTime > 0:
        canvas.create_text(160 , 35 , text = int(lapTime) , font = ("",30) , tag = "kesu")
        sld.set(lapTime)
        mform.after(50 , genzan)
    else:
        canvas.delete("syoukyo")
        canvas.create_text(160 , 35 , text = "爆発" , font = ("",30) , tag = "kesu")
        canvas.create_polygon(85, 20, 150, 80, 120, 150, 50, 150, 20, 80 , width = 3.0 , fill = "red")

var = tk.IntVar(master = mform , value = 3)
sld = tk.Scale(mform, orient = "h" , showvalue = False , variable = var , from_ = 1, to = 10 , length = 160 , command = onSlide)
sld.place(x = 75 , y = 75)
btn = tk.Button(mform , text = "スタート" , command = btnClick , width = 8 , font = ("",14))
btn.place(x = 110 , y = 110)
canvas.create_text(160 , 35 , text = sld.get() , font = ("",30) , tag = "kesu")

mform.mainloop()
