import pygame
from random import randrange
import psycopg2

pygame.init()
config = psycopg2.connect("host=127.0.0.1 dbname=postgres user=postgres password=omarova09")
current = config.cursor()

width, height = 645, 645
screen = pygame.display.set_mode((width, height))
OK = True
length = 1
block_size = 15
background = pygame.image.load('s_back.jpg').convert()
settings = pygame.font.SysFont('Arial', 16, bold=True)
end_settings = pygame.font.SysFont('Arial', 66, bold=True)

x, y = randrange(0, width, block_size), randrange(0, height, block_size)
food2 = randrange(0, width, block_size), randrange(0, height, block_size)
snake = [(x, y)]
walls = []
dx, dy = 0, 0

timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event, 5000)

for i in range(10):
    wall = randrange(0, width, block_size), randrange(0, height, block_size)
    walls.append(wall)


print("What is your name?")
username = input()

select = '''
    SELECT * FROM res WHERE username = %s;
'''
current.execute(select, [username])
table = current.fetchone()

if table == None:
    insert = '''
        INSERT INTO res VALUES(%s, 0, 0);
    '''
    current.execute(insert, [username])
    config.commit()
pygame.init()

current.execute(select, [username])
table = current.fetchone()


clock = pygame.time.Clock()
FPS = 6


class Food1:
  def __init__(self):
      
      self.generate_random_pos()
  
  def generate_random_pos(self):
    self.x = randrange(0, width, block_size), randrange(0, height, block_size)
    
  def change_place(self):
    self.generate_random_pos()
  
  def draw(self):
    pygame.draw.rect(screen, pygame.Color('yellow'), (*self.x, block_size, block_size))

food1 = Food1()
level = table[2]
score = 0
highscore = table[1]
paused = False
print(highscore)
while OK:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      OK = False
    if event.type == timer_event:
      food2 = randrange(0, width, block_size), randrange(0, height, block_size)   

    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_RIGHT:
        dx = 1
        dy = 0
      if event.key == pygame.K_LEFT:
        dx = -1
        dy = 0
      if event.key == pygame.K_UP:
        dx = 0
        dy = -1
      if event.key == pygame.K_DOWN:
        dx = 0
        dy = 1
      if event.key == pygame.K_ESCAPE:
        OK= False
      
      if event.key == pygame.K_p:
        paused = True

  screen.blit(background, (0, 0))
#
  
  while food1 == snake  or food2 == snake  or food1 == food2 or food1 in walls or food2 in walls:
    food1.change_place()
    food2 = randrange(0, width, block_size), randrange(0, height, block_size)
  
  food1.draw()
  for i, j in snake:
    pygame.draw.rect(screen, pygame.Color('black'), (i, j, block_size - 1, block_size - 1))
  for i, j in walls:
    pygame.draw.rect(screen, pygame.Color('red'), (i, j, block_size, block_size))
  pygame.draw.rect(screen, pygame.Color('blue'), (*food2, block_size, block_size))
  
  x += dx * block_size
  y += dy * block_size
  snake.append((x, y))
  snake = snake[-length:]
        
    # eating food
  if snake[-1] == food1.x:
    while food1.x in snake:
      food1.change_place()
    length += 1
    score += 1
    if score % 5 == 0 and score != 0:
      FPS += 2
      level += 1
        
  elif snake[-1] == food2:
    while food2 in snake:
      food2 = randrange(0, width, block_size), randrange(0, height, block_size)
    length += 2
    score += 2
    if score % 5 == 0 and score != 0:
      FPS += 2
      level += 1

  if x < 0 or x > width - block_size or y < 0 or y > height - block_size or len(snake) > len(set(snake)) or snake[-1] in walls: 
    while True:
      render_end = end_settings.render('GAME OVER', True, pygame.Color('red'))
      screen.blit(render_end, (135, 280))
      pygame.display.flip()
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          exit()
  render_score = settings.render(f'SCORE: {score}', True, pygame.Color('red'))
  screen.blit(render_score, (5, 5))
  render_level = settings.render(f'LEVEL: {level}', True, pygame.Color('red'))
  screen.blit(render_level, (5, 20)) 
  while paused:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        OK = False
        paused = False
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_c:
          paused = False

    if score > highscore:
       highscore = score
    sql = '''
            UPDATE res SET score = %s, level = %s WHERE username = %s;
        '''
    current.execute(sql, [highscore, level, username])
    config.commit()
  
  if score > highscore:
    highscore = score
  sql = '''UPDATE res SET score = %s, level = %s WHERE username = %s;'''
  current.execute(sql, [highscore, level, username])
  config.commit()

  pygame.display.update()
  clock.tick(FPS)
current.close()
config.close()

