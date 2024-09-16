import random
import turtle as t
color_list = [(236, 225, 206), (207, 157, 106), (214, 216, 227), (235, 213, 224), (142, 146, 160), (180, 71, 30), (227, 211, 116), (95, 105, 137), (189, 157, 28), (201, 149, 175), (221, 233, 224), (10, 18, 61), (98, 115, 174), (185, 18, 4), (15, 32, 15), (225, 169, 196), (28, 30, 11), (211, 86, 60), (236, 173, 160), (152, 165, 154), (123, 89, 100), (32, 48, 115), (234, 208, 6), (91, 104, 93), (180, 184, 217), (191, 91, 113), (183, 13, 20), (35, 18, 31), (78, 78, 35), (51, 73, 50)]#got using the previous file code
t.Screen().colormode(255)
tom= t.Turtle()
tom.speed("fastest")
tom.penup()
tom.hideturtle()
tom.setheading(225)
tom.forward(300)
tom.setheading(0)
no_of_dots = 100

for i in range(1, no_of_dots+1):
    tom.dot(20,random.choice(color_list))
    tom.forward(50)

    if i % 10 == 0:
        tom.setheading(90)
        tom.forward(50)
        tom.setheading(180)
        tom.forward(500)
        tom.setheading(0)

t.Screen().exitonclick()
