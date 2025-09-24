from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align='center', font=('Courier', 18, 'normal'))


    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            # read content of file and save it to a var called score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}" )
        self.score = 0
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over ", align='center', font=('Courier', 18, 'normal'))


    def increase_score(self):
        self.score +=1
        self.update_score()

