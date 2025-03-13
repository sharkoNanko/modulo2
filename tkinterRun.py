#imports all the modules in the library
from tkinter import * 

#NOTES:
#cd Desktop\MyPythonScripts (Windows)
#python(3) my_script.py

def obvMes():
    #this will print in the terminal
    print('the testing has been tested! :D')

#dimension limits
def dimLim():
    #this will print in the terminal
    print(f"Screen resolution: {screen_width}x{screen_height}")

#root is the name we chose for the master of the app
root = Tk() 

#the following are slave functions annexed to master variable
root.title('Learning')

#window dimensions and TL corner coordinates
root.geometry('600x600+300+150') 

#constraints on window dimensions
#wm_resizable() is the old version
#width= ,height=
root.resizable(True,True) 

#1variable;2masterFunction;3slaveFunction <- if all modules haven't been imported
btnVar = Button(root,text="testing",command=obvMes) 
#Tk.Button() isn't needed because all modules were...
#...already imported from tkinter, in this case Tk

#lets us see the button
#btnVar.place(x=250,y=200)
btnVar.pack(expand=True, fill="both")

#create
labelVar = Label(root,text='i have been labelled')
#make visible
#labelVar.place(width=120,height=120,x=400,y=400)
labelVar.pack(expand=True, fill="both")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
addInfo = Button(root,text="wanna know max sizes?",command=dimLim)
#addInfo.place(x=150,y=100)
addInfo.pack(expand=True, fill="both")

#this keeps the app running
root.mainloop() 
