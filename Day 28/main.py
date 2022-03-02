import math
from tkinter import *

# Constants
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
break_time = 1
stop = True

def stop():
    global stop
    stop = False

def start_time():
    global stop
    stop = True
    if break_time == 1:
        count_down(1500)
    else:
        count_down(300)


def count_down(count):
    global break_time
    if stop:
        if count > 0:
            canvas.itemconfig(text_time, text=f"{math.floor(count / 60)}:{count % 60}")
            window.after(1000, count_down, count - 1)
        else:
            break_time *= -1
            start_time()
    else:
        canvas.itemconfig(text_time, text=f"00:00")


# UI SETUP
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=GREEN)

title = Label(text="Timer", fg=PINK, bg=GREEN, font=(FONT_NAME, 40, "bold"))
title.grid(column=1, row=0)

canvas = Canvas(width=300, height=312, bg=GREEN, highlightthickness=0)
image_center = PhotoImage(file="image.png")
canvas.create_image(150, 156, image=image_center)
text_time = canvas.create_text(150, 280, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)


# Button
button_start = Button(text="Start",  highlightthickness=0, command=start_time)
button_start.grid(column=0, row=2)

button_reset = Button(text="Reset",  highlightthickness=0, command=stop)
button_reset.grid(column=2, row=2)


# Check mark
mark = Label(text="✔", bg=GREEN, fg=YELLOW, width=50)
mark.grid(column=1, row=3)



window.mainloop()