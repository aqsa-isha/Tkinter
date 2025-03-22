import tkinter as tk

window = tk.Tk()
window.title("Event Handling")

# Creating a frame to hold the labels
frame = tk.Frame(window)
frame.pack()

# Function for left-click event
def left_click(event):
    # Remove previous labels before showing the new one
    for widget in frame.winfo_children():
        widget.destroy()
    tk.Label(frame, text="Left Click!").pack()

# Function for middle-click event
def middle_click(event):
    # Remove previous labels before showing the new one
    for widget in frame.winfo_children():
        widget.destroy()
    tk.Label(frame, text="Middle Click!").pack()

# Function for right-click event
def right_click(event):
    # Remove previous labels before showing the new one
    for widget in frame.winfo_children():
        widget.destroy()
    tk.Label(frame, text="Right Click!").pack()

# Bind mouse buttons to the event handlers using ButtonPress (works across platforms)
window.bind("<ButtonPress-1>", left_click)   # Left mouse click
window.bind("<ButtonPress-2>", middle_click) # Middle mouse click (scroll wheel)
window.bind("<ButtonPress-3>", right_click)  # Right mouse click

window.mainloop()
