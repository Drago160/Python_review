"""Реализация моделек"""
import src.Toolfunc as C
import src.Globals as G
import math
from src.Tools import output
import pygame as pg
import time

class Label():
    """Класс надпись""" 
    def __init__(self, val, font_size, x, y, color, bg):
        """Конструктор принимает строку которую надо записать, размер шрифта, координаты для отрисовки относительно поля на котором находится, цвет надписи в формате (r, g, b), тело на котором происзодит отрисовка"""
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
    def __init__(self, val, font_size, x, y, color, bg):
        """Конструктор принимает то же что у обычной Надписи(родителя)"""
        super().__init__(val, font_size, x, y, color, bg)
        self.alpha = 0 

    def draw(self):
        """Отрисовывает надпись с эффектом исчезновения"""
        if (self.alpha > 0):
            self.alpha -= 3
        self.text.set_alpha(self.alpha)
        super().draw()

    def update(self):
        """Запускает надпись"""
        self.alpha = 255

class Field():
    """Класс Поле"""
    def __init__(self, screen, x, y, name, img, power, lvl):
        """Конструктор принимает экран для отрисовки, координаты, имя соответствующего Поля, картинку, начальную скорость прироста, уровень соответствующей фабрики"""
        self.screen = screen 
        self.x = x
        self.y = y
        self.img = pg.image.load(img)
        self.name = name

        self.bg = pg.Surface((400, G.IMG_SIZE))
        self.bg.fill((0, 0, 139))
        self.bg_bg = pg.Surface((self.bg.get_width() - G.IMG_SIZE, G.IMG_SIZE))
        self.bg_bg.fill((0, 0, 139))

        pg.font.init()

        ##############################
        self.name = Label(name, 35, G.IMG_SIZE+5, 5, (255, 255, 255), self.bg)  
        self.up_cost = Label("", 25, G.IMG_SIZE + 5, self.bg.get_height() - 20, (255, 255, 255), self.bg)
        self.buy_cost = Label("Cost: " + output(C.cost(lvl)), 25, G.IMG_SIZE + 5, self.bg.get_height() - 20, (255, 255, 255), self.bg)
        self.rate = Label(str(1), 50, self.bg.get_width() - 70, int(self.bg.get_height()/2 - 15), (255, 255, 255), self.bg)
        self.power = Label(str(power) + " PC / sec", 25, G.IMG_SIZE + 5, int(self.bg.get_height()/2 - 5), (255, 255, 255), self.bg)
        self.dis_label = Disappearing_Label("Not enough", 32, int(self.bg.get_width()/2),int(self.bg.get_height()/2) - 10, (255, 0, 0), self.bg) 
        ###############################

        #######################
        self.bg.set_alpha(0)
        self.bg_bg.set_alpha(0)
        self.img.set_alpha(0)
        ######################## 
        self._active = False

    @property
    def active(self):
        """Метод делает Поле активным"""
        return self._active 

    def pre_activate(self):
        """готовит поле к активации"""
        self.bg.set_alpha(65)
        self.bg_bg.set_alpha(65)
        self.img.set_alpha(85)


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
        self.power.rewrite(output(value) + " PC/sec")
        
    def set_upgrade_cost(self, value):
        """Метод меняе значение строки стоимости улучшения на принимаемое значение"""
        self.up_cost.rewrite("Upgrade: " + output(value))

    def Cant_buy(self):
        """Вызывает исчезающую надпись о недостаточном количестве очков"""
        self.dis_label.update()

    def set_rate(self, val):
        """Меняет значение надписи уровня на принимаемое значение"""
        self.rate.rewrite(output(val))
        
    def Tick_button(self):
        """Метод вызывает эффект нажатия на кнопку"""
        self.bg.set_alpha(100) 
        self.bg.fill((0, 0, 139))
        self.draw()
        time.sleep(0.05)
        self.bg.set_alpha(255) 
        self.bg.fill((0, 0, 139))

    def draw(self):
        """Метод отрисовывает данное поле"""
        self.screen.blit(self.bg, (self.x, self.y)) 
        self.bg.blit(self.bg_bg, (G.IMG_SIZE+5, 0))
        self.bg.blit(self.img, (0, 0))
        self.name.draw() 
        self.power.draw()
        if self.active:
            self.up_cost.draw()
            self.rate.draw()
        else:
            self.buy_cost.draw()
        self.dis_label.draw()
