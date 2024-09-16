import random
import turtle as t
screen=t.Screen()
colors_list = ["red", "green", "yellow", "orange", "blue", "purple"]
y_post=[-70, -40, -10, 20, 50, 80]
turtles_list = []
is_race_on = False
screen.setup(width = 500,height = 400)
user_bet = screen.textinput(title="Make your bet", prompt="Which Turtle will win the race?Enter a color:")
print(user_bet)

for _ in range(0,6):
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors_list[_])
    turtles_list.append(new_turtle)
    new_turtle.goto(x=-230,y=y_post[_])

if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in turtles_list:
        if turtle.xcor() > 230:
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You've won!! The winner is {winning_turtle}!")
            else:
                print(f"You've lost! The winner is {winning_turtle}!")
            exit()
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)
screen.exitonclick()
