from turtle import Turtle
from breakout.constants import SCREEN_WIDTH, SCREEN_HEIGHT, START_SPEED


class Ball(Turtle):
    """
    A class to represent the ball in the Breakout game.
    """
    def __init__(self):
        """
        Initializes the ball object.
        """
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("white")
        self.penup()
        self.x = 0
        self.y = 100 - (SCREEN_HEIGHT / 2)
        self.goto(self.x, self.y)
        self.dx = 10
        self.dy = 10
        self.speed = START_SPEED

    def move(self):
        """
        Moves the ball based on the x_move and y_move attributes.
        """
        self.x = self.xcor() + self.dx
        self.y = self.ycor() + self.dy
        self.goto(self.x, self.y)

    def bounce_x(self):
        """
        Bounces the ball in the x-axis.
        """
        self.dx *= -1

    def bounce_y(self):
        """
        Bounces the ball in the y-axis.
        """
        self.dy *= -1

    def reset_position(self):
        """
        Resets the ball position to the center of the screen.
        Sets ball speed to the initial speed.
        """
        self.x = 0
        self.y = 100 - (SCREEN_HEIGHT / 2)
        self.goto(self.x, self.y)
        self.dx = 10
        self.dy = 10
        self.speed = START_SPEED

    def increase_speed(self):
        """
        Increases the ball speed by 10%, by reducing the speed attribute.
        speed attribute is the time delay between ball movements.
        """
        self.speed *= 0.9

    def hits_side_wall(self):
        """
        Checks if the ball hits the side walls.
        Returns True if the ball hits the left or right wall.
        """
        # bounce off the left wall
        left_wall = -(SCREEN_WIDTH/2 - 20)
        right_wall = (SCREEN_WIDTH/2 - 20)
        if ((self.x < left_wall) or self.x > right_wall):
            return True
        return False

    def hits_top_wall(self):
        """
        Checks if the ball hits the top wall.
        Returns True if the ball hits the top wall.
        """
        # bounce off the top wall
        if self.y > (SCREEN_HEIGHT / 2) - 20:
            return True
        return False

    def hits_paddle(self, paddle):
        """
        Checks if the ball hits the paddle.
        Returns True if the ball hits the paddle.
        """
        paddle_top = (100 - (SCREEN_HEIGHT / 2))
        ball_to_paddle = self.x - paddle.xcor()
        if ((self.y < paddle_top) and (-60 < ball_to_paddle < 60)):
            return True
        return False

    def misses_paddle(self):
        """
        Checks if the ball misses the paddle.
        Returns True if the ball misses the paddle.
        """
        if self.y < ((-350)):
            return True
        return False

    def hits_brick(self, brick):
        """
        Checks if the ball hits a brick.
        Returns True if the ball hits a brick.
        """
        if self.distance(brick) < 20:
            return True
        return False
