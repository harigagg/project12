from tkinter import *
import tkinter as ttk

#create Tk window
root = Tk()

#set name of window
root.title('Testing Values')

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