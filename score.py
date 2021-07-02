from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 14, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.ht()
        self.goto(0, 280)
        self.current_score = 0
        self.show_score()

    def show_score(self):
        self.write(f"Score: {self.current_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.clear()
        self.current_score += 1
        self.show_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over.", align=ALIGNMENT, font=FONT)

