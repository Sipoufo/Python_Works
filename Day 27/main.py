from tkinter import *


def add(*args):
    somme = 0
    for n in args:
        somme += n
    return somme


window = Tk()
window.title('First tkinter')
window.minsize(width=500, height=300)

# Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)

def Button_click():
    my_label['text'] = my_entry.get()


# Button
my_button = Button(text="Button", command=Button_click)
my_button.grid(column=1, row=1)

my_button2 = Button(text="New Button", command=Button_click)
my_button2.grid(column=2, row=0)


# Entry
my_entry = Entry()
my_entry.grid(column=3, row=2)


window.mainloop()
