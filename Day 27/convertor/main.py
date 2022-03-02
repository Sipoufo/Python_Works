from tkinter import *

numbers = [str(number) for number in range(0, 10)]

def convert():
    do = True
    for val in entry1.get():
        if val not in numbers:
            do = False
    if do:
        result = int(entry1.get()) * 1.6
        print(result)
        entry2.insert(0, string=result)


window = Tk()
window.title("Km convertor")
window.config(padx=20, pady=20)

# Label
label1 = Label(text="Mile", font=("Bodoni MT", 12))
label1.grid(column=2, row=0)

label2 = Label(text="is equal to", font=("Bodoni MT", 12))
label2.grid(column=0, row=1)

label3 = Label(text="KM", font=("Bodoni MT", 12))
label3.grid(column=2, row=1)


# Entry
entry1 = Entry()
entry1.grid(column=1, row=0)

entry2 = Entry()
entry2.grid(column=1, row=1)


# Button
button = Button(text="Calculate", command=convert)
button.grid(column=1, row=2)

window.mainloop()