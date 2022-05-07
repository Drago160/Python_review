import src.Globals as G
import pygame as pg


class Label():
    """Класс надпись"""
    def __init__(self, val, font_size, x, y, color, bg):
        """
        Конструктор принимает строку которую надо записать,
        размер шрифта,
        координаты для отрисовки относительно поля на котором находится,
        цвет надписи в формате (r, g, b),
        тело на котором происзодит отрисовка
        """
        self.bg = bg
        self.x, self.y = x, y
        self.f = pg.font.Font(None, font_size)
        self.value = val
        self.color = color
        self.text = self.f.render(self.value, True, color)
        self.text.get_rect()

    def draw(self):
        """Метод рисует данную надпись"""
        self.bg.blit(self.text, (self.x, self.y))

    def rewrite(self, val):
        """Метод меняет содержание строки в Надписи"""
        self.text = self.f.render(val, True, self.color)


class Disappearing_Label(Label):
    """Класс исчезающая Надпись"""
    def __init__(self, val, font_size, x, y, color, disappearingRate, bg):
        """
        Конструктор принимает то же
        что у обычной Надписи(родителя) и скорость исчезновения
        """
        super().__init__(val, font_size, x, y, color, bg)
        self.disappearingRate = disappearingRate
        self.alpha = 0

    def draw(self):
        """Отрисовывает надпись с эффектом исчезновения"""
        if (self.alpha > 0):
            self.alpha -= self.disappearingRate
        self.text.set_alpha(self.alpha)
        super().draw()

    def update(self):
        """Запускает надпись"""
        self.alpha = 255
