import tkinter as tk 

window = tk.Tk()
window.title("Binding Function")

# Define the function that will be called when the button is clicked
def say_hi():
    tk.Label(window, text="Hi").pack()

# Create the button, and when clicked, it will call say_hi function
tk.Button(window, text="Click me!", command=say_hi).pack()

window.mainloop()
