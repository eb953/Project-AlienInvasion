import sys

import pygame 

from settings import Settings

from ship import Ship

from bullet import Bullet

from alien import Alien

class AlienInvasion:
    """Overall class to manage game assets and behaviors"""

    def __init__(self): 
        """Initialize the game, and create game resources"""
        pygame.init() 
        self.settings = Settings()
        
        #FullScreen mode 

        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        #comment the above out and uncomment below to have game in pop out mode 
        #self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()    
        self.aliens = pygame.sprite.Group() 
        self._create_fleet()
    
        #set the background color -> this has been moved to setting file 
        ##self.bg_color = (0, 0, 255)

    def run_game(self):
        """start the main loop for the game"""
        while True: 
            #Watch for keyboard and mouse events
            self._check_events()
            self.ship.update()
            self._update_bullets()
            #print(len(self.bullets)) -> show case  that bullets are deleting in the terminal 
            self._update_aliens()
            self._update_screen()
            

    def _check_events(self): #A helper method does work insde a class but isn't meant to be called through an instance. A single leading underscore indicates a helper method 
            
        #Watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    #move ship using arror keys
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)
    

    def _check_keydown_events(self, event): 
        """resond to pressed keydown"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True 
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True 
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
             sys.exit() 
        elif event.key == pygame.K_SPACE:
            self._fire_bullet() 

    def _check_keyup_events(self, event):
        """respond to key releases"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False 
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False   
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False  
    
    def _fire_bullet(self):
        """create a new bullet and add it to the bullets group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets"""
        #Update bullet positions 
        #Get Rid of bullets that have disappeared
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet) 
        #check for any bullets that have hit aliens
        # if so, get rid of the bullet and the alien
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

    def _update_screen(self):
         """update images on the screen , and flip to the new screen"""
        #Redraw the screen during each pass through the loop 
         self.screen.fill(self.settings.bg_color)
         self.ship.blitme()
         for bullet in self.bullets.sprites():
                bullet.draw_bullet() 
         self.aliens.draw(self.screen)
         pygame.display.flip()

    def _create_fleet(self):
        """create the fleet of aliens"""
        alien = Alien(self)
        ##alien_width = alien.rect.width
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2*alien_width)
        number_aliens_x = available_space_x // (2*alien_width) # floor division // divides 2 numbers and drops any remainder, so we'll get an integer number of aliens 

        #determine the number of rows of aliens that fit on the screen 
        ship_height = self.ship.rect.height 
        available_space_y = (self.settings.screen_height - (3*alien_height) - ship_height)
        number_rows = available_space_y // (2*alien_height)

        #create the full fleet of aliens
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)    

      

    def _create_alien(self, alien_number, row_number):
        """create an alien and place it in a row"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size 
        alien.x = alien_width +2*alien_width *alien_number # the screen width is stored in settings.screen_width 
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height +2*alien.rect.height*row_number
        self.aliens.add(alien)
    
    def _check_fleet_edges(self):
        """respond appropriately if any aliesn have reached an edge"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._check_fleet_direction()
                break
    
    def _check_fleet_direction(self):
        """drop the entire fleet and change the fleet's direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1 

    def _update_aliens(self):
        """update the positions of all aliens in the fleet, check if the fleet is at an edge, then update the positions of all aliens in the fleet """
        self._check_fleet_edges()
        self.aliens.update() 
    

if __name__ == '__main__':
    # Make a game instance, and run the game
    ai = AlienInvasion() 
    ai.run_game()

