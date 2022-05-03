"""Модуль содержит класс для основной игры"""
import src.Toolfunc as Toolfunc
import src.Fabricks as Fabricks
import src.Globals as G
from src.Objects import Label
import math
import src.Objects
from src.Tools import output
import pygame as pg
import random
import sys
import time


class Game:
    """
    Класс Игра - тут все события обработка их, цикл и тп
    """

    def __init__(self):
        """
        Конструктор не принимает параметров и инициализирует игру
        """
        self.width = G.WIDTH
        self.height = G.HEIGHT
        self.fps = G.FPS
        self.set_bg()
        pg.init()
        self.screen = pg.display.set_mode((self.width, self.height))
        self.set_clicker()
        self.set_clock()
        self.set_fabricks()
        self.set_labels()

    def set_bg(self):
        """
        Метод создает задний фон(картинку привязывает)
        """
        self.bg = pg.image.load("img/bg.jpg")

    def set_clicker(self):
        """
        Метод создает главный кликер
        """
        self.clicker = Fabricks.Fabrick(self.screen, 1)
        self.clicker.active = True

    def set_clock(self):
        """
        Метод создает таймер
        """
        self.clock = pg.time.Clock()

    def set_fabricks(self):
        """
        Метод создает список фабрик
        и инициализирует первую кликером
        """
        self.fabricks = [Fabricks.Fabrick(self.screen, i) for i in range(1, 12)]
        self.fabricks[0] = self.clicker
        self.fabricks[1].pre_activate()

    def set_labels(self):
        """
        Метод создает все выводящиеся на осн экран надписи
        """
        self.Score = Label(
                "",
                G.MAIN_LABEL_FONT_SIZE,
                int(G.WIDTH/2), int(G.HEIGHT/2) - G.MAIN_LABEL_MARGIN_TOP,
                G.MAIN_LABEL_COLOR,
                self.screen
                )

    def control_event(self, event):
        """
        Метод обрабатывает события
        """
        # check for closing window
        if event.type == pg.QUIT:
            self.run = False
        if event.type == pg.MOUSEBUTTONDOWN:
            if pg.mouse.get_pos()[0] <= G.FIELD_WIDTH:
                N = Toolfunc.lvl_from_h(pg.mouse.get_pos()[1])
                if N > 0:
                    self.upgrade(N)
        if event.type == pg.KEYDOWN:
            self.ControlTickKeyboard()

    def ControlTickKeyboard(self):
        """
        Метод обрабатывает улучшение фабрик на кнопки клавиатуры
        """
        if pg.key.get_pressed()[pg.K_z]:
            G.cake_score *= 100
        elif pg.key.get_pressed()[pg.K_SPACE]:
            self.clicker.update()
        elif pg.key.get_pressed()[pg.K_KP1]:
            self.clicker.upgrade()
        elif pg.key.get_pressed()[pg.K_KP2]:
            self.upgrade(2)
        elif pg.key.get_pressed()[pg.K_KP3]:
            self.upgrade(3)
        elif pg.key.get_pressed()[pg.K_KP4]:
            self.upgrade(4)
        elif pg.key.get_pressed()[pg.K_KP5]:
            self.upgrade(5)
        elif pg.key.get_pressed()[pg.K_KP6]:
            self.upgrade(6)
        elif pg.key.get_pressed()[pg.K_KP7]:
            self.upgrade(7)
        elif pg.key.get_pressed()[pg.K_KP8]:
            self.upgrade(8)
        elif pg.key.get_pressed()[pg.K_KP9]:
            self.upgrade(9)
        elif pg.key.get_pressed()[pg.K_0]:
            self.upgrade(10)
        elif pg.key.get_pressed()[pg.K_MINUS]:
            self.upgrade(11)

    def update(self):
        """Вызывает обновления состояния всех переданных фабрик"""
        for fabr in self.fabricks:
            if fabr:
                fabr.update()

    def upgrade(self, N):
        """
        Принимает уровень фабрики для улучшения
        Вызывает улучшение соответствующей фабрики если это возможно
        """
        if self.fabricks[N-1]:
            self.fabricks[N-1].upgrade()
        else:
            if Toolfunc.cost(N) <= G.cake_score and self.fabricks[N-2]:
                G.cake_score -= Toolfunc.cost(N)
                self.fabricks[N-1].active = True
                if (N < G.NUM_OF_FABRICKS):
                    if not self.fabricks[N]:
                        self.fabricks[N].pre_activate()
            elif self.fabricks[N-2]:
                self.fabricks[N-1].cant_buy()

    def start(self):
        T = time.time()

        self.run = True
        while self.run:
           # Держим цикл на правильной скорости
            self.clock.tick(self.fps)
            # Ввод процесса (события)
            for event in pg.event.get():
                self.control_event(event)

            # Обновляем фабрики каждую секнду
            if time.time() - T >= 1:
                T = time.time()
                self.update()

            # отрисовка BG
            self.screen.blit(self.bg, (0, 0))

            for fab in self.fabricks:
                fab.body.draw()

            # рисуем все
            self.Score.rewrite(output(G.cake_score))
            self.Score.draw()
            pg.display.update()
            pg.display.flip()

        pg.quit()
