import pygame
pygame.init()
screen=pygame.display.set_mode((600,400))
color=(255,0,0)
done=False
x=300
y=200
step=2
while not done :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done =True
    pressed=pygame.key.get_pressed()
    if pressed[pygame.K_UP] and y>0:
       y-=step
    elif pressed[pygame.K_DOWN] and y<600-25:
        y+=step
    elif pressed[pygame.K_LEFT] and x>0:
        x -=step
    elif pressed[pygame.K_RIGHT] and x<800-25:
        x+=step
    screen.fill((255,255,255))
    pygame.draw.circle(screen,color,(x,y),25)
    pygame.display.update()
