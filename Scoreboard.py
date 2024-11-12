from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.left_player_score = 0
        self.right_player_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        
        self.goto(-200, 200)
        self.write(self.left_player_score, align='center', font=('Courier', 88, 'normal'))

        self.goto(200, 200)
        self.write(self.right_player_score, align='center', font=('Courier', 88, 'normal'))


    def left_player_point_score(self):
        self.left_player_score += 1
        self.update_scoreboard()

    def right_player_point_score(self):
        self.right_player_score += 1
        self.update_scoreboard()
