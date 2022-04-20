import pygame
import random
import time
from pygame import mixer

pygame.init()

# цвета
BLACK = (0, 0, 0)
GREY = (66, 73, 73)
GREEN = (46, 204, 113)
RED = (231, 76, 60)
BLUE = (31, 97, 141)
YELLOW = (241, 196, 15)

# text
font1 = pygame.font.SysFont("Voltec", 50) # шрифт и размер
font_medium = pygame.font.SysFont("Voltec", 40)
font_big = pygame.font.SysFont("Voltec", 70)
game_over = font_medium.render("Game Over", True, (250,250,250))
winning = font1.render("YOU WON!", True, (244, 208, 63 ))
restart1 = font_medium.render("Press R to restart", True, (244, 208, 63 ))


# переменные для счетчиков уровней и собранных очков,и тд
WIDTH = 500
HEIGHT = 500
BLOCK_SIZE = 20 # размер  одной стороны каждого блока
score = 0
level = 1
limit = 5


clock = pygame.time.Clock()
FPS = 8
time_event = None

# создание дисплэя
screen = pygame.display.set_mode((500, 560))  
pygame.display.set_caption("ZHYLAN")

# бэкграунд музыка
pygame.mixer.music.load("background.ogg")
pygame.mixer.music.set_volume(0.18)
mixer.music.play(-1)


# функция для создания разметки клеток на заднем плане
def draw_grid():
    for i in range(0, 500, BLOCK_SIZE): # для х: с 0 до 500 пикселей и через каждые 20 пикселей(блок-сайз)
        for j in range(0, 500, BLOCK_SIZE): # для у: с 0 до 500 пикселей и через каждые 20 пикселей(блок-сайз)
            pygame.draw.rect(screen, GREY, (i, j, BLOCK_SIZE, BLOCK_SIZE), 1) # рисует квадраты на координатах i и j c шириной и высотой равные  BLOCK_SIZE, и с толщиной стенки равный 1


# класс для еды 
class Food: 
    def __init__(self): # инициализация новой позиции
        self.generate_random_pos()
  
    # создание рандомных координат для еды
    def generate_random_pos(self):
        self.x = random.randint(0, 24) # получаем рандомное значение для х
        self.y = random.randint(0, 24) # получаем рандомное значение для у
    
    # рисование блоков
    def draw(self):
        pygame.draw.rect(screen, RED, (self.x * BLOCK_SIZE, self.y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

# класс для супер еды 
class Super_Food: 
    def __init__(self): # инициализация новой позиции
        self.generate_random_pos()
  
    # создание рандомных координат для еды
    def generate_random_pos(self):
        self.x = random.randint(0, 24) # получаем рандомное значение для х
        self.y = random.randint(0, 24) # получаем рандомное значение для у
    
    # рисование блоков
    def draw(self):
        pygame.draw.rect(screen, YELLOW, (self.x * BLOCK_SIZE, self.y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

    def check(self, f1 : Food):
        if f1.x == self.x and f1.y == self.x:
            self.generate_random_pos()
    
    def out_of_time(self):
        self.x = 30
        self.y = 30

# класс змеи
class Snake:
    def __init__(self):
        self.body = [[10, 10]] # массив змейки 
        self.dx = 1  #скорость по х
        self.dy = 0 # скорость по у 
        self.destination = '' # направление змейки 
        self.color = GREEN 

    def move(self):
        for event in events: # проверяем все ивенты 
            if event.type == pygame.KEYDOWN: # если нажимаем на клавишу 
                if event.key == pygame.K_LEFT and self.destination != 'right': # если нажимаем на левую клавишу и змейка не направлена на право
                    self.dx = -1
                    self.dy = 0
                    self.destination = 'left'
                if event.key == pygame.K_RIGHT and self.destination != 'left': # если нажимаем на правую клавишу и змейка не направлена на лево
                    self.dx = 1
                    self.dy = 0
                    self.destination = 'right'
                if event.key == pygame.K_UP and self.destination != 'down': # если нажимаем на верхнюю клавишу и змейка не направлена вниз
                    self.dx = 0
                    self.dy = -1
                    self.destination = 'up'
                if event.key == pygame.K_DOWN and self.destination != 'up': # если нажимаем на нижнюю клавишу и змейка не направлена на вверх
                    self.dx = 0
                    self.dy = 1
                    self.destination = 'down'

        for i in range(len(self.body) - 1, 0, -1): # добавление блока в тело змейки 
            self.body[i][0] = self.body[i - 1][0]
            self.body[i][1] = self.body[i - 1][1]
        
        self.body[0][0] += self.dx  # двигаем постоянно
        self.body[0][1] += self.dy  # двигаем постоянно

        #чтобы змея проходила скозь экран и выходила с противополжной стороны
        if self.body[0][0] >= 25:
            self.body[0][0] = 0
        if self.body[0][0] < 0:
            self.body[0][0] = 25

        if self.body[0][1] >= 25:
            self.body[0][1] = 0                                                                                             
        if self.body[0][1] < 0:
            self.body[0][1] = 24
   
    def draw(self): # для рисования самой змеи и ее тела
        for block in self.body:
            x1 = block[0] * BLOCK_SIZE 
            y1 = block[1] * BLOCK_SIZE
            pygame.draw.rect(screen, self.color, (x1, y1 , BLOCK_SIZE, BLOCK_SIZE))
      
    
    def collide_self(self):  # проверка столкновения с самим собой
        global finished, lose
        if self.body[0] in self.body[2:]:
            finished = True
            lose = True

    def check_food(self, f: Food): # проверка чтобы еда не появилась в змейке
        if [f.x, f.y] in self.body:
            f.generate_random_pos()
            global food_yes
            food_yes = True
    
    def check_food2(self, f1: Super_Food): # проверка чтобы еда не появилась в змейке
        if [f1.x, f1.y] in self.body:
            f1.generate_random_pos()
            global food_yes
            food_yes = True
        
# класс для стенок (уровней)
class Wall:
    def __init__(self):
        global level
        self.body = [] # список для координат стенок
        self.load_W(level)
    
    # чтение уровней и их создание
    def load_W(self, level):

        if level == 5: # при прохождении всех уровней , выходит иконка победы
            time.sleep(1)
            mixer.music.stop()
            pygame.mixer.music.load("win.wav")
            mixer.music.play()

            screen.fill((155, 89, 182)) 
            screen.blit(winning, (150, 230))
            pygame.display.update()
            time.sleep(8)
            pygame.quit()


        with open(f'levels/level{level}.txt', 'r') as f: # читает с папки levels  файлы с названием level{порядковый номер}
            W_body = f.readlines()

        # с enumerate  получаем сразу индекс и значение полученного аргумента
        for i, line in enumerate(W_body): # после прочтения, смотрим на индекс и значение (линии)
            for j, value in enumerate(line): # пробегаемся по индексам линии и ее значениям
                if value == '#': 
                    self.body.append([j, i]) # добавляем в список координаты , где должны быть стенки
                if value == "@":
                    for block in S.body:
                        block[0] = j
                        block[1] = i
                        pygame.draw.rect(screen, S.color, (block[0] * BLOCK_SIZE, block[1] * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))



    def clear(self):
        self.body.clear()# очистка массива перед  добавлением нового уровня

    def draw(self):
        for x, y in self.body: # пробегаемся по списку стенок
            pygame.draw.rect(screen, BLUE, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)) # рисуем стенку с размерами 20 х 20 и координаты равны х * 20 и у * 20, потому что блоки создаются только через каждые 20 пикселей

            
  
S = Snake()
F = Food()
SF = Super_Food()
W = Wall()



finished = False
lose = False
food_yes = False

# time_event = pygame.USEREVENT + 1

while not finished:
    events =  pygame.event.get()


    for event in events:
        if event.type == pygame.QUIT:
            finished = True
            
    screen.fill(BLACK) # заполняем экран черным
    
    draw_grid() # рисование клетки
    
    S.draw() # рисует голову змея а в дальнейшем и все ее тело
    S.check_food(F)
    S.move() #  чтобы двигать змею и принимать все ивенты
    W.draw() # рисует стенки уровня
    S.collide_self()
    

    # коллизия тела и стены
    for x, y in W.body:
        if S.body[0][0] * BLOCK_SIZE ==  x * BLOCK_SIZE  and S.body[0][1] * BLOCK_SIZE == y * BLOCK_SIZE:
            finished = True
            lose = True

    # коллизия еды и стены
    for x, y in W.body:
        if F.x * BLOCK_SIZE == x * BLOCK_SIZE and F.y * BLOCK_SIZE == y * BLOCK_SIZE:
            F.generate_random_pos()

    # коллизия  супер еды и стены
    for x, y in W.body:
        if SF.x * BLOCK_SIZE == x * BLOCK_SIZE and SF.y * BLOCK_SIZE == y * BLOCK_SIZE:
            SF.generate_random_pos()

    
    #коллизия еды и змеи
    if score % 4 != 0 or score == 0:
        F.draw() # рисует еду
        if S.body[0][0] * BLOCK_SIZE == F.x * BLOCK_SIZE and S.body[0][1] * BLOCK_SIZE == F.y * BLOCK_SIZE: # тип если координата змеи по Х и еды по Х, и если коорданата змеи по У и еды по У совпадают
            S.body.append([0, 0]) # в тело добавляем новый блок
            F.generate_random_pos() # создаем еду в другом рандомном месте
            
            score += 1

            #звуковое сопровождение
            s1 = pygame.mixer.Sound("coin_s.wav") 
            s1.set_volume(1.0)
            s1.play()

            
            #если очки будут привышать лимит в 5, 10, 15 очков
            if score >= limit:
                s2 = pygame.mixer.Sound("win.wav")
                s2.set_volume(1.0)
                s2.play()

                level += 1 # изменяется уровень
                limit += 5
                FPS += 0.75 # изменяется скорость 

                W.clear() # убирает предыдущий уровень для добавления другого
                W.load_W(level) # добавляет координаты нового уровня в список
    

    # если очки будут делиться на 4 без остатка то будет появлятся супер еда
    if score % 4 == 0 and score != 0:
        SF.draw()
        
        # pygame.time.set_timer(time_event, 2000)
        # time_event = pygame.time.get_ticks()
        
        for event in events:
            if event.type == time_event:
                SF.out_of_time()

        if S.body[0][0] * BLOCK_SIZE == SF.x * BLOCK_SIZE and S.body[0][1] * BLOCK_SIZE == SF.y * BLOCK_SIZE: # тип если координата змеи по Х и еды по Х, и если коорданата змеи по У и еды по У совпадают
            S.body.append([0, 0]) # в тело добавляем новый блок
            S.body.append([0, 0]) # +1 
            SF.generate_random_pos() # создаем еду в другом рандомном месте
            
            score += 3
            
            #звуковое сопровождение
            s1 = pygame.mixer.Sound("coin_s.wav") 
            s1.set_volume(1.0)
            s1.play()

            #если очки будут привышать лимит в 5, 10, 15 очков
            if score >= limit:
                s2 = pygame.mixer.Sound("win.wav")
                s2.set_volume(1.0)
                s2.play()

                level += 1 # изменяется уровень
                limit += 5
                FPS += 0.75 # изменяется скорость 

                W.clear() # убирает предыдущий уровень для добавления другого
                W.load_W(level) # добавляет координаты нового уровня в список
    
    # if time_event != None:
    #         if  pygame.time.get_ticks() - time_event == 2000:
    #                 SF.out_of_time()
    #                 SF.draw()
    #                 score -= 1



    while lose == True: # если игкок проиграл
        mixer.music.stop()
        screen.blit(game_over, (190,240))
        text = font_medium.render(f'Score: {score}', True, (255,255,255))
        screen.blit(text, (200, 270))    
        pygame.display.update()

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
                lose = False
                pygame.quit()

        
    # часть текста где выводится собранные очки и номер уровня
    font2 = pygame.font.SysFont("voltec", 35)
    text = font2.render(f'Score: {score}', True, RED)
    text_2 = font2.render(f'Level: {level}', True, RED)

    screen.blit(text, (30, 515))
    screen.blit(text_2, (370, 515))       

    clock.tick(FPS)
    pygame.display.update()

pygame.quit()