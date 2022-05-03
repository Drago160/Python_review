"""Модуль содержит класс Fabrick"""
import src.Toolfunc
import src.Globals as G
import math
import src.Objects as Obj
import pygame as pg


class Fabrick(pg.sprite.Sprite):
    """класс Фабрика"""

    def __init__(self, screen, lvl):
        """
        конструктор принимает экран для отрисовки и уровень фабрики
        которую создать надо
        (уровни идут сверху вниз на экране от кликера к нижнему
        """
        self.body = Obj.Field(screen, lvl)
        self.lvl = lvl
        self.rate = 1
        self._cost = src.Toolfunc.cost(self.lvl)
        self.power = src.Toolfunc.growth_rate(self.lvl)
        self.accelerate = src.Toolfunc.accelerate(self.lvl)
        self.cost *= G.Multiplier
        self._active = False
        self.body.set_power(self.power)

    def update(self):
        """Метод для добавления кликов каждую секунду"""
        G.cake_score += self.power

    @property
    def active(self):
        """метод делает Фабрику активной"""
        return self._active

    @active.setter
    def active(self, val):
        """метод меняет значения активная ли на val"""
        self._active = val
        self.body.active = val

    @property
    def cost(self):
        """Метод показывает текущую стоимость покупки/улучшения"""
        return self._cost

    @cost.setter
    def cost(self, value):
        """
        Метод меняет стоимость улучшения
        и вызывает смену данного параметра у body
        """
        self._cost = value
        self.body.set_upgrade_cost(value)

    def pre_activate(self):
        """Метод вызывает состояние подготовки к активации"""
        self.body.pre_activate()

    def upgrade(self):
        """Метод улучшает фабрику"""
        if self.cost <= G.cake_score:
            self.tick_button()
            G.cake_score -= self.cost
            self.cost *= G.Multiplier
            self.power += self.accelerate
            self.rate += 1
            self.body.set_rate(self.rate)
            self.body.set_power(self.power)
        else:
            self.cant_buy()

    def cant_buy(self):
        """Метод вызывает у body объявление о нехватке очков"""
        self.body.cant_buy()

    def tick_button(self):
        """Метод вызывает эффект нажатия на кнопку у body"""
        self.body.tick_button()

    def __bool__(self):
        """Метод показывает активна ли данная фабрика"""
        return self.active
