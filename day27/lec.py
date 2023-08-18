# tkinter, *args, **kwargs, creating GUI programs

# # creating windows and labels with tkinter
# # import tkinter package (built in)
# import tkinter

# # initialize tk GUI
# window = tkinter.Tk()
# # GUI window title
# window.title('Sample TK Window')
# # resizing window
# window.minsize(500, 300)

# # label
# # initialize a label in GUI
# sample_label = tkinter.Label(text='Hello world', font=('Arial', 24, 'bold'))
# # show label in GUI, center default
# sample_label.pack()

# # exit GUI
# window.mainloop()

# ================================================
# setting default values for optional arguments inside a function header
# # advanced python arguments
# # keyword arguments e.g.
# def bar(a, b, c):
#     print(a, b, c)
# bar(a=1, b=2, c=3)
# # default arguments e.g.
# def foo(a=2, b=4, c=6):
#     print(a, b, c)
# foo()

# ================================================
# many-positional arguments using *args
# def nat(a):
#     print(a)
# # nat('stat', 2, 8) # returns error; function only takes 1 argument
# def cod(*args):
#     print(*args)
# cod(1, 1, 1, 1, 1) # returns any number of arguments inside the function

# # challenge
# def add(*args):
#     print(sum(args))
# add(1, 2, 3)

# ================================================
# many keyword arguments using **kwargs
# def foos(n=2,**kwargs):
#     print(n + kwargs.get('add'))
#     print(n * kwargs.get('multiply'))
# foos(add=4, multiply=-2)

# # without using **kwargs
# def bars(add, multiply, n=2):
#     print(n + add)
#     print(n * multiply)
# bars(4, -2)

# class Car:
#     def __init__(self, **kw):
#         self.model = kw.get('model')
#         self.year = kw.get('year')
#         self.color = kw.get('color')
# reb = Car(model='Subaru', year=1995, color='Silver')
# print(reb.model, reb.year, reb.color)

# ================================================
# more tkinter
from tkinter import *

window = Tk()
window.title('Sample TK Window')
window.minsize(500, 300)

# # label
# sample_label = Label(text='hello world', font=('Arial', 24, 'bold'))
# sample_label.pack()
# sample_label['text'] = 'sample text'

# # button
# # adding event listener to button
# def clicked_button():
#     print('click click')
# sample_button = Button(text='bonk', command=clicked_button)
# sample_button.pack()

# # challenge - change label when button is clicked
# label_text = 'hello world'
# sample_label2 = Label(text=label_text, font=('Arial', 24, 'bold'))
# sample_label2.pack()
# def change_sample_label():
#     sample_label2['text'] = 'label changed'
#     sample_label2.pack()
# change_label = Button(text='change label', command=change_sample_label)
# change_label.pack()

# # simple counter app
# main_lbl = Label(text='Simple Counter App', font=('Arial', 24, 'bold'))
# main_lbl.pack()
# counter = 0
# count_lbl = Label(text=counter, font=('Arial', 20, 'bold'))
# count_lbl.pack()

# def inc_count():
#     global counter
#     counter += 1
#     count_lbl['text'] = counter
# def dec_count():
#     global counter
#     counter -= 1
#     count_lbl['text'] = counter

# inc_button = Button(text='+', command=inc_count)
# inc_button.pack()
# dec_button = Button(text='-', command=dec_count)
# dec_button.pack()

# # input
# sign = Label(text='Change Me', font=('Arial', 24, 'bold'))
# sign.pack()
# input = Entry(width=30, font=('Calibri', 16), justify='center')
# input.pack()
# def change_sign():
#     new_sign = input.get()
#     sign['text'] = new_sign
#     input.delete(0, END)
# button = Button(text='Print', command=change_sign)
# button.pack()

# ================================================
# other tkinter widgets
# GO TO: tkinter_widget_demo.py

# ================================================
# tkinter layout manager - pack(), place(), grid()
sign = Label(text='Change Me', font=('Arial', 24, 'bold'))
# sign.pack()
# sign.place(x=100, y=0)
sign.grid(column=0, row=0)

input = Entry(width=30, font=('Calibri', 16), justify='center')
# input.pack()
# input.place()
input.grid(column=1, row=1)

def change_sign():
    new_sign = input.get()
    sign['text'] = new_sign
    input.delete(0, END)
button = Button(text='Print', command=change_sign)
# button.pack()
# button.place()
button.grid(column=3, row=2)

button2 = Button(text='Some button', command=change_sign)
button2.grid(column=2, row=0)

# padding
# _.cofig(padx=_, pady=_)

# exit GUI
window.mainloop()

