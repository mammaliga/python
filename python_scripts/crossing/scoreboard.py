from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 0
        self.hideturtle()
        self.goto(-220, 250)
        self.update_score()

    def update_score(self):
        self._increase_level()
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def _increase_level(self):
        self.clear()
        self.level += 1

    def game_over(self):
        self.clear()
        self.home()
        self.write("Game Over", align="center", font=FONT)
