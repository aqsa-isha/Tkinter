import tkinter as tk
from PIL import Image, ImageTk  # Import Pillow library for image handling

window = tk.Tk()
window.title("Images")

# Open the image using Pillow
image_path = r"E:\PRACTICAL\Tkinter\travel.jpg"  # Use raw string to avoid escape character issues
img = Image.open(image_path)

# Convert the image to a Tkinter-compatible format
icon = ImageTk.PhotoImage(img)

# Create a label to display the image
label = tk.Label(window, image=icon)
label.pack()

# Start the Tkinter event loop
window.mainloop()
