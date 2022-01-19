from tkinter import *

root = Tk()
myButton = Button(root, text="Click me")
myButton.pack()

myButton = Button(root, text="Click me", padx=50, state=DISABLED)
myButton.pack()

myButton = Button(root, text="Click me")
myButton.pack()

myButton = Button(root, text="Click me", padx=50,pady=50, state=DISABLED)
myButton.pack()

root,mainloop()