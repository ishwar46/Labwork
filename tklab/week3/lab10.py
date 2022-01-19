from tkinter import *

root = Tk()
root.title("GUI")
root.maxsize(width=600,height=300)
root.minsize(width=600,height=300)
#function
def add():
    x = var.get()
    print(x)
    mylabell.config(text=x,bg="green")
#label1
mylabel = Label(root,text="Username",fg="red",bg="yellow")
mylabel.place(x=10,y=10)

#label2
mylabell = Label(root,text="Nothing",fg="red",bg="yellow")
mylabell.place(x=40,y=120)

#entry
var = StringVar()
ent = Entry(root,bg="black",fg="white",textvariable=var)
ent.place(x=80,y=10)

#button

btn = Button(root, text="Sunmit",bg="green", fg="white", command=add)
btn.place(x=20,y=80)
root.mainloop()