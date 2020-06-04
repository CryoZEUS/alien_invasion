import sys
import pygame

class AlienInvasion:
    """Overall class to manage game assets and behaviour."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("Alien Invasion")

        #Set background colour in RGB values
        self.bg_color = (0,0,0)

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            #Watch for keyboard and mouse events.
            for even in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #Redraw the screen during each pass through the loop.
            self.screen.fill(self.bg_color)

            #Make the most recetly drawn screen visible.
            pygame.display.flip()

if __name__ == '__main__':
    #Make game instance and run game.
    ai = AlienInvasion()
    ai.run_game()
    


