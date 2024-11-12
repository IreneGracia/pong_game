from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.x_movement_speed = 2
        self.y_movement_speed = 2

    def move(self):
        new_x = self.xcor() + self.x_movement_speed
        new_y = self.ycor() + self.y_movement_speed
        self.goto(new_x, new_y)

    def bounce_top_bottom(self):
        self.y_movement_speed *= -1

    def bounce_off_paddle(self):
        self.x_movement_speed *= -1
        self.x_movement_speed *= 1.25

    def reset_ball_speed(self):
        self.x_movement_speed = 2

    def reset_position(self):
        self.goto(0,0)
        self.bounce_off_paddle()
