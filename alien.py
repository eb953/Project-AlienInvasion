import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Create a class to represent a single alien in a fleet """

    def __init__(self, ai_game):
        """Initialize the alien into its starting position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        
        #load the alien into the screen
        self.image = pygame.image.load('images/E2_thumbnail.jpeg')
        self.rect = self.image.get_rect() 

        #start the alien at the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height 

        #store the alien into the horizontal position 
        self.x = float(self.rect.x)

    def update(self):
        """move the alien to the right"""
        self.x += self.settings.alien_speed
        self.rect.x = self.x