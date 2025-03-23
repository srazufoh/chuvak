from pygame import*
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import*
from PyQt5.QtGui import *
from game import Game

class LauncherWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Лаунчер для игры на PyGame")
        self.setGeometry(100, 100, 600, 400)
        self.ui_components()
        self.show()
        self.modes = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

    def ui_components(self):
        self.setStyleSheet('.QWidget {background-image: url(grass.jpg);}')
        self.button = QPushButton("Запустить игру", self)
        self.button.setGeometry(250, 150, 100, 60)
        self.button.setFont(QFont("Arial", 15))
        self.button.setStyleSheet("background-color: rgb(68, 107, 145);")
        self.button.clicked.connect(self.handler)

        self.button_rules = QPushButton("Правила", self)
        self.button_rules.setGeometry(250, 190, 100, 60)
        self.button_rules.setFont(QFont("Arial", 15))
        self.button_rules.setStyleSheet("background-color: rgb(68, 107, 145);")
        self.button_rules.clicked.connect(self.rules)

        self.button_setting = QPushButton("Настройки", self)
        self.button_setting.setGeometry(250, 190, 100, 60)
        self.button_setting.setFont(QFont("Arial", 15))
        self.button_setting.setStyleSheet("background-color: rgb(68, 107, 145);")
        self.button_setting.clicked.connect(self.settings)

        self.picture = QLabel()
        pixmapimage = QPixmap('wasd.png')
        label_width, label_height = 100, 100
        scaled_pixmap = pixmapimage.scaled(label_width, label_height, Qt.KeepAspectRatio)
        self.picture.setPixmap(scaled_pixmap)
        self.picture.setVisible(True)

        v_line = QVBoxLayout()
        v2_line = QHBoxLayout()
        main_line = QHBoxLayout()

        v_line.addWidget(self.button)
        v_line.addWidget(self.button_rules)
        v_line.addWidget(self.button_setting)
        v2_line.addWidget(self.picture, alignment = (Qt.AlignTop | Qt.AlignRight))

        main_line.addLayout(v_line, 75)
        main_line.addLayout(v2_line, 25)

        central_widget = QWidget()
        central_widget.setLayout(main_line)
        self.setCentralWidget(central_widget)
        
    def handler(self):
        self.hide()
        #QApplication.exit(0)
        my_game = Game()
        my_game.run()

    def results(self):
        self.show()
        self.setStyleSheet('.QWidget {background-image: url(grass.jpg);}')
        count = QLabel('Ваш результат:' + str(count))

        self.button_again = QPushButton("Начать заново", self)
        self.button_again.setGeometry(250, 150, 100, 60)
        self.button_again.setFont(QFont("Arial", 15))
        self.button_again.setStyleSheet("background-color: rgb(68, 107, 145);")
        self.button_again.clicked.connect(self.ui_components)

        v_line = QVBoxLayout()

        v_line.addWidget(self.count, alignment= Qt.AlignCenter)
        v_line.addWidget(self.button_again, alignment= Qt.AlignLeft)
        v_line.addStretch(1)
        v_line.setSpacing(30)

        finish_widget = QWidget()
        finish_widget.setLayout(v_line)
        self.setCentralWidget(finish_widget)

    def rules(self):
        self.label = QLabel('Вы появляетесь в случайно сгенерированной комнате с противниками.', self)
        self.label.setFont(QFont('Arial', 13))
        self.label.setStyleSheet("color: rgb(255,255,255);")
        self.label2 = QLabel('В комнате находится монета, которую вам нужно забрать быстрее, чем вас схватит', self)
        self.label2.setFont(QFont('Arial', 13))
        self.label2.setStyleSheet("color: rgb(255,255,255);")
        self.label3 = QLabel('противник. Забрав монету, вы снова перемещаетесь в рандомную комнату.', self)
        self.label3.setFont(QFont('Arial', 13))
        self.label3.setStyleSheet("color: rgb(255,255,255);")
        self.label4 = QLabel('Это аркадная игра, поэтому вы можете устанавливать рекорды по количеству собранных монет.', self)
        self.label4.setFont(QFont('Arial', 13))
        self.label4.setStyleSheet("color: rgb(255,255,255);")

        self.button_back = QPushButton('Назад', self)
        self.button_back.clicked.connect(self.ui_components)
        self.button_back.setGeometry(250, 190, 100, 60)
        self.button_back.setStyleSheet("background-color: rgb(68, 107, 145);")
        self.button_back.setFont(QFont("Arial", 11))

        v_line = QVBoxLayout()

        v_line.addWidget(self.label, alignment= Qt.AlignCenter)
        v_line.addWidget(self.label2,alignment= Qt.AlignCenter)
        v_line.addWidget(self.label3, alignment= Qt.AlignCenter)
        v_line.addWidget(self.label4, alignment= Qt.AlignCenter)
        v_line.addWidget(self.button_back, alignment= Qt.AlignLeft)
        v_line.addStretch(1)
        v_line.setSpacing(30)

        rules_widget = QWidget()
        rules_widget.setLayout(v_line)
        self.setCentralWidget(rules_widget)
    
    def settings(self):
        self.setStyleSheet("background-color: white;")
        self.hide()
        chosen_mode, ok = QInputDialog.getInt(
            self, "Выбор сложности", "Выберите количество соперников:", 1, 1, len(self.modes), 1
        )
        if (chosen_mode and ok) or not(chosen_mode and ok):
            self.show()
            self.setStyleSheet('.QWidget {background-image: url(grass.jpg);}')

def main():
    application = QApplication([])
    window = LauncherWindow()
    application.exec_()

main()