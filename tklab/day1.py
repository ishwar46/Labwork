from tkinter import *

root = Tk()

redButton = Button(root, text="Left", fg="green")
redButton.pack(side=LEFT)

greenButton = Button(root, text="Right", fg="green")
greenButton.pack(side=RIGHT)

blueButton = Button(root, text="Top", fg="blue")
blueButton.pack(side=TOP)

blackButton = Button(root, text="Bottom", fg="black")
blackButton.pack(side=BOTTOM)
root.mainloop()