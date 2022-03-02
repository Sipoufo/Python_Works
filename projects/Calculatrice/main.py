from tkinter import *
from button import Cal_Button

window = Tk()
window.config(pady=30, padx=30)
buttons = []
special_button = ["AC", "+/-", "%", "/", "X", "-", "+", ".", "="]
default_number_first = None
default_number_second = None
prev_operation = None


def writeToEntry(val):
    global default_number_first, prev_operation
    if val in special_button and default_number_first is None:
        entry.delete(0)
        entry.insert(END, "0")
    elif val not in special_button:
        entry.delete(0)
        if default_number_first is not None:
            if prev_operation == "=":
                default_number_first = ""
            default_number_first = f"{default_number_first}{val}"
            print(f"after : {default_number_first}")
        else:
            default_number_first = val
        default_number_first = int(default_number_first)
        entry.delete(0, len(str(default_number_first)))
        entry.insert(END, default_number_first)
    elif val in special_button and default_number_first is not None:
        print(val)
        print(prev_operation)
        if val == "=":
            result()
        elif val == "AC":
            reset()
        elif val in special_button[1:-2] or prev_operation != "=":
            if prev_operation is not None:
                val, prev_operation = prev_operation, val
            else:
                prev_operation = val
            operation(val)

# Operation
def operation(val):
    global default_number_first, default_number_second
    print(f"before : {default_number_second}")
    # Addition
    if val == "+":
        if default_number_second is None:
            default_number_second = default_number_first + 0
        else:
            default_number_second += default_number_first
    # Soustraction
    elif val == "-":
        if default_number_second is None:
            default_number_second = default_number_first - 0
        else:
            default_number_second -= default_number_first
    # Division
    elif val == "X":
        if default_number_second is None:
            default_number_second = default_number_first * 1
        else:
            default_number_second *= default_number_first
    # Multiplication
    elif val == "/":
        if default_number_second is None:
            default_number_second = default_number_first / 1
        else:
            default_number_second /= default_number_first

    print(f"after : {default_number_second}")
    entry.delete(0, len(str(default_number_second)))
    entry.insert(END, default_number_second)
    default_number_first = None

def reset():
    global default_number_first, default_number_second, prev_operation
    print("sqdsq = ")
    entry.delete(0, len(str(default_number_first)))
    entry.insert(END, "0")
    default_number_first = None
    default_number_second = None
    prev_operation = None

def result():
    global default_number_first, default_number_second
    # Addition
    print(f"prev_operation {prev_operation}")
    if prev_operation == "+":
        if default_number_second is None:
            default_number_second = default_number_first + 0
        else:
            default_number_second += default_number_first
    # Soustraction
    elif prev_operation == "-":
        if default_number_second is None:
            default_number_second = default_number_first - 0
        else:
            default_number_second -= default_number_first
    # Division
    elif prev_operation == "X":
        if default_number_second is None:
            default_number_second = default_number_first * 1
        else:
            default_number_second *= default_number_first
    # Multiplication
    elif prev_operation == "/":
        if default_number_second is None:
            default_number_second = default_number_first / 1
        else:
            default_number_second /= default_number_first
    entry.delete(0, len(str(default_number_second)))
    entry.insert(END, default_number_second)
    default_number_first = None
    print('end')


i = 1
s = 0
for button_y in range(1, 6):
    for button_x in range(1, 5):
        if button_y == 1:
            buttons.append(Cal_Button(function=writeToEntry, val=special_button[s], column=button_x, row=button_y))
            s += 1
        else:
            if button_x % 4 == 0:
                buttons.append(Cal_Button(function=writeToEntry, val=special_button[s], column=button_x, row=button_y))
                s += 1
            elif button_x == 3 and button_y == 5:
                buttons.append(Cal_Button(function=writeToEntry, val=special_button[s], column=button_x, row=button_y))
                s += 1
            elif button_y == 5 and button_x == 1:
                buttons.append(
                    Cal_Button(function=writeToEntry, val=0, column=button_x, row=button_y, columnspan=2, size=11))
            elif button_y == 5 and button_x == 2:
                pass
            else:
                buttons.append(Cal_Button(function=writeToEntry, val=i, column=button_x, row=button_y))
                i += 1

# Entry
entry = Entry(width=30, textvariable="val")
entry.grid(column=1, row=0, columnspan=5, pady=5)
Cal_Button.funct(funct=writeToEntry)
entry.insert(END, "0")

window.mainloop()
