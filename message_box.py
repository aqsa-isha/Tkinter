import tkinter
from tkinter import messagebox
window = tkinter.Tk()
window.title("Message Box")


messagebox.showinfo("Message Title", "Message Content")

# Show a message box whena user clicks it
def clicked():
    messagebox.showinfo('Message Title', 'Message Content')
btn = tkinter.Button(window, text="Enter", command=clicked)


window.mainloop()