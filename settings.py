

class Settings:
    def __init__(self):
        self.screen_width = 600
        self.screen_height = 400
        self.bg_color = (233, 233, 233)     #(120, 81, 169) is a shade of purple.
        self.caption = "Alien Invasion 🎮🚀👽"
        self.ship_speed = 1.5
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1                #1 represents right, -1 represents left.
        
        #Bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (120, 81, 169)
        self.bullets_allowed = 3