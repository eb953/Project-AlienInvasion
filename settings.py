class Settings: 
    """A class to store all settings for Alien Invasion"""
    
    def __init__(self):
        """initializes the game's settings"""

        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (40,60,120)

        #inital value of speed 
        self.ship_speed = 1.5 

        #bullet settings
        self.bullet_speed = 1.0 
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 255, 255)
        self.bullets_allowed = 3 

        #alien settings
        self.alien_speed = 1.0 
        self.fleet_drop_speed = 1
        # fleet_direction of 1 represents right ; -1 represents left 
        self.fleet_direction = 1 


