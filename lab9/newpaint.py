import pygame
from math import sqrt

pygame.init()
# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (20, 20, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

screen = pygame.display.set_mode((700, 550))
run = True

clock = pygame.time.Clock()

color = BLACK

screen.fill(WHITE)
prev, cur = None, None
start = None

size = 1
x, y = 50, 50


while run:
    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():                  # close window
        if event.type == pygame.QUIT:
            run = False


        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_r:                 # change color
                color = RED
            if event.key == pygame.K_g:
                color = GREEN
            if event.key == pygame.K_b:
                color = BLUE
            if event.key == pygame.K_d:
                color = BLACK
            
            if event.key == pygame.K_SPACE:              # eraser
                color = WHITE if color != WHITE else BLACK
                size = 30 if size == 1 else 1

            if event.key == pygame.K_RIGHT:             # size of figures
                x +=10
                y +=10
            if event.key == pygame.K_LEFT:              # size of figures
                x -=10
                y -= 10

            if event.key == pygame.K_UP:               # draw rectangle
                start = pygame.mouse.get_pos()
                if start:
                    pygame.draw.rect(screen, color, (start[0], start[1], x, y), 4)
                    start = None
            if event.key == pygame.K_DOWN:               # draw circle
                start = pygame.mouse.get_pos()
                if start:
                    pygame.draw.circle(screen, color, (start[0], start[1]), x, 4)   
                    start= None
            if event.key == pygame.K_2:                 # draw square
                start = pygame.mouse.get_pos()
                if start:
                    pygame.draw.rect(screen, color, (start[0], start[1], x, x), 4)
                    start = None
            if event.key == pygame.K_3:                 # draw equilateral triangle
                start = pygame.mouse.get_pos()
                if start:
                    pygame.draw.line(screen, color, (start[0], start[1]), (start[0] + x, start[1]), 4)
                    pygame.draw.line(screen, color, (start[0], start[1]), (start[0] + x/2, start[1]-sqrt(3)*x/2), 4)
                    pygame.draw.line(screen, color, (start[0]+x, start[1]), (start[0] + x/2, start[1]-sqrt(3)*x/2), 4)
                    start = None
            if event.key == pygame.K_4:                 # draw right triangle
                start = pygame.mouse.get_pos()
                if start:
                    pygame.draw.line(screen, color, (start[0], start[1]), (start[0] + x, start[1]), 4)
                    pygame.draw.line(screen, color, (start[0], start[1]), (start[0],  start[1]- x ), 4)
                    pygame.draw.line(screen, color, (start[0] + x, start[1]), (start[0],  start[1]- x ), 4)
                    start = None
            if event.key == pygame.K_5:                 # draw rhombus
                start = pygame.mouse.get_pos()
                if start:
                    pygame.draw.line(screen, color, (start[0], start[1]), (start[0] + x, start[1] - x), 4)
                    pygame.draw.line(screen, color, (start[0] + x, start[1] - x), (start[0] + 2*x,  start[1]), 4)
                    pygame.draw.line(screen, color, (start[0] + 2 * x, start[1]), (start[0] + x,  start[1] + x ), 4)
                    pygame.draw.line(screen, color, (start[0] + x, start[1] + x), (start[0],  start[1]), 4)
                    start = None

        # if event.type == pygame.KEYDOWN : 
        #     if event.key == pygame.K_9:
        #         if event.type == pygame.MOUSEBUTTONDOWN:
        #             start = pygame.mouse.get_pos()
        #         if event.type == pygame.MOUSEBUTTONUP:
        #             end = pygame.mouse.get_pos()
        #             if start:
        #                 pygame.draw.rect(screen, color, (start[0], start[1], end[0]-start[0], end[1]-start[1]))
        #                 start = None
            



        if event.type == pygame.MOUSEBUTTONDOWN:         # painting
            prev = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEMOTION:
            cur = pygame.mouse.get_pos()
            if prev:
                pygame.draw.line(screen, color, prev, cur, size)
                prev = cur
        if event.type == pygame.MOUSEBUTTONUP:
            prev = None
            




    pygame.display.flip()
    clock.tick(30)

pygame.quit()