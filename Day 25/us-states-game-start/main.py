import turtle
from state import State

screen = turtle.Screen()
screen.title("U.S, States Game")
image = "./blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

state = State()

game_on = True
while game_on:
    answer_state = screen.textinput(title="Guess the state", prompt="What's another state's name ? [Press q for quit]")
    state.add_State(answer_state)
    if answer_state == "q":
        game_on = False