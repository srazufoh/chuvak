import pygame
import sys
from pygame.locals import *
from random import *
from classes import *
# Инициализация Pygame
pygame.init()

# Настройки экрана
WIDTH, HEIGHT = 1200, 800
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dungeon Survival")

# Цвета


loot = 0

import pygame
from random import *
import sys
from math import *

all_sprites = pygame.sprite.Group()
walls_group = pygame.sprite.Group()
enemies_group = pygame.sprite.Group()
loot_group = pygame.sprite.Group()

WHITE = (255, 255, 255)
DARKGRAY = (50, 50, 50)

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image_path, w, h, x, y, speed=0):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(image_path), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.add(all_sprites)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Enemy(GameSprite):
    def __init__(self, x, y):
        super().__init__("hero.jpg", 70, 70, x, y, 1)
        self.add(enemies_group)
        self.target = None

    def update(self):
        if self.target:

            dx = self.target.rect.x - self.rect.x
            dy = self.target.rect.y - self.rect.y
            distance = max(1, (dx**2 + dy**2)**0.5)
            
            self.rect.x += dx/distance * self.speed
            self.rect.y += dy/distance * self.speed

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill('darkgrey')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.add(walls_group, all_sprites)

    def generate_walls():
        # Генерация горизонтальных стен
        for row in range(5):
            y = 300 + row * 100
            for col in range(8):
                if randint(1, 3) < 2:
                    x = col * 150 + randint(20, 50)
                    Wall(x, y, 50, 10)

        # Генерация вертикальных стен
        for col in range(10):
            x = col * 100
            for row in range(6):
                if randint(1, 3) < 2:
                    y = row * 120 + randint(20, 50)
                    Wall(x, y, 10, 50)

class Player(GameSprite):
    def __init__(self, x, y):
        super().__init__("hero.jpg", 50, 50, x, y, 13)
        self.last_position = (x, y)

    def update(self):
        self.last_position = (self.rect.x, self.rect.y)
        keys = pygame.key.get_pressed()

        # Движение с учетом диагоналей
        dx, dy = 0, 0
        if keys[pygame.K_w] and self.rect.y > 100: dy -= self.speed
        if keys[pygame.K_s] and self.rect.y < 700: dy += self.speed
        if keys[pygame.K_a] and self.rect.x > 100: dx -= self.speed
        if keys[pygame.K_d] and self.rect.x < 1100: dx += self.speed

        # Нормализация диагональной скорости
        if dx != 0 and dy != 0:
            dx *= 0.7071
            dy *= 0.7071

        self.rect.x += dx
        self.rect.y += dy

        # Проверка коллизий
        self.check_collisions()

    def check_collisions(self):
        # С коллизиями стен
        if pygame.sprite.spritecollide(self, walls_group, False):
            self.rect.x, self.rect.y = self.last_position

        # С коллизиями врагов
        if pygame.sprite.spritecollide(self, enemies_group, False):
            self.kill()




class Loot(GameSprite):
    def __init__(self, x, y):
        super().__init__("coin2.png", 70, 70, x, y)
        self.add(loot_group)

    def update(self):
        # Проверка сбора игроком
        if pygame.sprite.spritecollide(self, [player], False):
            self.kill()
            all_sprites.empty()
            walls_group.empty()
            enemies_group.empty()
            game_init()
            global loot
            loot += 1



xs = (110, 600, 1000)
ys = (110, 700)
def game_init():
    global player
    player = Player(xs[randint(0,2)], ys[randint(0,1)])
    loot = Loot(choice(xs), randint(100, 700))
    # Генерация врагов
    for _ in range(3):
        enemy = Enemy(randint(200, 1000), randint(200, 600))
        enemy.target = loot
    
    # Генерация стен
    Wall.generate_walls()

font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

background = pygame.image.load('image.jpeg')
background = pygame.transform.scale(background, (WIDTH, HEIGHT)) 
clock = pygame.time.Clock()
game_init()

running = True
while running:
    win.blit(background, (0,0))
    
    # Обработка событий
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    

    all_sprites.update()
    draw_text(win,str(loot), 40, WIDTH/2, 50)

    all_sprites.draw(win)
    enemies_group.update()
    pygame.display.flip()
    clock.tick(40)

pygame.quit()
