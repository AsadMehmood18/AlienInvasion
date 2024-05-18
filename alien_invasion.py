import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
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
        self.bullets = pygame.sprite.Group()                            # Create a group to store bullets.
        self.aliens = pygame.sprite.Group()
        
        self._create_fleet()
        
    
    def run_game(self):
        while True:                                                     # Start the main loop for the game.
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_bullets()
            self._update_aliens()
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
        elif event.key == pygame.K_SPACE:
            self.fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()
    
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
             self.ship.moving_left = False
        
    def fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    
    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
    
    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()
          
    
    def _create_fleet(self):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        current_x, current_y = alien_width, alien_height
        while current_y < self.settings.screen_height - 2*alien_height:
            while current_x < self.settings.screen_width - alien_width:
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width
            current_x = alien_width
            current_y += 2 * alien_height
    
    def _create_alien(self,x_position, y_position):
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)
    
    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    
    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
    
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)                        # Redraw the screen during each pass through the loop.
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()                                              # Draw the ship on the screen.
        self.aliens.draw(self.screen)
        pygame.display.flip()                                           # Make the most recently drawn screen visible.

if __name__=='__main__':                                                # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()