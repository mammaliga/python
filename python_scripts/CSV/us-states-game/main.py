import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")
t = turtle.Turtle()
t.penup()
t.hideturtle()


data = pandas.read_csv("50_states.csv")
states = data.state.to_list()

count = 0
while count <= 50:
    answer_state = screen.textinput(
        title=f"{count}/50 states",
        prompt="What's another state's name?")
    answer = answer_state.title()

    if answer in states:
        _state = data.loc[data.state == answer]
        state = list(_state.state)[0]
        x_cord = list(_state.x)[0]
        y_cord = list(_state.y)[0]
        cords = (x_cord, y_cord)
        t.goto(cords)
        t.write(state, align="center", font=("Verdana", 8, "normal"))
        print(f"{state} {cords}")
        count += 1
    else:
        print(f"no match found for {answer}")

turtle.mainloop()
