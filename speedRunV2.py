from tkinter import * 

def obvMes():
    print('the testing has been tested! :D')

#dimension limits
def dimLim():
    print(f"Screen resolution: {screen_width}x{screen_height}")

root = Tk() 

root.title('Learning')
root.geometry('600x600+300+150') 
root.resizable(True,True) 

'''
pack(side,fill,expand,anchor,padx,pady,ipadx,ipady)
side: where to pack against parent widget
fill: in which dimensions to expand in available space (both->big button/none->small button)
expand: expands to extra space (push or be pushed)
anchor: 1 of the 8 cardinal directions and centre
padx/pady: external padding
ipadx/ipady: internal padding
default values?
'''

btnVar = Button(root,text="testing",command=obvMes).pack(expand=True, fill="none")

labelVar = Label(root,text='i have been labelled').pack(expand=True, fill="none")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

#additional information
addInfo = Button(root,text="wanna know max sizes?",command=dimLim).pack(expand=True, fill="none")

root.mainloop() 
