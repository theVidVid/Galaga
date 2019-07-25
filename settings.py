class Settings:
    """A class to store all settings for Galaga game."""

    def __init__(self):
        """Initialize game settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 675

        # Ship settings
        self.ship_speed = 5

        # Missile settings
        self.speed_factor = 1
        self.missiles_allowed = 4

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 1

        # Fleet direction, 1 = right and 0 = left
        self.fleet_direction = 1
