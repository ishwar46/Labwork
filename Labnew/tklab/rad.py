"""from tkinter import*
window=Tk()
def add():
    print(var.get())
var=IntVar()
r1=Radiobutton(window,text="Male",variable=var,value=1,command=add)
r1.pack(anchor=W)
r2=Radiobutton(window,text="Female",variable=var,value=2,command=add)
r2.pack(anchor=W)

window.mainloop()"""

from tkinter import*
window=Tk()
def add():
    if var.get()==1:
        print(var.get())
    else:
        print("Female")
var=IntVar()
r1=Radiobutton(window,text="Male",variable=var,value=1,command=add)
r1.pack(anchor=W)
r2=Radiobutton(window,text="Female",variable=var,value=2,command=add)
r2.pack(anchor=W)

window.mainloop()