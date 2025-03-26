from turtle import Screen
from breakout.paddle import Paddle
from breakout.ball import Ball
from breakout.brick import BrickManager
from breakout.scoreboard import Scoreboard
from breakout.constants import SCREEN_WIDTH, SCREEN_HEIGHT, INITIAL_PAUSE
import time
import logging
import os

# Setup logging
file_path = os.path.join(os.path.dirname(__file__), 'breakout.log')
logging.basicConfig(filename=file_path,
                    level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S")
#

# Setup screen
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Breakout Game")
screen.tracer(0)

# Create objects
scoreboard = Scoreboard()
paddle = Paddle()
ball = Ball()
bricks = BrickManager()


def initialize_game():
    """
    Resets the paddle and ball positions and adjusts the ball speed
    based on the current level.
    """
    paddle.reset_position()
    ball.reset_position()
    # increase ball speed every level
    for speed in range(1, scoreboard.level):
        ball.increase_speed()


def handle_wall_collisions():
    """
    Checks if the ball hits the side or top wall and bounces it accordingly.
    """
    if ball.hits_side_wall():
        ball.bounce_x()
    if ball.hits_top_wall():
        ball.bounce_y()


def handle_paddle_collision():
    """
    Checks if the ball hits the paddle and bounces it accordingly.
    increases the ball speed every 5th touch.
    """
    global touch
    if ball.hits_paddle(paddle):
        if touch % 5 == 0:
            ball.increase_speed()
        touch += 1
        ball.bounce_y()


def handle_brick_collisions():
    """
    Checks if the ball hits a brick and if it has
    Removes the brick, increases the score and updates the scoreboard.
    """
    for brick in bricks.brick_list:
        if ball.hits_brick(brick):
            brick_color = brick.color()[0]
            scoreboard.increase_score(brick_color)
            bricks.remove_brick(brick)
            ball.bounce_y()
            scoreboard.update_scoreboard()


def check_win_condition():
    """
    Checks if all bricks have been removed
    If they have, then current Level is completed.
    A new wall is built and the game moves to the next Level.
    """
    if len(bricks.brick_list) == 0:
        bricks.create_bricks()
        scoreboard.next_level()
        initialize_game()


def check_game_over():
    """
    If the ball misses the paddle, the player loses a life.
    If the player has no lives left, the game is over.
    """
    global game_on, touch
    if ball.misses_paddle():
        scoreboard.lose_life()
        if scoreboard.lives == 0:
            game_on = False
        else:
            touch = 1
            initialize_game()


def pause_game():
    """
    Pauses the game and the paddle movement.
    """
    global pause
    print(f"pause {pause} Game pause - press space to continue")
    pause = not pause
    paddle.pause = not paddle.pause


# Key bindings
screen.listen()
screen.onkey(paddle.move_left, "Left")
screen.onkey(paddle.move_right, "Right")
screen.onkey(pause_game, "space")


# Main game loop
game_on = True
pause = INITIAL_PAUSE
touch = 1

logging.info("Game started")
logging.info(f"Score: {scoreboard.score}, Lives: {scoreboard.lives}")

while game_on:
    screen.update()
    while game_on and not pause:
        time.sleep(ball.speed)
        screen.update()
        ball.move()
        handle_wall_collisions()
        handle_paddle_collision()
        handle_brick_collisions()
        check_win_condition()
        check_game_over()

# Game over
scoreboard.game_over()
screen.exitonclick()
