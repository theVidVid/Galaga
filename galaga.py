import sys

import pygame

from background import BackgroundImage

from settings import Settings

from ship import SpaceShip

from missile import Missile

from alien import Alien


class GalagaGame:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Galaga")
        self.ship = SpaceShip(self)
        self.missiles = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()
        self.background = BackgroundImage(self.settings, self.screen)

    def run_game(self):
        """Start the main game loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self.missiles.update()
            self._update_missile()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses"""
        if event.key == pygame.K_RIGHT:
            # Move the ship to the right
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # Move the ship to the left
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            # Fires a missile
            self._fire_missile()
        elif event.key == pygame.K_q:
            # Pressing the 'q' key quits the game.
            sys.exit()

    def _check_keyup_events(self, event):
        """Respond to key releases"""
        if event.key == pygame.K_RIGHT:
            # Stops the rightward movement of the ship
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            # Stops the leftward movement of the ship
            self.ship.moving_left = False

    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Make an alien
        alien = Alien(self)
        alien_width = alien.rect.width

        # Find out the available space for an alien fleet
        available_space_x = self.settings.screen_width - 2 * alien_width
        number_aliens_x = available_space_x // (1 * alien_width)

        # Create the first row of aliens
        for alien_number in range(number_aliens_x):
            # Create an alien and place it in a row
            alien = Alien(self)
            alien.x = alien_width + 1.25 * alien_width * alien_number
            alien.rect.x = alien.x
            self.aliens.add(alien)

    def _fire_missile(self):
        """Load missile and add it to missiles group."""
        if len(self.missiles) < self.settings.missiles_allowed:
            new_missile = Missile(self)
            self.missiles.add(new_missile)

    def _update_missile(self):
        """Update position of missiles and get rid of old missiles."""
        for missile in self.missiles.copy():
            if missile.rect.bottom <= 0:
                self.missiles.remove(missile)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.background.blitme()
        self.ship.blitme()
        for missile in self.missiles.sprites():
            missile.blitme()
        self.aliens.draw(self.screen)

        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    gg = GalagaGame()
    gg.run_game()
