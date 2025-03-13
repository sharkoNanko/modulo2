import tkinter as tk
from tkinter import *

#window
root = tk.Tk()

root.title('Demo')
root.geometry('400x400')

#title
title_label = tk.Label(master = root, text = 'beleza', font = 'Calibri 24')
title_label.pack()



#run
root.mainloop()
