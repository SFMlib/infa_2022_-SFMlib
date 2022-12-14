import math
from random import choice

import pygame


FPS = 30

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
DARKGREEN = (0, 95, 0)
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN, DARKGREEN]

WIDTH = 800
HEIGHT = 600


class Ball:
    def __init__(self, screen: pygame.Surface, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 30
    
    def move(self):
        # FIXME
        if self.x >= WIDTH - r or self.x < self.r:
            self.vx *= -1
        if self.y >= HEIGHT - r or self.y < self.r:
            self.vy *= -1
        else:
            self.vy += 1
        self.x += self.vx
        self.y += self.vy
    
    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )
    def hittest(self, obj):
        d1 = self.r + obj.r
        d2 = math.sqrt((self.x - obj.x) ** 2 + (self.y - obj.y) ** 2)
        if d2 < d1:
            return True
        return False


class Gun:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.x = 20
        self.y = HEIGHT - 20
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.screen)
        new_ball.r += 5
        self.an = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.pos[1]-450) / (event.pos[0]-20))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        pygame.draw.rect(screen, GREEN, (self.x - 10, self.y - 15, 20, 30))
        pygame.draw.rect(screen, DARKGREEN, (self.x - 15, self.y - 18, 5, 36))
        pygame.draw.rect(screen, DARKGREEN, (self.x + 10, self.y - 18, 5, 36))
        pygame.draw.circle(screen, GREY, (self.x, self.y), 9)
        if self.f2_on == 0:
            pygame.draw.line(self.screen, self.color, (self.x, self.y), (self.x + 35 * math.cos(self.an),
                                                                         self.y + 35 * math.sin(self.an)), 7)
        else:
            pygame.draw.line(self.screen, self.color, (self.x, self.y),
                             (self.x + (35 + self.f2_power) * math.cos(self.an),
                              self.y + (35 + self.f2_power) * math.sin(self.an)), 7)
    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY

'''
class Target:
    # self.points = 0
    # self.live = 1
    # FIXME: don't work!!! How to call this functions when object is created?
    # self.new_target()

    def new_target(self):
        """ Инициализация новой цели. """
        x = self.x = rnd(600, 780)
        y = self.y = rnd(300, 550)
        r = self.r = rnd(2, 50)
        color = self.color = RED

    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.points += points

    def draw(self):
        
'''

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []

clock = pygame.time.Clock()
gun = Gun(screen)
#target = Target()
finished = False

while not finished:
    screen.fill(WHITE)
    gun.draw()
    #target.draw()
    for b in balls:
        b.draw()
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)
'''
    for b in balls:
        b.move()
        if b.hittest(target) and target.live:
            target.live = 0
            target.hit()
            target.new_target()
    gun.power_up()
'''
pygame.quit()
