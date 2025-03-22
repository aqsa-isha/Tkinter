import tkinter as tk

window = tk.Tk()
window.title("Organize Layout")

# Create frames
top_frame = tk.Frame(window)
top_frame.pack()

bottom_frame = tk.Frame(window)
bottom_frame.pack(side="bottom")

# Create buttons in top_frame and bottom_frame
btn1 = tk.Button(top_frame, text="Button1", fg="red")
btn1.pack()

btn2 = tk.Button(top_frame, text="Button2", fg="green")
btn2.pack()

btn3 = tk.Button(bottom_frame, text="Button3", fg="purple")
btn3.pack(side="left")

btn4 = tk.Button(bottom_frame, text="Button4", fg="orange")
btn4.pack(side="left")

window.mainloop()
