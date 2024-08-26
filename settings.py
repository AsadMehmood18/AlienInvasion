

class Settings:
    def __init__(self):
        self.screen_width = 600
        self.screen_height = 400
        self.bg_color = (233, 233, 233)     #(120, 81, 169) is a shade of purple.
        self.caption = "Alien Invasion 🎮🚀👽"
        
        #Ship settings
        self.ship_limit = 3
        
        #Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (120, 81, 169)
        self.bullets_allowed = 3
        
        #Alien settings
        self.fleet_drop_speed = 10
        
        #How quickly the game speeds up
        self.speedup_scale = 1.5
        
        self.initialize_dynamic_settings()
        
    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 1.5
        self.bullet_speed = 2.5
        self.alien_speed = 1.0
        self.fleet_direction = 1                #1 represents right, -1 represents left.
        
    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale