from turtle import Turtle
from breakout.constants import SCREEN_WIDTH, SCREEN_HEIGHT, INITIAL_PAUSE


class Paddle(Turtle):
    """
    A class to represents the paddle in the breakout game.
    """
    def __init__(self):
        """
        Initializes the paddle object.
        """
        super().__init__()
        self.shape("square")
        self.color("dim gray")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.speed("fastest")
        self.penup()
        self.pause = INITIAL_PAUSE
        self.goto(0, ((SCREEN_HEIGHT / 10) - (SCREEN_HEIGHT / 2)))

    def move_left(self):
        """
        If the game is not paused,
        And the paddle is not at the left edge of the screen,
        Moves the paddle to the left.
        """
        if self.pause:
            return
        x = self.xcor() - 20
        if x > 50 - SCREEN_WIDTH / 2:
            self.goto(x, self.ycor())

    def move_right(self):
        """
        If the game is not paused,
        And the paddle is not at the right edge of the screen,
        Moves the paddle to the right.
        """
        if self.pause:
            return
        x = self.xcor() + 20
        if x < SCREEN_WIDTH / 2 - 50:
            self.goto(x, self.ycor())

    def reset_position(self):
        """
        Resets the paddle position to the center of the screen.
        """
        self.goto(0, ((SCREEN_HEIGHT / 10) - (SCREEN_HEIGHT / 2)))
