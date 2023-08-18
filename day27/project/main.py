from tkinter import *

# initializations
window = Tk()
window.title('MILES - KM Converter')
window.minsize(300, 200)
window.config(padx=10, pady=10)

APP_FONT = ('Arial', 14, 'bold')
BUTTON_FONT = ('Arial', 12)

# conversion function
def convert():
    km = float(mile_input.get()) * 1.60934
    km_display['text'] = round(km, 2)

# widgets
mile_input = Entry(width=10, font=APP_FONT, justify='center')
mile_input.insert(END, 0)
mile_label = Label(text='MILES', font=APP_FONT)
acc_lbl = Label(text='is equal to:', font=APP_FONT)
km_display = Label(text=0, font=APP_FONT)
km_label = Label(text='KM', font=APP_FONT)
calc = Button(text='Calculate', font=BUTTON_FONT, command=convert)

# position
mile_input.grid(column=1, row=0)
mile_label.grid(column=2, row=0)
acc_lbl.grid(column=0, row=1)
km_display.grid(column=1, row=1)
km_label.grid(column=2, row=1)
calc.grid(column=1, row=2)

window.mainloop()

