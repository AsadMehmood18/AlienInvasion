import pygame


class Ship:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect() # Get the screen's rect attribute.
        
        self.image = pygame.image.load('Images/ship.bmp')
        self.rect = self.image.get_rect() # Load the ship image and get its rect.
        
        self.rect.midbottom = self.screen_rect.midbottom # Start each new ship at the bottom center of the screen.
        self.x = float(self.rect.x)
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right: #this is done to check if the ship is moving right and if it is within the screen.
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x    #this is done to update the position of the ship.
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)