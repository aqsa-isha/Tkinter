import tkinter
from tkinter import scrolledtext

window = tkinter.Tk()
window.title("Scrolled Text")

# Create the ScrolledText widget with width and height
txt = scrolledtext.ScrolledText(window, text ="Aptech Defence", width=40, height=10)

# Pack the widget to make it visible in the window
txt.pack()

# Start the main loop
window.mainloop()
