# Button is created and added to the window the same as the label
# We can change the foreground for a buttonor any other widget using fg property.
# Also you change the background color for any widget using bg property.
import tkinter

window = tkinter.Tk()
window.title("Button")

# Create a label to update the text when the button is clicked
l1 = tkinter.Label(window, text="Click the button!", font=("Arial", 14))
l1.grid(column=0, row=1)

# Create a button with background and foreground colors
bt = tkinter.Button(window, text="Enter", bg="orange", fg="red", command=lambda: clicked())
bt.grid(column=1, row=0)

# Function to update the label when the button is clicked
def clicked():
    l1.configure(text="Button was clicked!!")

# Start the main loop
window.mainloop()
