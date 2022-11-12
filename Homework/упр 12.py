import pygame
from pygame.draw import *
from random import randint
import math
pygame.init()

FPS = 60

LimX = 1400
LimY = 800

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

screen = pygame.display.set_mode((LimX, LimY))

def new_ball():
    '''рисует новый шарик '''
    r = randint(30, 100)
    
    x = randint(r + 1, LimX - r - 1)
    y = randint(r + 1, LimY - r - 1)
    
    vx = randint(-4, 4)
    vy = randint(-4, 4)
    color = COLORS[randint(0, 5)]
    
    m = randint(0, 1)
    return [screen, color, x, y, vx, vy, r, m]


def move(Ball):
    x = Ball[2]
    y = Ball[3]
    r = Ball[6]
    m = Ball[7]
    if x >= LimX - r or x < r:
        Ball[4] *= -1
    if y >= LimY - r or y < r:
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

while not finished:
    clock.tick(FPS)
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
                xb, yb, rb = b[2], b[3], b[6]
                xm, ym = event.pos
                d = math.sqrt((xm - xb) ** 2 + (ym - yb) ** 2)
                if d < rb:
                    print('Click!')
                    Balls.remove(b)
    new_ball()
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
