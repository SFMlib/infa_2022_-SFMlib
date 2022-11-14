import pygame
from pygame.draw import *
from random import randint
import math


pygame.init()

FPS = 60

LIMX = 1536
LIMY = 864

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

screen = pygame.display.set_mode((LIMX, LIMY))


def new_ball():
    '''рисует новый шарик '''
    r = randint(50, 100)
    
    x = randint(r + 1, LIMX - r - 1)
    y = randint(r + 1, LIMY - r - 1)
    
    vx = randint(-4, 4)
    vy = randint(-4, 4)
    color = COLORS[randint(0, 5)]
    
    m = randint(0, 1)
    C = 5
    if not m:
        vx *= C
        vy *= C
        r //= 2
    return [screen, color, x, y, vx, vy, r, m]


def move(Ball):
    x = Ball[2]
    y = Ball[3]
    r = Ball[6]
    m = Ball[7]
    if x >= LIMX - r or x < r:
        Ball[4] *= -1
    if y >= LIMY - r or y < r:
        Ball[5] *= -1
    elif m:
        Ball[5] += 1
    Ball[2] += Ball[4]
    Ball[3] += Ball[5]
    return Ball


def draw_ball(Ball):
    circle(Ball[0], Ball[1], (Ball[2], Ball[3]), Ball[6])


pygame.display.update()
clock = pygame.time.Clock()
finished = False

Balls = []
Score = 0


while not finished:
    clock.tick(FPS)
    text_score = "Score " + str(Score)
    font = pygame.font.Font(None, 72)
    text = font.render(text_score, True, RED)
    place = text.get_rect(center=(125, 50))
    
    if len(Balls) < 10 and randint(1, 50) == 1:
        b = new_ball()
        Balls.append(b)
    for b in Balls:
        b = move(b)
        draw_ball(b)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for b in Balls:
                xb, yb, rb, mb = b[2], b[3], b[6], b[7]
                xm, ym = event.pos
                d = math.sqrt((xm - xb) ** 2 + (ym - yb) ** 2)
                if d < rb:
                    print('Click!')
                    if mb:
                        Score += 1
                    else:
                        Score += 2
                    Balls.remove(b)
    new_ball()
    screen.blit(text, place)
    
    pygame.display.update()
    screen.fill(BLACK)
print(text_score)
pygame.quit()
