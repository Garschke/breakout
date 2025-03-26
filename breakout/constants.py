"""
This module contains all the constants used in the game.
"""
# Screen
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
# Ball
START_SPEED = 0.08  # very slow  0.1 | slow 0.08 | very fast 0.01
# Bricks
BRICKS_PER_ROW = 9
BRICK_HEIGHT = 25
COLORS = ["yellow", "yellow", "green", "green",
          "orange", "orange", "red", "red"]
# Scoreboard
COLOR_SCORE = {"yellow": 1,
               "green": 3,
               "orange": 5,
               "red": 7
               }
ALIGNMENT = "center"
FONT = ("Arial", 22, "normal")
# Paddle
INITIAL_PAUSE = False  # set to True to pause the game on launch
