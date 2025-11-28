from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.penup()
        self.goto(-240,270)
        self.color("black")
        self.update_score()

    def update_score(self):
        self.write(f"Level: {self.score}", align='center', font=('Courier', 18, 'normal'))


    def game_over(self):
        self.goto(0,0)
        self.write("Game Over ", align='center', font=('Courier', 18, 'normal'))

    def increase_score(self):
        self.score +=1
        self.clear()
        self.update_score()


