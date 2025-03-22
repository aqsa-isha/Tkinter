# We can use entry class to add textbox
import tkinter

window = tkinter.Tk()
window.title("Entry Example")

# Create a label to display the result
l1 = tkinter.Label(window, text="Enter your name:", font=("Arial", 14))
l1.grid(column=0, row=0)

# Create an Entry widget (textbox)
txt = tkinter.Entry(window, width=20)
txt.grid(column=1, row=0)

# Function to update the label when the button is clicked
def clicked():
    res = "Welcome to " + txt.get()
    l1.configure(text=res)

# Create a Button widget that calls the 'clicked' function when pressed
bt = tkinter.Button(window, text="Enter", command=clicked)
bt.grid(column=1, row=1)

# Start the main loop
window.mainloop()
