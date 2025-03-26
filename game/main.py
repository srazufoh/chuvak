import pygame
import sys
from pygame.locals import *
from random import *
from classes import *
from settings import *
# Initialize pygame
pygame.init()

# Настройки экрана
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dungeon Survival")

# Цвета
WHITE = (255, 255, 255)
DARKGRAY = (50, 50, 50)

# Game variables
loot = 0
player = None

# Positions
xs = (110, 600, 1000)
ys = (110, 700)

def game_init():
    global player
    player = Player(xs[randint(0,2)], ys[randint(0,1)])
    loot = Loot(choice(xs), randint(100, 700), player)
    # Генерация врагов
    for _ in range(3):
        enemy = Enemy(randint(200, 1000), randint(200, 600))
        enemy.target = player  # Changed to target player instead of loot
    
    # Генерация стен
    Wall.generate_walls()

font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

background = pygame.image.load('background.png')
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
    
    draw_text(win, str(loot), 40, WIDTH/2, 50)

    all_sprites.draw(win)
    enemies_group.update()
    player.update()
    for item in loot_group:
        item.update()

    pygame.display.flip()
    clock.tick(40)

pygame.quit()
sys.exit()