from tkinter import *
root=Tk()

def myClick():
    myLabel = Label(root,text="Yeah!!!!! TOUCH ME!")
    myLabel.pack()

myButton1 = Button(root,text="Touch Me", command=myClick, fg="white", bg="green")
myButton1.pack()

root.mainloop()