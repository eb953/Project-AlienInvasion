import pygame


class Ship: 
    """A class to manage the ship"""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect() ##rect -> rectangle 

        # Load the ship image and get its rect 
        self.image = pygame.image.load('images/Frida1_thumbnail.jpeg')
        self.rect = self.image.get_rect() 

        #Start each new ship at the center of the screen.
        self.rect.center = self.screen_rect.center

        #store a decimal value for the ship's horizontal position & Vertical 
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        #Movement Flag 
        self.moving_right = False 
        self.moving_left = False    
        self.moving_up = False 
        self.moving_down = False

    def update(self):
        """update the ship's position based on the movement flag"""
        #update the ship's x value, not the rect
        if self.moving_right: 
            self.x += self.settings.ship_speed  
        if self.moving_left:
            self.x -= self.settings.ship_speed  
        if self.moving_up: 
            self.y -= self.settings.ship_speed  
        if self.moving_down:
            self.y += self.settings.ship_speed

        #update rext object from self.x and self.y 
        self.rect.x = self.x 
        self.rect.y = self.y
        


    def blitme(self): #blitme() method draws the image to the screen at the position specified by self.rect
        """Draw the ship at its current location """
        self.screen.blit(self.image, self.rect)