import pygame

from pygame.sprite import Sprite


class GreenWing(Sprite):
    """Class representing an Alien battleship"""

    def __init__(self, ga_game):
        """Initialize the alien and set it's starting position."""
        super().__init__()
        self.screen = ga_game.screen
        self.settings = ga_game.settings

        # Load the alien image and set its rect attribute
        self.image = pygame.image.load('Images/green_enemy.png')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height * 0.05

    def update(self):
        """Move the alien to the left."""
        self.x += self.settings.alien_speed


class BlueWing(Sprite):
    """Class representing an Alien battleship"""
    def __init__(self, ga_game):
        """Initialize the alien and set it's starting position."""
        super().__init__()
        self.screen = ga_game.screen
        self.settings = ga_game.settings

        # Load the alien image and set its rect attribute
        self.image = pygame.image.load('Images/blue_enemy.png')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height * 4

        # Store the alien's exact horizontal and vertical position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """Move the alien to the right."""
        self.x -= self.settings.alien_speed


class RedWing(Sprite):
    """Class representing an Alien battleship"""
    def __init__(self, ga_game):
        """Initialize the alien and set it's starting position."""
        super().__init__()
        self.screen = ga_game.screen
        self.settings = ga_game.settings

        # Load the alien image and set its rect attribute
        self.image = pygame.image.load('Images/red_enemy.png')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height * 6.66

        # Store the alien's exact horizontal and vertical position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """Move the alien to the right."""
        self.x -= self.settings.alien_speed


class TealWing(Sprite):
    """Class representing an Alien battleship"""

    def __init__(self, ga_game):
        """Initialize the alien and set it's starting position."""
        super().__init__()
        self.screen = ga_game.screen
        self.settings = ga_game.settings

        # Load the alien image and set its rect attribute
        self.image = pygame.image.load('Images/teal_enemy.png')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height * 6

        # Store the alien's exact horizontal and vertical position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Store the alien's exact horizontal and vertical position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """Move the alien to the right."""
        self.x -= self.settings.alien_speed
