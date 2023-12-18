import sys

import pygame 

from settings import Settings

class AlienInvasion:
    """Overall class to manage game assets and behaviors"""

    def __init__(self): 
        """Initialize the game, and create game resources"""
        pygame.init() 
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        #set the background color -> this has been moved to setting file 
        ##self.bg_color = (0, 0, 255)

    def run_game(self):
        """start the main loop for the game"""
        while True: 
            #Watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit() 
            
            #Redraw the screen during each pass through the loop 
            self.screen.fill(self.settings.bg_color)

            pygame.display.flip() 

if __name__ == '__main__':
    # Make a game instance, and run the game
    ai = AlienInvasion() 
    ai.run_game()