import tkinter as tk

mform = tk.Tk()
canvas  = tk.Canvas(mform, width = 300, height = 300)
canvas.pack()

im = tk.PhotoImage(file = "d02.gif")
canvas.create_image(150, 150, image = im)
mform.mainloop()
