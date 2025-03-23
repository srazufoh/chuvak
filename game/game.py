import pygame
#from interface import LauncherWindow

class Game:
    def __init__(self):
        # Инициализирует игру и создает объекты экрана
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("  ")
        bg_color = (230, 230, 230)
        self.screen.fill(bg_color)

    def run(self):
        # Запуск основного цикла игры
        game = True
        finish = False
        while game:
            # Отслеживание событий клавиатуры и мыши
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False

            '''if finish != True:



            application = QApplication([])
            window = LauncherWindow()
            application.exec_()
            window.results()'''
            # Отоброжение  последнего прорисованного экрана
            pygame.display.flip()