import tkinter as tk

mform = tk.Tk()
mform.geometry("320x240")

lbl1 = tk.Label(text = "LABEL1")
btn1 = tk.Button(text = "BUTTON1")

lbl1.pack()
btn1.pack()
mform.mainloop()
