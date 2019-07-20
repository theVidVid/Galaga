import sys

import pygame

from background import BackgroundImage

from settings import Settings


class GalagaGame:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Galaga")

        background = BackgroundImage(self.settings, self.screen)

    @staticmethod
    def run_game():
        """Start the main game loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    sys.exit()

                # Make the most recently drawn screen visible.
                pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    gg = GalagaGame()
    gg.run_game()
