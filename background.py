import pygame


class BackgroundImage:
    """Models background for Rocket Riders game."""
    def __init__(self, ai_settings, screen):
        """Initializes image for game background."""
        self.screen = screen
        self.ai_settings = ai_settings

        # Loads the image and its rectangles
        self.image = pygame.image.load(
            'images/galaga_background.png').convert()
        self.rect = self.image.get_rect()

        # Load the rectangle representing the game screen.
        self.screen_rect = screen.get_rect()

    def blitme(self):
        """Draw the background at its current location."""
        self.screen.blit(self.image, self.rect)
