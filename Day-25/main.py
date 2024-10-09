import turtle
import pandas
import csv
screen = turtle.Screen()
screen.title("U.S. States Game")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

data = pandas.read_csv("50_states.csv")
states = data['state'].to_list()

guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 the State", prompt="What's another state's name?")
    answer_state_title = answer_state.title()

    if answer_state_title == "Exit":
        df = pandas.DataFrame({
            "Missed States": states
        })
        df.to_csv("states_to_learn.csv")
        data = pandas.read_csv("states_to_learn.csv")
        print(data)
        break
    if answer_state_title in states:
        guessed_states.append(answer_state_title)
        states.remove(answer_state_title)
        print("correct")
        t = turtle.Turtle()
        t.hideturtle()
        t.color("green")
        t.penup()
        state = data[data.state == answer_state_title]
        x = state.x.item()
        y = state.y.item()
        t.goto(x, y)
        t.write(state.state.item())

