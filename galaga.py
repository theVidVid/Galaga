import sys

import pygame

from background import BackgroundImage

from settings import Settings

from ship import SpaceShip

from missile import Missile

from alien import GreenWing, BlueWing, RedWing, TealWing


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
        self.green_aliens = pygame.sprite.Group()
        self.blue_aliens = pygame.sprite.Group()
        self.red_aliens = pygame.sprite.Group()
        self.teal_aliens = pygame.sprite.Group()
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
        # Make a green, blue, red, and teal wing alien
        green_alien = GreenWing(self)
        green_width = green_alien.rect.width
        green_height = green_alien.rect.height
        blue_alien = BlueWing(self)
        blue_width = blue_alien.rect.width
        blue_height = blue_alien.rect.height
        red_alien = RedWing(self)
        red_width = red_alien.rect.width
        red_height = red_alien.rect.height
        teal_alien = TealWing(self)
        teal_width = teal_alien.rect.width
        teal_height = teal_alien.rect.height

        # Find out the available space for an alien fleet
        green_space_x = self.settings.screen_width - 1 * green_width
        green_number_aliens_x = green_space_x // (1 * green_width)
        blue_space_x = self.settings.screen_width - 2 * blue_width
        blue_number_aliens_x = blue_space_x // (1 * blue_width)
        red_space_x = self.settings.screen_width - 2 * red_width
        red_number_aliens_x = red_space_x // (1 * red_width)
        teal_space_x = self.settings.screen_width - 2 * teal_width
        teal_number_aliens_x = teal_space_x // (1 * teal_width)

        # Create the first row of green wing aliens
        for alien_number in range(green_number_aliens_x):
            # Create a green wing alien and place it in a row
            alien = GreenWing(self)
            alien.x = green_width + 0.75 * green_width * alien_number
            alien.rect.x = alien.x
            self.green_aliens.add(alien)

        # Create the first row of blue wing aliens
        for alien_number in range(blue_number_aliens_x):
            # Create a blue wing alien and place it in a row
            alien = BlueWing(self)
            alien.x = blue_width + 1.25 * blue_width * alien_number
            alien.rect.x = alien.x
            self.blue_aliens.add(alien)

        # Create the first row of red wing aliens
        for alien_number in range(red_number_aliens_x):
            # Create a red wing alien and place it in a row
            alien = RedWing(self)
            alien.x = red_width + 1.5 * red_width * (alien_number + 0.35)
            alien.rect.x = alien.x
            self.red_aliens.add(alien)

        # Create the first row of teal wing aliens
        for alien_number in range(teal_number_aliens_x):
            # Create a blue wing alien and place it in a row
            alien = TealWing(self)
            alien.x = teal_width + 1.25 * teal_width * alien_number
            alien.rect.x = alien.x
            self.teal_aliens.add(alien)

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
        self.green_aliens.draw(self.screen)
        self.blue_aliens.draw(self.screen)
        self.red_aliens.draw(self.screen)
        self.teal_aliens.draw(self.screen)

        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    gg = GalagaGame()
    gg.run_game()
