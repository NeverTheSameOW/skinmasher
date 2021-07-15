from os import path
import tkinter as tk
from OsFunctions import *

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, text="Select Osu Directory", fg="red",command=foldercheck())
button.pack(side=tk.LEFT)

path = tk.Label(frame, text=str(foldercheck()))
path.pack(side=tk.LEFT)

print(skinlist())













root.mainloop()