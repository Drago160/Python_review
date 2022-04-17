import Cupcakes as C  
import pygame as pg
import Objects as Obj
import math


class Fabrick(pg.sprite.Sprite):

    def __init__(self, screen, lvl): 
        self.body = Obj.Field(screen, 0, C.field_h(lvl), C.name(lvl), C.img(lvl),C.growth_rate(lvl), lvl)
        self.lvl = lvl 
        self.rate = 1
        self._cost = C.cost(self.lvl)
        self.power = C.growth_rate(self.lvl)
        self.accelerate = C.accelerate(self.lvl)
        self.cost *= C.Multiplier
        self._active = False

        
    def update(self):
        C.CakeScore += self.power


    @property
    def active(self):
        return self._active


    @active.setter
    def active(self, val):
        self._active = val 
        self.body.active = val


    @property
    def cost(self):
        return self._cost


    @cost.setter
    def cost(self, value):
        self._cost = value
        self.body.set_upgrade_cost(value)
    
    def pre_activate(self):
        self.body.pre_activate()

    def upgrade(self):
        if self.cost <= C.CakeScore:
            self.Tick_button()
            C.CakeScore -= self.cost
            self.cost *= C.Multiplier
            self.power += self.accelerate
            self.rate += 1;
            self.body.set_rate(self.rate)
            self.body.set_power(self.power);    
        else:
            self.Cant_buy()
    
    def Cant_buy(self):
        self.body.Cant_buy()

    def Tick_button(self):
        self.body.Tick_button()

    def __bool__(self):
        return self.active 
