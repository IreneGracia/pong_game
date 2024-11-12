from turtle import *
from Paddles import *
from Ball import *
from Scoreboard import *

#Create screen
screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')
screen.tracer(0)


#Create paddles
left_paddle = Paddle((-350, 0), 'red')
right_paddle = Paddle((350, 0), 'blue')


#Make paddle move up and down by 20 pixels at a time
screen.listen()

screen.onkeypress(right_paddle.paddle_move_upwards, 'Up')
screen.onkeypress(right_paddle.paddle_move_downwards, 'Down')

screen.onkeypress(left_paddle.paddle_move_upwards, 'w')
screen.onkeypress(left_paddle.paddle_move_downwards, 's')


#Make the ball
ball = Ball()


#Create a scoreboard for left and right players
scoreboard = Scoreboard()


# While loop to allow the constant refreshes needed in the game (e.g.
# ball moving, scoreboard updates, etc.)
game_ongoing = True

while game_ongoing:
    screen.update()

    ball.move()


    #Bounce against top and bottom
    if ball.ycor() >= 300 or ball.ycor() <= -300:
        ball.bounce_top_bottom()


    #Bounce against left and right paddles
    if ball.distance(right_paddle) < 60 and ball.xcor() > 330 or ball.distance(left_paddle) < 60 and ball.xcor() < -330:
        ball.bounce_off_paddle()


    #Change scores when left and right paddles miss the ball, respectively
    if ball.xcor() < -400:
        scoreboard.right_player_point_score()
        ball.reset_position()
        ball.reset_ball_speed()

    elif ball.xcor() > 400:
        scoreboard.left_player_point_score()
        ball.reset_position()
        ball.reset_ball_speed()


screen.exitonclick()
