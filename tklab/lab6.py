from tkinter import *
root=Tk()

myButton1 = Button(root,text="Click Me")
myButton1.pack()

myButton2 = Button(root,text="I am disabled", state=DISABLED)
myButton2.pack()

myButton3 = Button(root,text="New Button", padx=50)
myButton3.pack()

myButton4 = Button(root,text="Click me", padx=50, pady=50)
myButton4.pack()

root.mainloop()
