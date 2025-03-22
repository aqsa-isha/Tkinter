import tkinter as tk

window = tk.Tk()
window.title("Layout Fill Example")
# Sufficient Width
tk.Label(window, text="Sufficient width", fg="white", bg="purple").pack()
# width of x
tk.Label(window, text="taking all available x widths", fg="white", bg="green").pack(fill="x")


# height of y
tk.Label(window, text="taking all available y height", fg="white", bg="black").pack(side="left", fill="y")


window.mainloop()