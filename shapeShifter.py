from tkinter import *

def turnRed():
    root.config(bg='red')
def turnBlue():
    root.config(bg='blue')
def turnYellow():
    root.config(bg='yellow')
def turnGreen():
    root.config(bg='green')

root = Tk()

root.title('Colour Fidget Toy')
root.geometry('310x300')
root.resizable(False,False)

red = Button(root,text='now you see me red',command=turnRed).pack(expand=True)
blue = Button(root,text='you can have me blue',command=turnBlue).pack(expand=True)
yellow = Button(root,text='percieve me yellow',command=turnYellow).pack(expand=True)
green = Button(root,text='watch me go green',command=turnGreen).pack(expand=True)

root.mainloop()
