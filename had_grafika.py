import pyglet
import random
from pathlib import Path

# velikost pole
pole = 64
SIRKA = pole * 10
VYSKA = pole * 10
window = pyglet.window.Window(width=SIRKA, height=VYSKA)
# later create a function to set a width and height with default parameters 10, 10 
# def set_dimensions(width=10, height=10): 
#   SIRKA = pole*width 
#   VYSKA = pole*height
# v inputu bude možnost, jak velkou plochu si hráč chce zvolit: small/medium/large => to budou klíče k parametrům 10/15/20, které dosadím funkci jako parametr k vytvoření pole
# bude potřeba počítat s resize celé hry i souřadnic - nastavit je jako proměnnou (to bude lepší řešit pomocí OOP)




# počáteční souřadnice
souradnice_had = [(0, 0), (1, 0)]
souradnice_ovoce = [(2, 3)]

TILES_DIRECTORY = Path('snake-tiles')

snake_tiles = {}
# key = název, value = obrázek
for path in TILES_DIRECTORY.glob('*.png'):
    snake_tiles[path.stem] = pyglet.image.load(path)


had = pyglet.sprite.Sprite(snake_tiles['tail-head'])


ovoce = pyglet.sprite.Sprite(snake_tiles['apple'])

"""def tik(t):
    # kdyby se měl ten had pohybovat sám
    had.x = had.x + 1*pole

pyglet.clock.schedule_interval(tik, 1)"""

hra_bezi = True

def pohyb(souradnice_had, smer):
    x = souradnice_had[-1][0]
    y = souradnice_had[-1][1]
    if smer == pyglet.window.key.UP:
        y += 1
    elif smer == pyglet.window.key.DOWN:
        y -= 1
    elif smer == pyglet.window.key.LEFT:
        x -= 1
    elif smer == pyglet.window.key.RIGHT:
        x += 1
    if (x < 0 or x > 9) or (y < 0 or y > 9) or ((x, y) in souradnice_had):
        raise ValueError()
    souradnice_had.append((x, y))
    if ((x, y) not in souradnice_ovoce):
        del souradnice_had[0]
    if (x, y) in souradnice_ovoce:
        souradnice_ovoce.remove((x, y))
        pridej_jablko(souradnice_had, souradnice_ovoce)


def stisk_klavesy(klavesa, mod):
    global hra_bezi
    if hra_bezi:
        try:
            pohyb(souradnice_had, klavesa)

        except ValueError:
            print("Game Over!")
            hra_bezi = False



def pridej_jablko(souradnice_had, souradnice_ovoce):
    # přidá nové ovoce na náhodnou pozici mimo hada
    x = random.randrange(10)
    y = random.randrange(10)
    while (x, y) in souradnice_had:
       x = random.randrange(10)
       y = random.randrange(10) 
    souradnice_ovoce.append((x, y))


def vykresli():
    window.clear()
    # pohyb hada
    for x,y in souradnice_had:
        had.x = x*pole
        had.y = y*pole
        had.draw()
    
    # umístění ovoce
    for x,y in souradnice_ovoce:
        ovoce.x = x*pole
        ovoce.y = y*pole
        ovoce.draw()
    
    # konec hry
    if hra_bezi == False:
        obrazek = snake_tiles['game_over_transparent']
        konec = pyglet.sprite.Sprite(obrazek, x = 2.5*pole, y = 4*pole)
        konec.draw()

window.push_handlers(
    on_key_press=stisk_klavesy,
    on_draw=vykresli,
    )

pyglet.app.run()


# had může jezdit sám
# ještě bych mohla doplnit počítadlo ocasu
# v momentě, kdy na počítadle je 99, hra končí - "You beat the game!"
# nakonec vylepšit grafiku hada