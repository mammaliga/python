from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.show_high_score()
        self.speed("fastest")
        self.color("white")
        self.penup()
        self.hideturtle()
        self._keep_score()

    def show_high_score(self):
        with open("data.txt") as data:
            high_score = data.read()
        return int(high_score)

    def _keep_score(self):
        self.clear()
        self.goto(0, 280)
        self.write(
            f"Score: {self.score}   High Score: {self.high_score}",
            align="center",
            font=(
                "Arial",
                14,
                "normal"))

    def increase_score(self):
        self.score += 1
        self._keep_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score

        self.score = 0
        with open("data.txt", "w") as data:
            data.write(f"{self.high_score}")
        self._keep_score()

    # def end_game(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align="center", font=("Arial", 24, "normal"))
