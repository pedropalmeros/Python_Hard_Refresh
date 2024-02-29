import turtle
import pandas 

screen = turtle.Screen()
screen.title('U.S. State Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 Guess the State", prompt ="What's anther state's name?")
    answer_state = answer_state.lower()
    answer_state = answer_state.title()

    all_states = data.state.to_list()

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(state_data.state.item())

screen.exitonclick()

  
