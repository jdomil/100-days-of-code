from tkinter import *


def convert():
    miles = float(mile_input.get())
    km = miles * 1.609
    result = round(km, 2)
    result_label.config(text=result)


window = Tk()
window.title("Miles to Km Converter")
window.config(padx=20, pady=20)

# Input
mile_input = Entry(width=10)
mile_input.grid(row=0, column=1)

# "Miles" label
miles_label = Label(text="Miles", font=("Arial", 20), anchor="w")
miles_label.grid(row=0, column=2)

# "is equal to" label
equals_label = Label(text="is equal to", font=("Arial", 20), anchor="e")
equals_label.grid(row=1, column=0)

# Result label
result_label = Label(text="0", font=("Arial", 20), anchor="center")
result_label.grid(row=1, column=1)

# "Km" label
km_label = Label(text="Km", font=("Arial", 20), anchor="w")
km_label.grid(row=1, column=2)

# Calculate button
button = Button(text="Calculate", command=convert, width=5)
button.grid(row=2, column=1)


window.mainloop()
