from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position, color):
        super().__init__()
        self.shape('square')
        self.color(color)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def paddle_move_upwards(self):
        new_y = self.ycor() + 50
        self.goto(self.xcor(), new_y)

    def paddle_move_downwards(self):
        new_y = self.ycor() - 50
        self.goto(self.xcor(), new_y)
