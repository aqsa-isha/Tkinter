# Introduction to Tkinter
# framework : Flask and Django

# Installing and working with Tkinter
# Overview of all the concepts in Tkinter
# Looking at code to unserstand history

## Graphical User Interface: GUI is a desktop app which helps you to interact with computers.

# GUI can used to create Text Editors, Games and apps.

# we prefer GUI over Command Line.
# Python Libraries for GUI: Kivy, Qt, wxpython, Tkinter

# Tkinter in Python GUI Programming is standard python GUI library.
# It gives us an object-oriented interface to the Tk GUI Toolkit.

# 1. Import the Tkinter module
# 2. Create the GUI applicatin main window
# 3. Add widgets
# 4. Enter the main event loop

# Basic syntax of Tkinter
import tkinter

window = tkinter.Tk()
# to rename the title of window
window.title("My First GUI")
# pack is used to show the object in the window
label = tkinter.Label(window, text="Hello World!").pack()
window.mainloop()


# A widget is an element of a graphical user interface(GUI) that displays information 
# or provides a specific way for a user to interact with the operating system or an application.


# 1.Label 2.Button 3.Entry 4.ComboBox 5.CheckButton 6.Radio 7.Radio 8.ScrolledText
# 9.SpinBox 10.Menu Bar 11.Notebook


# Label: You can set the label so you can make it bigger or maybold

