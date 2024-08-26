import pygame

class Settings:
    def __init__(self):
        self.screen_width = 960
        self.screen_height = 540
        self.bg = pygame.image.load('Images/space.bmp')
        self.caption = "Alien Invasion 🎮🚀👽"
        
        #Ship settings
        self.ship_limit = 2
        
        #Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (120, 81, 169)
        self.bullets_allowed = 3
        
        #Alien settings
        self.fleet_drop_speed = 10
        
        #Score settings
        self.alien_points = 50
        
        #How quickly the game speeds up
        self.speedup_scale = 1.2
        
        #How quickly the alien point values increase
        self.score_scale = 1.5
        
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
        
        self.alien_points = int(self.alien_points * self.score_scale) 
        