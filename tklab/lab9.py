from tkinter import *
root=Tk()

e1=Entry(root, width=50,fg="blue", bg="white", borderwidth=5)
e1.pack()

def myClick():
    textoutput = "HEY" + e1.get()
    myLabel = Label(root,text=textoutput)
    myLabel.pack()

btn_new = Button(root, text="Click me", command=myClick)
btn_new.pack()
root.mainloop()