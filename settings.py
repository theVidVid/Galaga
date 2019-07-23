class Settings:
    """A class to store all settings for Galaga game."""

    def __init__(self):
        """Initialize game settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 675

        # Ship settings
        self.ship_speed = 1.5

        # Missile settings
        self.speed_factor = 1.1
        self.missiles_allowed = 3
