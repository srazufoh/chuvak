from classes import *
from perfomance import *
from map_generator import *



up_door = door('red',(WIDTH/2 - 50), 0, 100, 100)
left_door = door('red',0, (HEIGHT/2 - 50), 100, 100)
right_door = door('red',(WIDTH-100), (HEIGHT/2 - 50), 100, 100)
down_door = door('red',(WIDTH/2 - 50), 700, 100, 100)



room1 = room(10, 1)
player = Player(70,70,"hero.jpg", 2, 315, 0)

enemy = Enemy(70,70,"hero.jpg", 1, 205, 100, player.rect.x, player.rect.y)

run = True
while run:

    win.fill('darkgray')
    up_door.draw()
    down_door.draw()
    left_door.draw()
    right_door.draw()
    player.draw()
    player.update()
    enemy.draw()
    enemy.attack(player.rect.x, player.rect.y)




    for e in event.get():
        if e.type == QUIT:
            run =False
    display.update()
