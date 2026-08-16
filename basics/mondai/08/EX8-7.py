import tkinter as tk

def herasu(c):
    global lbl1, mform

    if c >= 0:
        lbl1.configure(text = c)
        mform.after(1000, herasu, c - 1)
    else:
        lbl1.configure(text = "終了")

def hajimari():
    global mform
    lbl1.configure(text = "開始")
    mform.after(1000, herasu, 5)

mform = tk.Tk()
mform.geometry("320x240")
lbl1 = tk.Label(mform , font=("" , "20"))
lbl1.pack()

btn1 = tk.Button(mform, text = "押して！",  font=("" , "20"), command = hajimari)
btn1.pack()

mform.mainloop()
