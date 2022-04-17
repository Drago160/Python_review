import pygame as pg
import Cupcakes as C
import math
from Tools import output
import time

class Label():
        def __init__(self, val, font_size, x, y, color, bg):
            self.bg = bg
            self.x, self.y = x, y
            self.f = pg.font.Font(None, font_size)
            self.value = val
            self.color = color
            self.text = self.f.render(self.value, True, color)
            self.text.get_rect()

        def draw(self):
            self.bg.blit(self.text, (self.x, self.y))           

        def rewrite(self, val):
            self.text = self.f.render(val, True, self.color)


class Disappearing_Label(Label):
    def __init__(self, val, font_size, x, y, color, bg):
        super().__init__(val, font_size, x, y, color, bg)
        self.alpha = 0 
    def draw(self):
        self.alpha -= 3
        self.text.set_alpha(self.alpha)
        super().draw()
    def update(self):
        self.alpha = 255

class Field():
    def __init__(self, screen, x, y, name, img, power, lvl):
    
        self.screen = screen 
        self.x = x
        self.y = y
        self.img = pg.image.load(img)
        self.name = name


        self.bg = pg.Surface((400, C.IMG_SIZE))
        self.bg.fill((0, 0, 139))
        self.bg_bg = pg.Surface((self.bg.get_width() - C.IMG_SIZE, C.IMG_SIZE))
        self.bg_bg.fill((0, 0, 139))


        pg.font.init()


        ##############################
        self.name = Label(name, 35, C.IMG_SIZE+5, 5, (255, 255, 255), self.bg)  
        self.up_cost = Label("", 25, C.IMG_SIZE + 5, self.bg.get_height() - 20, (255, 255, 255), self.bg)

        self.buy_cost = Label("Cost: " + output(C.cost(lvl)), 25, C.IMG_SIZE + 5, self.bg.get_height() - 20, (255, 255, 255), self.bg)
        self.rate = Label(str(1), 50, self.bg.get_width() - 70, int(self.bg.get_height()/2 - 15), (255, 255, 255), self.bg)
        self.power = Label(str(power) + " PC / sec", 25, C.IMG_SIZE + 5, int(self.bg.get_height()/2 - 5), (255, 255, 255), self.bg)
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
        return self._active 

    def pre_activate(self):
        self.bg.set_alpha(65)
        self.bg_bg.set_alpha(65)
        self.img.set_alpha(85)


    @active.setter
    def active(self, value):
        self.bg.set_alpha(255)
        self.bg_bg.set_alpha(255)
        self.img.set_alpha(255)
        self._active = value



    def set_power(self, value):
        self.power.rewrite(output(value) + " PC/sec")

        
    def set_upgrade_cost(self, value):
        self.up_cost.rewrite("Upgrade: " + output(value))

    def Cant_buy(self):
        self.dis_label.update()

    def set_rate(self, val):
        self.rate.rewrite(output(val))
        
    def Tick_button(self):
        self.bg.set_alpha(100) 
        self.bg.fill((0, 0, 139))
        self.draw()
        time.sleep(0.1)
        self.bg.set_alpha(255) 
        self.bg.fill((0, 0, 139))

    def draw(self):
        self.screen.blit(self.bg, (self.x, self.y)) 
        self.bg.blit(self.bg_bg, (C.IMG_SIZE+5, 0))
        self.bg.blit(self.img, (0, 0))
        self.name.draw() 
        self.power.draw()
        if self.active:
            self.up_cost.draw()
            self.rate.draw()
        else:
            self.buy_cost.draw()
        self.dis_label.draw()
