##### MAIN SCORE #######
CakeScore = 0
########################

Multiplier = 1.1

IMG_SIZE = 80

MARGIN = 10

M_TOP = 40

FIELD_HEIGHT = IMG_SIZE


from PIL import Image
img = Image.open("img/grandma.jpg")
img = img.resize((IMG_SIZE, IMG_SIZE))
img.save("img/grandma.jpg")

img = Image.open("img/cursor.jpg")
img = img.resize((IMG_SIZE, IMG_SIZE))
img.save("img/cursor.jpg")

img = Image.open("img/bake.jpg")
img = img.resize((IMG_SIZE, IMG_SIZE))
img.save("img/bake.jpg")

img = Image.open("img/bakehouse.png")
img = img.resize((IMG_SIZE, IMG_SIZE))
img.save("img/bakehouse.png")

img = Image.open("img/CakeMachine.jpg")
img = img.resize((IMG_SIZE, IMG_SIZE))
img.save("img/CakeMachine.jpg")

img = Image.open("img/Factory.jpg")
img = img.resize((IMG_SIZE, IMG_SIZE))
img.save("img/Factory.jpg")

img = Image.open("img/AlchLab.jpg")
img = img.resize((IMG_SIZE, IMG_SIZE))
img.save("img/AlchLab.jpg")

img = Image.open("img/TimeMachine.jpg")
img = img.resize((IMG_SIZE, IMG_SIZE))
img.save("img/TimeMachine.jpg")

img = Image.open("img/Portal.jpg")
img = img.resize((IMG_SIZE, IMG_SIZE))
img.save("img/Portal.jpg")

img = Image.open("img/AntimatterCondencer.jpg")
img = img.resize((IMG_SIZE, IMG_SIZE))
img.save("img/AntimatterCondencer.jpg")

img = Image.open("img/Prism.jpg")
img = img.resize((IMG_SIZE, IMG_SIZE))
img.save("img/Prism.jpg")


def cost(lvl):
    match lvl:
        case 1:
            return 15;
        case 2:
            return 100;
        case 3:
            return 500;
        case 4:
            return 3000;
        case 5:
            return 10000;
        case 6:
            return 40000;
        case 7:
            return 200000;
        case 8:
            return 1666666;
        case 9:
            return 123456789;
        case 10:
            return 3999999999;
        case 11:
            return 75000000000;

def growth_rate(lvl):
    match lvl:
        case 1:
            return 0.1;
        case 2:
            return 0.5;
        case 3:
            return 4;
        case 4:
            return 10;
        case 5:
            return 40;
        case 6:
            return 100;
        case 7:
            return 400;
        case 8:
            return 6666;
        case 9:
            return 98765;
        case 10:
            return 999999;
        case 11:
            return 10000000;



def accelerate(lvl):
    return cost(lvl)/20

def img(lvl):
    match lvl:
        case 1:
            return "img/cursor.jpg"
        case 2:
            return "img/grandma.jpg" 
        case 3:
            return "img/bake.jpg"
        case 4:
            return "img/bakehouse.png"
        case 5:
            return "img/CakeMachine.jpg"
        case 6:
            return "img/Factory.jpg"
        case 7:
            return "img/AlchLab.jpg"
        case 8:
            return "img/TimeMachine.jpg"
        case 9:
            return "img/Portal.jpg"
        case 10:
            return "img/AntimatterCondencer.jpg"   
        case 11:
            return "img/Prism.jpg"


def name(lvl):
    match lvl:
        case 1:
            return "Cursor"
        case 2:
            return "Grandma" 
        case 3:
            return "Bake"
        case 4:
            return "Bakehouse"
        case 5:
            return "CakeMachine"
        case 6:
            return "Factory"
        case 7:
            return "AlchLab"
        case 8:
            return "TimeMachine"
        case 9:
            return "Portal"
        case 10:
            return "AntiCondencer"   
        case 11:
            return "Prism"




def field_h(lvl, h = M_TOP):
    if lvl == 1:
        return h
    return field_h(lvl - 1, h + FIELD_HEIGHT + MARGIN)

def lvl_from_h(h, H = M_TOP):
    lvl = 0
    while H < h:
        lvl += 1
        H += FIELD_HEIGHT + MARGIN 
    return lvl
