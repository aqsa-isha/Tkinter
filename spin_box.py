import tkinter as tk

window = tk.Tk()

window.title("Spin Box Example")

spin = tk.Spinbox(window, from_=0, to=100, width=5)
spin.pack()  # Add the Spinbox widget to the window
# pack method is responsible for positioning the widget.
window.mainloop()
