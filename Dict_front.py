from tkinter import *

window=Tk()

l1=Label(window,text="Enter a word:")
l1.grid(row=0,column=1)

word=StringVar()
e1=Entry(window,textvariable=word)
e1.grid(row=0,column=3)

b1=Button(window,text="Search")
b1.grid(row=1, column=3)

window.mainloop()