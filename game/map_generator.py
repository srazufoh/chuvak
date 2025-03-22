from classes import *
from random import randint
from perfomance import *


class door(sprite.Sprite):
    def __init__(self, wall_color, x, y, w, h):
        super().__init__()
        self.image = Surface((w,h))
        self.image.fill(wall_color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def draw(self):
        win.blit(self.image, (self.rect.x, self.rect.y))


def generate():
    loot = dif * loot
    enemyes = randint((dif * enemyes - 1),(dif * enemyes + 1))

