import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall class to manage game assets and behaviour."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        
        pygame.init()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        #Set background colour in RGB values
        self.bg_color = (230,230,230)

        #Create instance of ship after screen has been created.
        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            #Watch for keyboard and mouse events.
            for even in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #Redraw the screen during each pass through the loop.
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            #Make the most recetly drawn screen visible.
            pygame.display.flip()

if __name__ == '__main__':
    #Make game instance and run game.
    ai = AlienInvasion()
    ai.run_game()
    


