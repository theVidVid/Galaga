import pygame

from pygame.sprite import Sprite


class Missile(Sprite):
    """A class to manage missiles fired from the spaceship."""

    def __init__(self, ga_game):
        """Create a missile object at the spaceship's current position."""
        super().__init__()
        self.screen = ga_game.screen
        self.settings = ga_game.settings

        # Load image of missile and it's rectangle.
        self.missile = pygame.image.load('Images/sm_missile.png')
        self.rect = self.missile.get_rect()

        # Load the rectangle for the game screen.
        self.screen_rect = ga_game.screen.get_rect()

        # Set starting position of missile to be on top of ship
        self.rect.midtop = ga_game.ship.rect.midtop

        # Store the missile's position as a decimal value
        self.y = float(self.rect.y)

        # Reference stored missile speed settings
        self.speed_factor = self.settings.speed_factor

    def update(self):
        """Move the missile towards the top of screen."""
        self.y -= self.speed_factor
        self.rect.y = self.y

    def blitme(self):
        """Load the missile at its current location."""
        self.screen.blit(self.missile, self.rect)
