
import pygame, sys 
from pygame.locals import * 
import random, time 
 
#Initialzing  
pygame.init() 
 
#Setting up FPS  
FPS = 60 
FramePerSec = pygame.time.Clock() 
 
#Creating colors 
BLACK = (0, 0, 0) 
WHITE = (255, 255, 255) 
RED   = (255, 0, 0) 
 
#Other Variables for use in the program 
SCREEN_WIDTH = 400 
SCREEN_HEIGHT = 600 
SPEED = 5 
SCORE = 0 
SCORE_COINS = 0 
N = 10 
#Setting up Fonts 
font = pygame.font.SysFont("Verdana", 60) 
font_small = pygame.font.SysFont("Verdana", 20) 
game_over = font.render("Game Over", True, BLACK) 
 
background = pygame.image.load("racer_images/AnimatedStreet.png") 
 
#Create a white screen  
DISPLAYSURF = pygame.display.set_mode((400,600)) 
DISPLAYSURF.fill(WHITE) 
pygame.display.set_caption("Game") 
 
 
class Enemy(pygame.sprite.Sprite): 
      def __init__(self): 
        super().__init__()  
        self.image = pygame.image.load("racer_images/Enemy.png") 
        self.rect = self.image.get_rect() 
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0) 
 
      def move(self): 
        global SCORE 
        self.rect.move_ip(0,SPEED) 
        if (self.rect.bottom > 600): 
            SCORE += 1 
            self.rect.top = 0 
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0) 
 
 
class Player(pygame.sprite.Sprite): 
    def __init__(self): 
        super().__init__()  
        self.image = pygame.image.load("racer_images/Player.png") 
        self.rect = self.image.get_rect() 
        self.rect.center = (160, 520) 
        
    def move(self): 
        pressed_keys = pygame.key.get_pressed() 
         
        if self.rect.left > 0: 
              if pressed_keys[K_LEFT]: 
                  self.rect.move_ip(-5, 0) 
        if self.rect.right < SCREEN_WIDTH:         
              if pressed_keys[K_RIGHT]: 
                  self.rect.move_ip(5, 0) 
        if pressed_keys[K_UP]: 
            if self.rect.bottom > 0: 
                self.rect.move_ip(0, -5)         
        if pressed_keys[K_DOWN]: 
            if self.rect.top < SCREEN_HEIGHT: 
                self.rect.move_ip(0, 5) 
 
class Coin(pygame.sprite.Sprite): 
      def __init__(self): 
        super().__init__()  
        self.image = pygame.transform.scale(pygame.image.load('racer_images/coin.png'), (25,24)) 
        self.rect = self.image.get_rect() 
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), random.randint(90,SCREEN_HEIGHT-90)) 
 
      def update(self): 
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), random.randint(90,SCREEN_HEIGHT-90)) 
                   
class Coin2(pygame.sprite.Sprite): 
      def __init__(self): 
        super().__init__()  
        self.image = pygame.transform.scale(pygame.image.load('racer_images/PINK.png'), (25,24)) 
        self.rect = self.image.get_rect() 
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), random.randint(90,SCREEN_HEIGHT-90)) 
 
      def update(self): 
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), random.randint(90,SCREEN_HEIGHT-90)) 
                   
 
#Setting up Sprites         
P1 = Player() 
E1 = Enemy() 
C1 = Coin() 
C2 = Coin2() 
 
#Creating Sprites Groups 
enemies = pygame.sprite.Group() 
enemies.add(E1) 
 
coins = pygame.sprite.Group() 
coins.add(C1) 
 
coins2 = pygame.sprite.Group() 
coins2.add(C2) 
 
all_sprites = pygame.sprite.Group() 
all_sprites.add(P1) 
all_sprites.add(E1) 
all_sprites.add(C1) 
all_sprites.add(C2) 
 
#Adding a new User event  
INC_SPEED = pygame.USEREVENT + 1 
pygame.time.set_timer(INC_SPEED, 1000) 
 
#Game Loop 
while True: 
       
    #Cycles through all events occuring   
    for event in pygame.event.get(): 
        if event.type == INC_SPEED: 
              SPEED += 0.5       
        if event.type == QUIT: 
            pygame.quit() 
            sys.exit() 
 
 
    DISPLAYSURF.blit(background, (0,0)) 
     
    #Displaying points on the screen for each passage of the enemy past the player 
    scores = font_small.render(str(SCORE), True, BLACK) 
    DISPLAYSURF.blit(scores, (10,10)) 
     
    #Withdrawal of points for coins 
    scores2 = font_small.render(str(SCORE_COINS), True, BLACK) 
    DISPLAYSURF.blit(scores2, (360,10)) 
     
    P1.move() 
    E1.move() 
 
    #Moves and Re-draws all Sprites 
    for entity in all_sprites: 
        DISPLAYSURF.blit(entity.image, entity.rect) 
         
 
    #To be run if collision occurs between Player and Enemy 
    if pygame.sprite.spritecollideany(P1, enemies): 
          pygame.mixer.Sound('crash.wav').play() 
          time.sleep(1) 
                    
          DISPLAYSURF.fill(RED) 
          DISPLAYSURF.blit(game_over, (30,250)) 
           
          pygame.display.update() 
          for entity in all_sprites: 
                entity.kill()  
          time.sleep(2) 
          pygame.quit() 
          sys.exit()    
 
    #To be run if collision occurs between Player and Coin 
    if pygame.sprite.spritecollideany(P1, coins): 
          SCORE_COINS += 1 
          for entity in coins: 
            entity.update() 
    if pygame.sprite.spritecollideany(P1, coins2): 
          SCORE_COINS += 10 
          for entity in coins2: 
            entity.update() 
 
    #When the number of coins exceeds N the enemy's speed will increase 
    if SCORE_COINS >= 50: 
        SPEED = 15 
         
    pygame.display.update() 
    FramePerSec.tick(FPS)