"""Модуль содержит функции для чтения констант и передачи их в нужном виде"""
import src.Globals as G

def cost(lvl):
    """Возвращает стоимость фабрики соответствующей переданному значению"""
    return G.COST[lvl-1]

def growth_rate(lvl):
    """Возвращает стоимость фабрики соответствующей переданному значению"""
    return G.GROUTH_RATE[lvl-1]

def accelerate(lvl):
    """Возвращает изменени скорости при улучшении фабрики соответствующей переданному значению"""
    return cost(lvl)/20

def img(lvl):
    """Возвращает изображение(его имя в img) соответствующей фабрики соответствующей переданному значению""" 
    return "img/" + G.IMAGES[lvl-1]

def name(lvl):
    """Возвращает имя соответствующей фабрики соответствующей переданному значению""" 
    return G.NAMES[lvl-1]

def field_h(lvl, h = G.M_TOP):
    """Возвращет высоту для отрисовки фабрики соответствующей переданному значению"""
    if lvl == 1:
        return h
    return field_h(lvl - 1, h + G.FIELD_HEIGHT + G.MARGIN)

def lvl_from_h(h, H = G.M_TOP):
    """определяет уровень фабрики по переданной высоте"""
    lvl = 0
    while H < h:
        lvl += 1
        H += G.FIELD_HEIGHT + G.MARGIN 
    return lvl
