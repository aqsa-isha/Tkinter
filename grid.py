# Grid is another way to organixe the widgets. It uses the matrix row column concepts.
import tkinter as tk

window = tk.Tk()
window.title("Grid")
tk.Label(window, text="Username").grid(row=0) # this is placed in 0 0

# Entry is used to display the input field.
tk.Entry(window).grid(row= 0, column=1) # this is placed in 0 1
tk.Label(window, text="password").grid(row=1) # this is placed in 1 0

tk.Entry(window).grid(row= 1, column=1) # this is placed in 1 1

tk.Checkbutton(window, text="Keep me Logged In").grid(columnspan=2) # columnspan tells to take the width of 2 columns
window.mainloop()