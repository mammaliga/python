from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self._l_score = 0
        self._r_score = 0
        self._update_scoreboard()

    def _update_scoreboard(self):
        self.clear()
        self.goto(-100, 190)
        self.write(
            self._l_score,
            align="center",
            font=(
                "Courier",
                80,
                "normal"))
        self.goto(100, 190)
        self.write(
            self._r_score,
            align="center",
            font=(
                "Courier",
                80,
                "normal"))

    def l_point(self):
        self._l_score += 1
        self._update_scoreboard()

    def r_point(self):
        self._r_score += 1
        self._update_scoreboard()
