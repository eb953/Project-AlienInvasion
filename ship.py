import pygame


class Ship: 
    """A class to manage the ship"""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect() ##rect -> rectangle 

        # Load the ship image and get its rect 
        self.image = pygame.image.load('images/Frida1_thumbnail.jpeg')
        self.rect = self.image.get_rect() 

        #Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom
    
    def blitme(self): #blitme() method draws the image to the screen at the position specified by self.rect
        """Draw the ship at its current location """
        self.screen.blit(self.image, self.rect)