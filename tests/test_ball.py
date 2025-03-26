import pytest
from breakout.ball import Ball
from breakout.constants import SCREEN_HEIGHT

# We will test the Ball class from breakout.ball module
# The Ball class has the following methods:
# 1. __init__(self)
# 2. move(self)
# 3. bounce_x(self)
# 4. bounce_y(self)
# 5. reset_position(self)
# 6. increase_speed(self)


@pytest.fixture
def ball():
    """
    Fixture to create a Ball instance for testing.
    """
    return Ball()


def test_init(ball):
    """
    Test that the Ball instance is initialized
    with the correct attributes.
    """
    assert ball.x == 0
    assert ball.y == 100 - (SCREEN_HEIGHT / 2)
    assert ball.dx == 10
    assert ball.dy == 10
    assert ball.speed == 0.08
    "Ball should be initialized with x, y, dx, dy, and speed attributes."


def test_move(ball):
    """
    Test that the ball moves based on the dx and dy attributes.
    """
    initial_x = ball.x
    initial_y = ball.y
    ball.move()
    assert ball.x == initial_x + ball.dx
    assert ball.y == initial_y + ball.dy
    "move should move the ball based on the dx and dy attributes."


def test_bounce_x(ball):
    """
    Test that the ball's x-direction reverses when bounce_x is called.
    """
    initial_dx = ball.dx
    ball.bounce_x()
    assert ball.dx == -initial_dx
    "bounce_x should reverse the x-direction"


def test_bounce_y(ball):
    """
    Test that the ball's y-direction reverses when bounce_y is called.
    """
    initial_dy = ball.dy
    ball.bounce_y()
    assert ball.dy == -initial_dy
    "bounce_y should reverse the y-direction"


def test_reset_position(ball):
    """
    Test that the ball resets to its initial position.
    """
    ball.x = 100
    ball.y = 200
    ball.reset_position()
    assert ball.x == 0 and ball.y == 100 - (SCREEN_HEIGHT / 2)
    "reset_position should reset the ball to (0, 0)"


def test_increase_speed(ball):
    """
    Test that the ball's speed increases when increase_speed is called.
    """
    initial_time_delay_between_ball_moves = ball.speed
    ball.increase_speed()
    assert ball.speed == 0.9 * initial_time_delay_between_ball_moves
    "increase_speed should increase the ball's speed by 10%,"
    "by reducing the speed attribute."
