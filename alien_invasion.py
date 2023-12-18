import sys

import pygame 

from settings import Settings

from ship import Ship

class AlienInvasion:
    """Overall class to manage game assets and behaviors"""

    def __init__(self): 
        """Initialize the game, and create game resources"""
        pygame.init() 
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

        #set the background color -> this has been moved to setting file 
        ##self.bg_color = (0, 0, 255)

    def run_game(self):
        """start the main loop for the game"""
        while True: 
            #Watch for keyboard and mouse events
            self._check_events()
            self._update_screen()

    def _check_events(self): #A helper method does work insde a class but isn't meant to be called through an instance. A single leading underscore indicates a helper method 
            
        #Watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    #move ship using keys
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = True 
                    if event.key == pygame.K_LEFT:
                        self.ship.moving_left = True
                    if event.key == pygame.K_UP:
                        self.ship.moving_up = True 
                    if  event.key == pygame.K_DOWN:
                        self.ship.moving_down = True 
                        


    def _update_screen(self):
         """update images on the screen , and flip to the new screen"""
        #Redraw the screen during each pass through the loop 
         self.screen.fill(self.settings.bg_color)
         self.ship.blitme()
         pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game
    ai = AlienInvasion() 
    ai.run_game()

