import sys
import pygame
from settings import Settings
from ship import Ship
# Alien Invasion Game by Asad Mehmood
class AlienInvasion:
    
    def __init__(self):
        pygame.init()                                                   # Initialize the game and create a game window.
        self.clock = pygame.time.Clock()                                # Set the clock class to control the frame rate.
        self.settings = Settings()                                      # Create an instance of Settings class.
        self.screen=pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))  # Set the screen size.
        pygame.display.set_caption(self.settings.caption)               # Set the caption of the game window.
        self.ship = Ship(self)                                          # Create an instance of the Ship class.
        
    
    def run_game(self):
        while True:                                                     # Start the main loop for the game.
            for event in pygame.event.get():                            # Watch for keyboard and mouse events.
                if event.type == pygame.QUIT:                           
                    sys.exit()                                          #quit the game
            self.screen.fill(self.settings.bg_color)                    # Redraw the screen during each pass through the loop.
            self.ship.blitme()                                          # Draw the ship on the screen.
            pygame.display.flip()                                       # Make the most recently drawn screen visible.
            self.clock.tick(60)                                         # Set the frame rate to 60 frames per second.

if __name__=='__main__':                                                # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()