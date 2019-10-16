import subprocess
import os
path = r'C:\Users\harika.gaggara\Documents\PycharmProjects\automation\automation.bat'

from tkinter import *
import tkinter as ttk


root = Tk()
# root.title("Subjects")
# item_1 = IntVar()
# a = item_1.get()
#
# # Add a grid
# mainframe = Frame(root)
# mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
# mainframe.columnconfigure(0, weight=1)
# mainframe.rowconfigure(0, weight=1)
# mainframe.pack(pady=100, padx=100)
#
#
# # Create a Tkinter variable
# tkvar = StringVar(root)
#
# # Dictionary with options
# subjects = {'Paul', 'Arevik', 'Reza', 'Munir', 'Diogo'}
#
# cases = {'nothing', 'laptop', 'pliers', 'phone', 'wallet', 'colt', 'magnum', 'knife', 'blade', 'bomb-belt'}
#
# tkvar.set('Subjects')  # set the default option
#
# tkvar.set('Cases')
# popupMenu = OptionMenu(mainframe, tkvar, *cases)
# Label(mainframe, text="Choose a test case").grid(row=1, column=1)
# popupMenu.grid(row=2, column=1)
#

#
# # on change dropdown value
# def change_dropdown(*args):
#     print('Subject changed to {}'.format(tkvar.get()))
#
# def print_item_values():
#     global a
#     print (a)
#
#
# def ok():
#     print("selected subject is:" + tkvar.get())
# # link function to change dropdown
# tkvar.trace('w', change_dropdown)
#
# #item 1 spinbox
# item_1 = Spinbox(root, from_= 0, to = 10, width = 10)        #.grid(row = 1, column = 1)
#
# #print values
# value_button = Button(root, text = 'Print values', width = 10, command = print_item_values)
# # value_button.grid(row = 0, column = 1)
#
# button = Button(root, text = "Next", command=ok)
# button.pack()
#
# root.mainloop()
#
# # import subprocess
# # import tkinter as tk
# #
# # root = tk.Tk()
# #
# # canvas1 = tk.Canvas(root, width = 350, height = 250)
# #
# # def start_batch():
# #     subprocess.call([path])
# # button1 = tk.Button(root, text = 'select the subject', command = start_batch)
# # canvas1.pack()
# # canvas1.create_window(170,130, window=button1)
# # root.mainloop()


#initalise values from user (spinbox values)
item_1 = IntVar()
a = item_1.get()

def print_item_values():
    global a
    print (a)

#item 1 spinbox
item_1 = Spinbox(root, from_= 0, to = 10, width = 5)
item_1.grid(row = 0, column = 0)

#print values
value_button = Button(root, text = 'Print values', width = 10, command = print_item_values)
value_button.grid(row = 0, column = 1)

root.mainloop()
