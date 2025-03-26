from turtle import Turtle
import os
from breakout.constants import SCREEN_WIDTH, SCREEN_HEIGHT
from breakout.constants import ALIGNMENT, FONT, COLOR_SCORE


class Scoreboard(Turtle):
    """
    A class to represents the scoreboard in the breakout game.
    """
    def __init__(self):
        """
        Initializes the scoreboard object.
        """
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.file_path = os.path.join(os.path.dirname(__file__), 'data.txt')
        self.load_high_score()
        self.lives = 3
        self.level = 1
        self.color("white")
        self.penup()
        self.goto(0, ((SCREEN_HEIGHT / 2) - 60))
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Updates the scoreboard with
        current level, current score, high score, and lives.
        """
        self.clear()
        self.goto(-SCREEN_WIDTH/2+10, ((SCREEN_HEIGHT / 2) - 60))
        self.write(f"Level: {self.level}",
                   True, align="left", font=FONT)
        self.goto(-110, ((SCREEN_HEIGHT / 2) - 60))
        self.write(f"Score: {self.score}",
                   True, align=ALIGNMENT, font=FONT)
        self.goto(60, ((SCREEN_HEIGHT / 2) - 60))
        self.write(f"High-Score: {self.high_score}",
                   True, align=ALIGNMENT, font=FONT)
        self.goto(SCREEN_WIDTH/2-30, ((SCREEN_HEIGHT / 2) - 60))
        self.write(f"Lives: {max(self.lives, 0)}",
                   True, align="right", font=FONT)

    def increase_score(self, brick_color):
        """
        Increases the score based on the brick color.
        """
        self.score += COLOR_SCORE[brick_color]
        self.update_scoreboard()

    def lose_life(self):
        """
        Decreases the lives by 1.
        """
        self.lives -= 1
        self.update_scoreboard()

    def next_level(self):
        """
        Increases the level by 1.
        Increases the lives by 3.
        Displays message letting the user know they are levelling up.
        """
        self.level += 1
        self.lives = self.lives + 3
        self.update_scoreboard()
        self.goto(0, 0)
        self.write(("LEVELLING UP"), True, align=ALIGNMENT, font=FONT)

    def game_over(self):
        """
        Displays the game over message.
        If the current score is higher than the high score,
        updates the high score.
        """
        self.goto(0, 0)
        self.write("GAME OVER", True, align=ALIGNMENT, font=FONT)
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()

    def load_high_score(self):
        """
        Loads the high score from the data.txt file.
        """
        with open(self.file_path) as file:
            data = file.read()
            if len(data) > 0:
                self.high_score = int(data)
            else:
                self.high_score = 0

    def save_high_score(self):
        """
        Saves the high score to the data.txt file.
        """
        with open(self.file_path, mode="w") as file:
            file.write(f"{self.high_score}")
