import pygame 


import random

from pygame.locals import (
    RLEACCEL, 
    QUIT,
    K_UP,
    K_DOWN ,
    K_LEFT,
    K_ESCAPE,
    K_RIGHT,
    KEYDOWN,

)
#defining constants for the screen 
SCREEEN_WIDTH= 800
SCREEN_HEIGHT =600


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75,25))
        self.surf.fill((255,255,255))
        self.rect=self.surf.get_rect()
  #movement 
    def update(self,pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0 ,-1)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0 ,1)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-1,0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(1 ,0)
        #keeping it on the screen 
        if  self.rect.left<0:
            self.rect.left=0
                
        if  self.rect.top<=0:
            self.rect.top =0
                
        if  self.rect.right>SCREEEN_WIDTH:
            self.rect.right=SCREEN_HEIGHT
                
        if  self.rect.bottom>=SCREEN_HEIGHT:
            self.rect.bottom=SCREEN_HEIGHT
                
 


#enemies 
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy ,self ).__init__() 
        self.surf = pygame.Surface((20,10))
        self.surf.fill((25,255,255))
        self.rect= self.surf.get_rect(
             center=(
               random.randint(SCREEEN_WIDTH+20,SCREEEN_WIDTH+70 ),
                random.randint(0, SCREEN_HEIGHT),
            )
             )
        self.speed = random.randint(1,2)



    def update(self):
      self.rect.move_ip(-self.speed,0)
      if self.rect.right <0:
            self.kill()






pygame.init()




#creating screen object 
screen= pygame.display.set_mode((SCREEEN_WIDTH,SCREEN_HEIGHT))

#adding the enemies 
ADDENEMY =pygame.USEREVENT +1
pygame.time.set_timer(ADDENEMY,550)
    
#instantiating a player
player =Player()

enemies =pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)



#game loop
running= True 
  
while running :
    for event in pygame.event.get():
        #did the user hit a key
         if event.type ==KEYDOWN:
            
             #was the escape key  
           if event.key ==K_ESCAPE:
                running ==False

        #did the user click the close button 
         elif event.type ==QUIT:
               running = False
         elif event.type == ADDENEMY:
             #create the enemy 
             new_enemy =Enemy()

             enemies.add(new_enemy)
             all_sprites.add(new_enemy) 
           
     
     #get the set of keys pressed and check for user input
    pressed_keys = pygame.key.get_pressed()
    #updating the movement 
    player.update(pressed_keys)
    
    
    #enemy positions 
    enemies.update()

     #fill the screen 
    
    screen.fill((0,0,0))
    #draw the player
    for entity in all_sprites:
        screen.blit(entity.surf ,entity.rect)
    


# checkimg collision 
    if pygame.sprite.spritecollideany(player,enemies):
      player.kill
      running =False
    # update display 
    pygame.display.flip()


