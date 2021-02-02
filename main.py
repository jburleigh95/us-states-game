import turtle
import pandas

screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv('50_states.csv')
states_list = data.state.to_list()
guessed_states = []

all_states_guessed = False
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f'{len(guessed_states)}/50 States Guessed', prompt="What's another state?").title()
    if answer_state == "Exit":
        missed_states = [state for state in states_list if state not in guessed_states]
        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv('states_to_learn.csv')
        break

    if answer_state in states_list:
        guessed_states.append(answer_state)
        state_data = data[data.state == answer_state]
        state_name = turtle.Turtle()
        state_name.hideturtle()
        state_name.penup()
        state_name.goto(int(state_data.x), int(state_data.y))
        state_name.write(answer_state)
