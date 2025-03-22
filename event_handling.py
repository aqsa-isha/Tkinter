# Events: mousemove, mouseover, clciking and scrolling are som events.

# button1 -> left click,   button2 -> middle click, button3 -> right click
import tkinter as tk

window = tk.Tk()
window.title("Event Handling")

# Creating a function with an arguments 'events'
def say_hi(event):
    tk.Label(window, text="Hi").pack()
    
btn = tk.Button(window, text="Click Me!")
btn.bind("<Button-1>", say_hi) # bind takes two parameters, 1st is 'event', 2nd is 'function'

btn.pack()


window.mainloop()