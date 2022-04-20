import pygame
import random,time
import sys
pygame.init()
pygame.mixer.Sound('background.wav').play(-1)
score_font= pygame.font.SysFont("Verdana",20)
game_font=pygame.font.SysFont("comicsans",40)
FPS = 60
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
STEP = 5
ENEMY_STEP = 10
COIN_STEP=5
COLOR=(0,0,0)
BLACK=(0,0,0)

SCORE = 0
COIN_SCORE = 0
clock=pygame.time.Clock()
SURF= pygame.display.set_mode((SCREEN_WIDTH , SCREEN_HEIGHT))
pygame.display.set_caption("Street Racer")
game_over =game_font.render("GAME OVER", True, BLACK)
bg = pygame.image.load("racer_images/AnimatedStreet.png")

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image= pygame.image.load("racer_images/Enemy.png")
        self.rect=self.image.get_rect()
        self.rect.center =(random.randint(40,SCREEN_WIDTH - 40 ),0)    #coordinates where car starts moving
    def update(self):
        global SCORE
        self.rect.move_ip(0,ENEMY_STEP)
        if(self.rect.bottom > SCREEN_HEIGHT):
            SCORE += 1
            self.top=0
            self.rect.center = (random.randint(30,350),0)
    def draw(self,surface):
        surface.blit(self.image,self.rect)


# to blint player objects in the screen / Sprite - for visible game objects
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image= pygame.image.load("racer_images/Player.png")
        self.rect=self.image.get_rect()
        self.rect.center =(160,520)    #coordinates where car starts moving
    def update(self):
        pressed_keys=pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[pygame.K_LEFT]:
                self.rect.move_ip(-STEP,0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[pygame.K_RIGHT]:
                self.rect.move_ip(STEP,0)
    def draw(self,surface):
        surface.blit(self.image,self.rect)
#adding randomly apperating coins
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image= pygame.image.load("racer_images/coin.png")
        self.rect=self.image.get_rect()
        self.rect.center =(random.randint(40,SCREEN_WIDTH - 40 ),0)   
    def update(self):
        global COIN_SCORE
        self.rect.move_ip(0,COIN_STEP)
        if(self.rect.bottom > SCREEN_HEIGHT):
            COIN_SCORE+=1
            self.top=0
            self.rect.center = (random.randint(40,SCREEN_WIDTH - 40 ),0)
    def draw(self,surface):
        surface.blit(self.image,self.rect)
class Coin_Pink(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image= pygame.image.load("racer_images/PINK.png")
        self.rect=self.image.get_rect()
        self.rect.center =(random.randint(40,SCREEN_WIDTH - 40 ),0)   
    def update(self):
        global COIN_SCORE
        self.rect.move_ip(0,COIN_STEP)
        if(self.rect.bottom > SCREEN_HEIGHT):
            COIN_SCORE+=2
            self.top=0
            self.rect.center = (random.randint(40,SCREEN_WIDTH - 40 ),0)
    def draw(self,surface):
        surface.blit(self.image,self.rect)

P1= Player()
E1= Enemy()
C1=Coin()
CP=Coin_Pink()
enemies=pygame.sprite.Group()
enemies.add(E1)
coins=pygame.sprite.Group()
coins.add(C1)
coin_p=pygame.sprite.Group()
coin_p.add(CP)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    P1.update()
    E1.update()
    C1.update()
    CP.update()
    if pygame.sprite.spritecollideany(P1,enemies):
        pygame.mixer.Sound('crash.wav').play(0)
        SURF.fill((255,0,0))
        SURF.blit(game_over, (100,250))
        pygame.display.update() 
        time.sleep(3)
        pygame.quit()
        sys.exit()  
    if pygame.sprite.spritecollideany(P1,coins):
        pygame.mixer.Sound('coin_s.wav').play(0)
        C1.update()
    if pygame.sprite.spritecollideany(P1,coin_p):
        pygame.mixer.Sound('coin_s.wav').play(0)
        CP.update()
        


    SURF.blit(bg,( 0 , 0 ))
    P1.draw(SURF)
    E1.draw(SURF)
    C1.draw(SURF)
    CP.draw(SURF)
    #Increase the speed of Enemy when the player earns N coins
    if (COIN_SCORE == 10):
        ENEMY_STEP+= 5



    score_img= score_font.render("Score"+":"+str(SCORE),True,COLOR)
    SURF.blit(score_img,(300,10))
    coin_img=score_font.render("Coins"+":"+str(COIN_SCORE),True,COLOR)   #Showing the number of collected coins in the top right corner  
    SURF.blit(coin_img,(300,60))
    pygame.display.update()
    clock.tick(FPS)
