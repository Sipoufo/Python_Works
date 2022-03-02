import pandas
from turtle import Turtle

class State:
    def __init__(self):
        super().__init__()
        self.allState = []
        self.extract_State()

    def extract_State(self):
        state_file = pandas.read_csv("./50_states.csv")
        name_states = state_file["state"].to_list()
        for name_state in name_states:
            state = state_file[state_file["state"] == name_state]
            x = state["x"].to_list()[0]
            y = state["y"].to_list()[0]
            self.allState.append({
                "state": name_state,
                "x": int(x),
                "y": int(y)
            })

    def add_State(self, state_in):
        for one_state in self.allState:
            if state_in.lower() == one_state["state"].lower():
                print(one_state)
                state = Turtle()
                state.hideturtle()
                state.penup()
                state.goto(one_state["x"], one_state["y"])
                state.write(f"{one_state['state']}", align="center", font=("Courier", 8, "normal"))
