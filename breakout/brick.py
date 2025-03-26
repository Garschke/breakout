from turtle import Turtle
from breakout.constants import SCREEN_WIDTH, SCREEN_HEIGHT
from breakout.constants import BRICKS_PER_ROW, BRICK_HEIGHT, COLORS


class BrickManager:
    """
    A class to represents the brick wall in the breakout game.
    """
    def __init__(self):
        """
        Initializes the brick wall.
        """
        self.brick_list = []
        self.create_bricks()

    def create_bricks(self):
        brick_width = SCREEN_WIDTH // BRICKS_PER_ROW - 1
        x_start_position = (brick_width - SCREEN_WIDTH) // 2
        y_start_position = ((SCREEN_HEIGHT // 2)
                            - ((len(COLORS) + 3) * BRICK_HEIGHT))
        for y_index in range(len(COLORS)):
            for x_index in range(BRICKS_PER_ROW):
                x_position = x_start_position + x_index * brick_width
                y_position = y_start_position + y_index * BRICK_HEIGHT
                position = (x_position, y_position)
                self.add_brick(position, COLORS[y_index])

    def add_brick(self, position, color):
        """
        Adds a brick to the brick wall.
        """
        new_brick = Turtle(shape="square")
        new_brick.color(color)
        new_brick.shapesize(stretch_wid=1, stretch_len=3)
        new_brick.penup()
        new_brick.goto(position)
        self.brick_list.append(new_brick)

    def remove_brick(self, brick):
        """
        Removes a brick from the brick wall.
        """
        self.brick_list.remove(brick)
        brick.goto(0, SCREEN_HEIGHT)
        del brick
