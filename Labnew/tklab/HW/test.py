from tkinter import *
root=Tk()
root.geometry("500x500")
root.title("Login")

l1=Label(root,text="Username",width=10,font=("arial",12))
l1.place(x=20,y=120)
e1=Entry(root)
e1.place(x=200,y=120)

l3=Label(root,text="Password",width=10,font=("arial",12))
l3.place(x=19,y=160)
e3=Entry(root)
e3.place(x=200,y=160)

l4=Label(root,text="Email",width=13,font=("arial",12))
l4.place(x=19,y=200)
e4=Entry(root)
e4.place(x=200,y=200)

l5=Label(root,text="Age",width=13,font=("arial",12))
l5.place(x=5,y=240)
e5=Entry(root,show='*')
e5.place(x=200,y=240)

l6=Label(root,text="Contact",width=15,font=("arial",12))
l6.place(x=21,y=280)
e6=Entry(root, show='*')
e6.place(x=200,y=280)

Button(root,text="Login",width=10,bg='blue',fg='white').place(x=200,y=400)
root.mainloop()