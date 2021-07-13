import tkinter as tk
    

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, text="Select Osu Skin Directory", fg="red",command=quit)
button.pack(side=tk.LEFT)


root.mainloop()