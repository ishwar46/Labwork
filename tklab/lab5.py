from tkinter import *
root = Tk()

myLable1 = Label(root, text="Hello Tkinter")
myLable2 = Label(root, text="Hi, I am Ishwar")
myLabel3 = Label(root, text= "I am a Mobile Application Developer")

myLable1.grid(row=0,column=1)
myLable2.grid(row=1,column=4)
myLabel3.grid(row=2,column=1)

root.mainloop()