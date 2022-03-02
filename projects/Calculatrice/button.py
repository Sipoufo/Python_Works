from tkinter import Button
from functools import partial

class Cal_Button(Button):
    def __init__(self, function, **kwargs):
        super().__init__()
        self.cols = 1
        self.width = 5

        if kwargs.get("columnspan") is not None:
            self.cols = kwargs.get("columnspan")

        if kwargs.get("size") is not None:
            self.width = kwargs.get("size")

        self.__value = kwargs["val"]
        self.config(text=self.__value, width=self.width, command=partial(function, self.__value))
        self.grid(column=kwargs["column"], row=kwargs["row"], columnspan=self.cols)

    def value(self):
        return self.__value

    def funct(funct):
        pass