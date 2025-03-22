# Combobox Widgets are very easy to use and aree widely used as well.

import tkinter
from tkinter.ttk import Combobox

window = tkinter.Tk()
window.title("Combobox Example")

# Create the Combobox widget
combo = Combobox(window)
# Adding the combobox items using tuple
combo['values'] = (1, 2, 3, 4, 5, "Text")
# Setting the selected item
combo.current(3)  # This selects the item at index 3 (which is 4)
combo.grid(column=0, row=0)

# Start the main loop
window.mainloop()
