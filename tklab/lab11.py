#Adding Frame to progeam

from tkinter import *

window = Tk()
frame = LabelFrame(window, text="this is frame", padx=10, pady=10)
frame.pack(padx=50,pady=50)
b=Button(frame, text="Dont click here")
b2=Button(frame, text="............here")
b.grid(row=0, cloumn=0)
b2.grid(row=1, column=1)
window.mainloop()