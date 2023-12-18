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

        #Start each new ship at the center of the screen.
        self.rect.center = self.screen_rect.center

        #Movement Flag 
        self.moving_right = False 
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False 

    def update(self):
        """update the ship's position based on the movement flag"""
        if self.moving_right: 
            self.rect.x += 10
        if self.moving_left:
            self.rect.x -= 10
        if self.moving_up:
            self.rect.y -= 10
        if self.moving_down:
            self.rect.y += 10
        


    def blitme(self): #blitme() method draws the image to the screen at the position specified by self.rect
        """Draw the ship at its current location """
        self.screen.blit(self.image, self.rect)