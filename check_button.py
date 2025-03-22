# to create a checkbutton widget, we can use Checkbutton Widget.

import tkinter

window = tkinter.Tk()
window.title("Checkbox Button")

chk_state = tkinter.BooleanVar()
chk_state.set(True)

chk = tkinter.Checkbutton(window, text="select", var=chk_state)
chk.grid(column=0,row=0)

window.mainloop()
