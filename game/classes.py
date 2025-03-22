from pygame import *
import random 
import sys

HEIGHT = 800
WIDTH = 1200

win = display.set_mode((WIDTH, HEIGHT))
game = True




class GameSprite(sprite.Sprite):
    def __init__(self, w, h,image, speed, x, y):
        super().__init__()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y)) 

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_d] and self.rect.x < WIDTH:
            self.rect.x +=self.speed
        if keys[K_a] and self.rect.x > 0:
            self.rect.x -=self.speed
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -=self.speed
        if keys[K_s] and self.rect.y < HEIGHT:
            self.rect.y +=self.speed

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



up_door = door('red',(WIDTH/2 - 50), 0, 100, 100)
left_door = door('red',0, (HEIGHT/2 - 50), 100, 100)
right_door = door('red',(WIDTH-100), (HEIGHT/2 - 50), 100, 100)
down_door = door('red',(WIDTH/2 - 50), 700, 100, 100)



class loot():
    def __init__(self, rr, rw):
        self.reward = rw
        self.rare = rr
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

room1 = room(10, 1)
player = Player(70,70,"hero.jpg", 10, 315, 0)

run = True
while run:

    win.fill('darkgray')

    up_door.draw()
    down_door.draw()
    left_door.draw()
    right_door.draw()



    for e in event.get():
        if e.type == QUIT:
            run =False
    display.update()

