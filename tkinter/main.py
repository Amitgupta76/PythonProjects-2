from tkinter import *


def button_clicked():
    my_label3.config(text=f"{round(float(input.get())*1.609344, 1)}")


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=350, height=180)
window.config(padx=30, pady=30)

my_label = Label(text="Miles", font=("Arial", 24))
my_label.grid(column=2, row=0)

input = Entry(width=10)
input.grid(column=1, row=0)

my_label1 = Label(text="is equal to", font=("Arial", 24))
my_label1.grid(column=0, row=1)

my_label2 = Label(text="Km", font=("Arial", 24))
my_label2.grid(column=2, row=1)

my_label3 = Label(text="0", font=("Arial", 24))
my_label3.grid(column=1, row=1)

button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)


window.mainloop()
