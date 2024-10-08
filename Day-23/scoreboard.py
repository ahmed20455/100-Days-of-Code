FONT = ("Courier", 24, "normal")
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-220, 250)
        self.write("Level=" + str(self.level), align="center", font=FONT)

    def level_increment(self):
        self.level += 1
        self.update_scoreboard()

    def reset_game(self):
        self.goto(0,0)
        self.write(f"GAME OVER : YOU LOST ❗❗", align="center", font=FONT)

