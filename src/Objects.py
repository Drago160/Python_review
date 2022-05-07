"""Реализация моделек"""
import src.Toolfunc
import src.Globals as G
from src.Labels import Label, Disappearing_Label
import math
from src.Tools import output
import pygame as pg
import time


class FabrickName(Label):
    """Класс Имя Фабрики"""
    def __init__(self, name, bg):
        """Конструктор принимает имя фабрики и bg для отрисовки"""
        super().__init__(
                name,
                G.NAME_SIZE,
                G.IMG_SIZE+G.NAME_MARGIN_LEFT,
                G.NAME_MARGIN_TOP,
                G.NAME_COLOR, bg
                )


class FabrickUpcost(Label):
    """Класс стоимости апгрейда Фабрики"""
    def __init__(self, bg):
        """Конструктор принимает bg для отрисовки стоимости"""
        super().__init__(
                "",
                G.UPCOST_FONT_SIZE,
                G.IMG_SIZE + G.UPCOST_MARGIN_LEFT,
                G.FIELD_HEIGHT - G.UPCOST_MARGIN_BOT,
                G.UPCOST_COLOR,
                bg
                )


class FabrickBuycost(Label):
    """Класс стоимость покупки данной Фабрики"""
    def __init__(self, lvl, bg):
        """
        Конструктор принимает уровень соответствующей фабрики
        и bg для отрисовки
        """
        super().__init__(
                G.BUYCOST_LABEL + output(src.Toolfunc.cost(lvl)),
                G.BUYCOST_FONT_SIZE,
                G.IMG_SIZE + G.BUYCOST_MARGIN_LEFT,
                G.FIELD_HEIGHT - G.BUYCOST_MARGIN_BOT,
                G.BUYCOST_COLOR,
                bg
                )


class FabrickRate(Label):
    """Класс Рейтинг для данной Фабрики"""
    def __init__(self, bg):
        """Конструктор принимает bg для отрисовки"""
        super().__init__(
                str(1),
                G.RATE_FONT_SIZE,
                G.FIELD_WIDTH - G.RATE_MARGIN_RIGHT,
                int(G.FIELD_HEIGHT/2 - G.RATE_STANDART_MARGIN),
                G.RATE_COLOR,
                bg
                )


class FabrickPower(Label):
    """Класс скорости прироста для данной Фабрики"""
    def __init__(self, bg):
        """Конструктор принимает bg для отрисовки"""
        super().__init__(
                G.POWER_STR,
                G.POWER_FONT_SIZE,
                G.IMG_SIZE + G.POWER_MARGIN_LEFT,
                int(G.FIELD_HEIGHT/2 - G.POWER_MARGIN_TOP),
                G.POWER_COLOR,
                bg
                )


class FabrickWarning(Disappearing_Label):
    """
    Класс Warning надпись данной фабрики
    (предупреждение о нехватке очков для покупки/апгрейда
    """
    def __init__(self, bg):
        """Конструктор принимает bg для отрисовки исчезающей надписи"""
        super().__init__(
                G.DIS_STR,
                G.DIS_FONT_SIZE,
                int(G.FIELD_WIDTH / 2),
                int(G.FIELD_HEIGHT / 2 - G.STANDART_DIS_PUDDING),
                G.DIS_COLOR,
                G.DIS_RATE,
                bg
                )


class Field():
    """Класс Поле - тут рисуется моделька фабрики"""
    def __init__(self, screen, lvl):
        """Конструктор принимает уровень соответствующей фабрики и
        сопостовляет ей Полу по уровню"""
        self.screen = screen
        self.x = G.MAIN_FIELD_MARGIN_LEFT
        self.y = src.Toolfunc.field_h(lvl)
        self.img = pg.image.load(src.Toolfunc.img(lvl))
        self.str_name = src.Toolfunc.name(lvl)

        self.bg = pg.Surface((G.FIELD_WIDTH, G.IMG_SIZE))
        self.bg.fill(G.BG_COLOR)
        self.bg_bg = pg.Surface((self.bg.get_width() - G.IMG_SIZE, G.IMG_SIZE))
        self.bg_bg.fill(G.BG_COLOR)

        self.name = FabrickName(self.str_name, self.bg)
        self.up_cost = FabrickUpcost(self.bg)
        self.buy_cost = FabrickBuycost(lvl, self.bg)
        self.rate = FabrickRate(self.bg)
        self.power = FabrickPower(self.bg)
        self.dis_label = FabrickWarning(self.bg)

        self.bg.set_alpha(0)
        self.img.set_alpha(0)
        self._active = False

    @property
    def active(self):
        """Метод делает Поле активным"""
        return self._active

    def pre_activate(self):
        """готовит поле к активации"""
        self.bg.set_alpha(G.BG_PRE_ACTIVE_ALPHA)
        self.img.set_alpha(G.BG_IMG_ACTIVE_ALPHA)

    @active.setter
    def active(self, value):
        """Метод активирует Поле(если применяет True)"""
        self._active = value
        if self._active:
            self.bg.set_alpha(255)
            self.bg_bg.set_alpha(255)
            self.img.set_alpha(255)

    def set_power(self, value):
        """Метод меняет значения строки прироста на принимаемое значение"""
        self.power.rewrite(output(value) + G.POWER_STR)

    def set_upgrade_cost(self, value):
        """
        Метод меняе значение строки стоимости улучшения
        на принимаемое значение
        """
        self.up_cost.rewrite(G.UPCOST_STR + output(value))

    def cant_buy(self):
        """Вызывает исчезающую надпись о недостаточном количестве очков"""
        self.dis_label.update()

    def set_rate(self, val):
        """Меняет значение надписи уровня на принимаемое значение"""
        self.rate.rewrite(output(val))

    def tick_button(self):
        """Метод вызывает эффект нажатия на кнопку"""
        self.bg.set_alpha(G.TICK_ALPHA)
        self.bg.fill(G.BG_COLOR)
        self.draw()
        time.sleep(G.CLICK_BUTTON_TIMERANGE)
        self.bg.set_alpha(255)
        self.bg.fill(G.BG_COLOR)

    def draw(self):
        """Метод отрисовывает данное поле"""
        self.screen.blit(self.bg, (self.x, self.y))
        self.bg.blit(self.bg_bg, (G.IMG_SIZE+G.BG_MARGIN_LEFT, 0)) 
        self.bg.blit(self.img, (0, 0))
        self.name.draw()
        self.power.draw()
        if self.active:
            self.up_cost.draw()
            self.rate.draw()
        else:
            self.buy_cost.draw()
        self.dis_label.draw()
