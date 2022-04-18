import pygame as pg
import random
import src.Fabricks as F
import src.Toolfunc as C
import src.Globals as G
from src.Objects import Label
import sys
import math
import src.event as E
import time
from src.Tools import output
import src.Objects


WIDTH = 1900 
HEIGHT = 1080 
FPS = 30

# Обрабатывая изображение на BG
image_path = "img/bg.jpg"
bg = pg.image.load("img/bg.jpg")


# Основные параметры 
pg.font.init()
pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("CupCakeClicker")




# Инициализируем кликер основной 
Clicker = F.Fabrick(screen, 1)
Clicker.active = True
Clicker.body.active = True

##### TIMER #######
clock = pg.time.Clock()
###################


#список фабрик
Fabricks = [F.Fabrick(screen, i) for i in range(1, 12)] 
Fabricks[0] = Clicker
Fabricks[1].pre_activate()



Score = Label("", 280, int(screen.get_width()/2), int(screen.get_height()/2) - 20, (255, 15, 192), screen)


def Upgrade(Fabrics, N):
    """Принимает список фабрик и уровень фабрики для улучшения
    Вызывает улучшение соответствующей фабрики если это возможно"""
    if Fabricks[N-1]:
        Fabricks[N-1].upgrade()
    else:
        if C.cost(N) <= G.CakeScore and Fabricks[N-2]:
            G.CakeScore -= C.cost(N)
            Fabricks[N-1].active = True 
            if (N < 11):
                if not Fabricks[N]:
                    Fabricks[N].pre_activate()
        elif Fabricks[N-2]:
            Fabricks[N-1].Cant_buy()

    


T = time.time()

run = True
while run:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pg.event.get():
        # check for closing window
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.MOUSEBUTTONDOWN:
            if pg.mouse.get_pos()[0] <= 400:
                N = C.lvl_from_h(pg.mouse.get_pos()[1])
                if N > 0:
                    Upgrade(Fabricks, N)
        #события клавиатуры
        if event.type == pg.KEYDOWN:
            if pg.key.get_pressed()[pg.K_z]:
                G.CakeScore *= 100
            elif pg.key.get_pressed()[pg.K_SPACE]:
                Clicker.update()
            elif pg.key.get_pressed()[pg.K_KP1]:
                Clicker.upgrade()
            elif pg.key.get_pressed()[pg.K_KP2]:
                Upgrade(Fabricks, 2)
            elif pg.key.get_pressed()[pg.K_KP3]:
                Upgrade(Fabricks, 3)
            elif pg.key.get_pressed()[pg.K_KP4]:
                Upgrade(Fabricks, 4) 
            elif pg.key.get_pressed()[pg.K_KP5]:
                Upgrade(Fabricks, 5) 
            elif pg.key.get_pressed()[pg.K_KP6]:
                Upgrade(Fabricks, 6) 
            elif pg.key.get_pressed()[pg.K_KP7]:
                Upgrade(Fabricks, 7) 
            elif pg.key.get_pressed()[pg.K_KP8]:
                Upgrade(Fabricks, 8) 
            elif pg.key.get_pressed()[pg.K_KP9]:
                Upgrade(Fabricks, 9) 
            elif pg.key.get_pressed()[pg.K_0]:
                Upgrade(Fabricks, 10)
            elif pg.key.get_pressed()[pg.K_MINUS]:
                Upgrade(Fabricks, 11)




    #Обновляем фабрики каждую секнду
    if time.time() - T >= 1:
        T = time.time()
        E.update(Fabricks)

    #отрисовка BG
    screen.blit(bg, (0, 0))
   
    for fab in Fabricks:
        fab.body.draw()


    #пишем сколько же там очков

    #text = f.render(output(C.CakeScore), True, (255, 15, 192))
    Score.rewrite(output(G.CakeScore))
    Score.draw()
    #screen.blit(text, (int(1.05*(WIDTH/2)), int(0.9*(HEIGHT/2))))
    pg.display.update()
    pg.display.flip()

pg.quit()
