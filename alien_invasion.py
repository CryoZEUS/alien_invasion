import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """Overall class to manage game assets and behaviour."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        
        pygame.init()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode((1280, 720), pygame.HWSURFACE)
        self.settings.screen_width = self.screen.get_rect().width        
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")        

        #Set background colour in RGB values
        self.bg_color = (230,230,230)

        #Create instance of ship after screen has been created.
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

        self.aliens = pygame.sprite.Group()
        #Group method draws all elements of the group to the screen

        self._create_fleet()

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
            
    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        #Update bullet position.
        self.bullets.update()

        #Get rid of bullets that have disappeared.
        for bullets in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullets)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen) #Draws each element in group to screen uing rect attribute.

        #Make the most recetly drawn screen visible.
        pygame.display.flip()

    def _check_events(self):
        """Respond to keypresses and mouse events."""

        #Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
                

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                            
    def _check_keydown_events(self,event):
        """Respond to key presses."""
        if event.key == pygame.K_RIGHT:
            #Move the ship to the right.
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        #Pressing 'q' to quit
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            #Move the ship to the left?
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet nd add it to the bullets group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _create_fleet(self):
        """Create a fleet of aliens."""
        #Create an alien and find number of aliens in a row.
        #Space between aliens is equal to one alien width.
        alien = Alien(self)
        alien_width, alien_height  = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        #Determine the number of rows of aliens that fit on the screen
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        #Create full fleet of aliens.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """Create an alien and place it on the row."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)



if __name__ == '__main__':
    #Make game instance and run game.
    ai = AlienInvasion()
    ai.run_game()
    


