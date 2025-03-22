import tkinter as tk

window = tk.Tk()
window.title("Image as icons")


icon = tk.PhotoImage(file=r"E:\PRACTICAL\Tkinter\travel.jpg")

label = tk.Label(window, image=icon)
label.pack()

window.mainloop()