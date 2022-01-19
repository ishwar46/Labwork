from tkinter import *
root = Tk()
root.geometry("400x250")

email = Label(root,text="Email").place(x=30,y=50)
e1 = Entry(root).place(x=100,y=50)
password = Label(root,text="Password").place(x=30,y=90)
e2 = Entry(root).place(x=100,y=90)
address = Label(root,text="Address").place(x=30,y=130)
e3 = Entry(root).place(x=100,y=130)
submit = Button(root,text="Submit").place(x=100,y=160)
root.mainloop()