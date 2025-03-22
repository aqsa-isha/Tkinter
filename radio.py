# you can use radio button to select one of the options

import tkinter


window = tkinter.Tk()
window.title("Radio button example")

rad1 = tkinter.Radiobutton(window, text='Python', value=1)
rad2 = tkinter.Radiobutton(window, text='Java', value=2)
rad3 = tkinter.Radiobutton(window, text='Scala', value=3)

rad1.grid(column = 0, row = 0)
rad2.grid(column = 1, row = 0)
rad3.grid(column = 2, row = 0)


window.mainloop()















