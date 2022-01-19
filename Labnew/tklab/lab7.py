from tkinter import *
root=Tk()

def myClick():
    myLabel = Label(root,text="Touched")
    myLabel.pack()

myButton1 = Button(root,text="Touch me", command=myClick)
myButton1.pack()

root.mainloop()