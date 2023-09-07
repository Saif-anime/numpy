import tkinter as tk
from tkinter import PhotoImage

# Create the main Tkinter window
root = tk.Tk()
root.title("Window with Icons")

# Load the icon images
icon1 = PhotoImage(file="banner_1.jpg")
# icon2 = PhotoImage(file="icon2.png")

# Create labels to display the icons
label1 = tk.Label(root, image=icon1)
# label2 = tk.Label(root, image=icon2)

# Place the labels in the window
label1.pack()
# label2.pack()

# Start the Tkinter main loop
root.mainloop()
