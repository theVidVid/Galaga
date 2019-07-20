import pygame


class SpaceShip:
    """Class representing the Galaga spaceship."""
    def __init__(self, ga_game):
        """Initialize the spaceship's starting position."""
        self.screen = ga_game.screen
        self.screen_rect = ga_game.screen.get_rect()

        # Load the ship image and get its rect
        self.image = pygame.image.load('Images/galaga_spaceship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
