import tkinter as tk

def dsplbl1():
    lbl1.configure(text = "押されたぁ！")

mform = tk.Tk()
mform.geometry("320x240")

lbl1 = tk.Label(text = "")
btn1 = tk.Button(text = "押して！", command = dsplbl1)

lbl1.pack()
btn1.pack()
mform.mainloop()
