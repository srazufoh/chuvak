from pygame import *
import random 
import sys
from math import *
from perfomance import *


win = display.set_mode((WIDTH, HEIGHT))




class GameSprite(sprite.Sprite):
    def __init__(self, w, h , name_image, speed, x, y):
        super().__init__()
        self.image = transform.scale(image.load(name_image), (w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def draw(self):
        win.blit(self.image, (self.rect.x, self.rect.y)) 

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_d] and keys[K_w] and self.rect.y > 0 and self.rect.x < WIDTH:
            self.rect.x +=self.speed * sqrt(2)
            self.rect.y -=self.speed * sqrt(2)
        elif keys[K_d] and keys[K_s] and self.rect.y < HEIGHT and self.rect.x < WIDTH:
            self.rect.x +=self.speed * sqrt(2)
            self.rect.y +=self.speed * sqrt(2)
        elif keys[K_a] and keys[K_w] and self.rect.y > 0 and self.rect.x > 0:
            self.rect.x -=self.speed * sqrt(2)
            self.rect.y -=self.speed * sqrt(2)
        elif keys[K_a] and keys[K_s] and self.rect.y < HEIGHT and self.rect.x > 0: 
            self.rect.x -=self.speed * sqrt(2)
            self.rect.y +=self.speed * sqrt(2)
        elif keys[K_d] and self.rect.x < WIDTH:
            self.rect.x +=self.speed
        elif keys[K_a] and self.rect.x > 0:
            self.rect.x -=self.speed
        elif keys[K_w] and self.rect.y > 0:
            self.rect.y -=self.speed
        elif keys[K_s] and self.rect.y < HEIGHT:
            self.rect.y +=self.speed

class Enemy(sprite.Sprite):
    def __init__(self, w, h , name_image, speed, x, y, player_x, player_y):
        super().__init__()
        self.image = transform.scale(image.load(name_image), (w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def attack(self, player_x, player_y):
        
        self.difference_x = self.rect.x - player_x
        self.difference_y = self.rect.y - player_y
        print(self.difference_x)
        if self.difference_y < 0: 
            self.rect.y += self.speed
        elif self.difference_y > 0: 
            self.rect.y -= self.speed
        if self.difference_x < 0: 
            self.rect.x += self.speed
        elif self.difference_x > 0: 
            self.rect.x -= self.speed
    def draw(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

class loot(GameSprite):
    def __init__(self, rr, rw):
        self.reward = rw
    def pick_up(self):
        pass
class room():
    def __init__(self,count_of_enemyes,main_door, fl=Rect(0,0,1200,800)):
        self.floor = fl
        self.coe = count_of_enemyes
        self.loot = loot
        self.md = main_door
    def generate(self):
        pass


