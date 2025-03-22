# Label: You can set the label so you can make it bigger or maybe bold.
# We can set the default window size using geometry function
# pp i
import tkinter

window = tkinter.Tk()
# to rename the title of window
window.title("Label")

# Create the label with the desired font style and size
l1 = tkinter.Label(window, text="Aptech!", font=("Arial Bold", 50))

# Place the label in the window using grid layout
l1.grid(column=0, row=0)

# Start the main loop of the window
window.mainloop()
