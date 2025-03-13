import tkinter as tk

root = tk.Tk()
root.title("Buttons Example")

label1 = tk.Label(root, text="Label 1")
label1.pack(pady=10)

button1 = tk.Button(root, text="Button 1")
button1.pack(pady=10)

label2 = tk.Label(root, text="Label 1")
label2.pack(pady=10)

button2 = tk.Button(root, text="Button 2")
button2.pack(pady=10)

label3 = tk.Label(root, text="Label 1")
label3.pack(pady=10)

button3 = tk.Button(root, text="Button 3")
button3.pack(pady=10)

root.mainloop()
