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
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))  # Set the screen size.
        #self.screen=pygame.display.set_mode((0, 0), pygame.FULLSCREEN)  # Set the screen fullsize.
        #self.settings.screen_width = self.screen.get_rect().width
        #self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption(self.settings.caption)               # Set the caption of the game window.
        self.ship = Ship(self)                                          # Create an instance of the Ship class.
        
    
    def run_game(self):
        while True:                                                     # Start the main loop for the game.
            self._check_events()
            self.ship.update()
            self._update_screen()                                      
            self.clock.tick(60)                                         # Set the frame rate to 60 frames per second.
    def _check_events(self):
        for event in pygame.event.get():                                # Watch for keyboard and mouse events.
                if event.type == pygame.QUIT:                           
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)
                      
    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
    
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
             self.ship.moving_left = False
    
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)                        # Redraw the screen during each pass through the loop.
        self.ship.blitme()                                              # Draw the ship on the screen.
        pygame.display.flip()                                           # Make the most recently drawn screen visible.

if __name__=='__main__':                                                # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()