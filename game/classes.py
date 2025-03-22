import pygame
import random 

pygame.init()

win = pygame.display.set_mode((1200, 800))

class door():
    def __init__(self, x, y, height, width):
        self.x = x
        self.y = y
        self.h = height
        self.w = width
        self.Rect = pygame.Rect(self.x,self.y,self.h,self.w)
    def location(self):
        pygame.draw.rect(win, 'brown', self.rect)

up_door = door(100, 100, 100, 100)
left_door = door(100, 10, 100, 10)
right_door = door(100, 100, 100, 100)
down_door = door(10, 100, 10, 100)



class loot():
    def __init__(self, rr, rw):
        self.reward = rw
        self.rare = rr
    def pick_up(self):
        pass
class room():
    def __init__(self,count_of_enemyes,main_door, fl=pygame.Rect(0,0,1200,800)):
        self.floor = fl
        self.coe = count_of_enemyes
        self.loot = loot
        self.md = main_door
    def generate(self):
        up_door.location()
        down_door.location()
        left_door.location()
        right_door.location()

room1 = room(10, 1)

run = True
while run:

    win.fill('darkgray')






    
    pygame.display.update(60)

