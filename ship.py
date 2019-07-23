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

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's moving position based on the movement flag."""
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
