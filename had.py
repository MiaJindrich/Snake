# initial code for building a Snake game
# to play the game, run had_grafika.py file

import random

def nakresli_mapu(seznam, souradnice_ovoce, souradnice_tajemne_ovoce, rozmery_pole):
    line = "." * 10
    tabulka = {}
    for i in range(10):
        tabulka[i] = line
        # vytvoří tabulku 10x10 teček
    for sloupec, radek in souradnice_ovoce:
        nahradit_radek(tabulka, sloupec, radek, "o")
        # zakreslí do tabulky ovoce
    for sloupec, radek in souradnice_tajemne_ovoce:
        nahradit_radek(tabulka, sloupec, radek, "?")
    for sloupec, radek in seznam:
        nahradit_radek(tabulka, sloupec, radek, "x")
        # zakreslí do tabulky hada
    return tabulka

def nahradit_radek(tabulka, sloupec, radek, znak):
    tabulka[radek] = tabulka[radek][:sloupec] + znak + tabulka[radek][sloupec+1:]

def print_map(tabulka):
    # vytiskne tabulku s ovocem a hadem
    for i in tabulka.values():
        print(i)

def pohyb(souradnice,smer, souradnice_ovoce, pocet_kol, souradnice_tajemne_ovoce, rozmery_pole): 
    # po zadání směru se k seznamu souřadnic hada přidá nová souřadnice
    x = souradnice[-1][0]
    y = souradnice[-1][1]
    smer = smer.lower()
    if smer == "v":
        x += 1
    elif smer == "z":
        x -= 1
    elif smer == "j":
        y += 1
    elif smer == "s":
        y -= 1
    else:                                       # tahle podmínka nefunguje!!!
        print("chybné zadání")
        x = x
        y = y 
    if (x < 0 or x > 9) or (y < 0 or y > 9) or ((x, y) in souradnice):
        # pokud se dostane ven z mapy nebo zvolí pole, na kterém už je, ukončí se hra
        raise ValueError("Game Over!")
    if ((x, y) not in souradnice_ovoce) and ((x, y) not in souradnice_tajemne_ovoce):
        # pokud nesežere ovoce, délka hada je stejná (odečte se první tupl ze seznamu = ocas hada)
        del souradnice[0]
        # smaže poslední souřadnici hada
    elif (x, y) in souradnice_ovoce:
        souradnice_ovoce.remove((x, y))
        # smaže souřadnici ovoce, na které stojí
    elif (x, y) in souradnice_tajemne_ovoce:
        souradnice_tajemne_ovoce.remove((x, y))
    souradnice.append((x, y))
    # přidá novou souřadnici hada do seznamu
    if len(souradnice_ovoce) == 0:
        # pokud zmizí všechna ovoce, přidá se nové ovoce
        pridej_jablko(souradnice, souradnice_ovoce, rozmery_pole)
    if pocet_kol%30 == 0:
        # pokud nastane 30. kolo, vytvoří se tajné ovoce
        pridej_jablko(souradnice, souradnice_tajemne_ovoce, rozmery_pole)
        print(souradnice_tajemne_ovoce)


def pridej_jablko(seznam, ovoce, rozmery_pole):
    # přidá nové ovoce na náhodnou pozici mimo hada
    x = random.randrange(10)
    y = random.randrange(10)
    while (x, y) in seznam:
       x = random.randrange(10)
       y = random.randrange(10) 
    ovoce.append((x, y))


hra_bezi = True
seznam = [(0, 0), (1, 0), (2, 0)]
souradnice_ovoce = [(2, 3)]
souradnice_tajemne_ovoce = []
pocet_kol = 1


mapa = nakresli_mapu(seznam, souradnice_ovoce, souradnice_tajemne_ovoce, (10, 10))
print_map(mapa)
while hra_bezi:
    pocet_kol += 1
    try:
        pohyb(seznam, input("Zvol směr('s'/'j'/'v'/'z'): "), souradnice_ovoce, pocet_kol, souradnice_tajemne_ovoce, (10, 10))
    except ValueError:
        print("Game Over!")
        hra_bezi = False
    mapa = nakresli_mapu(seznam, souradnice_ovoce, souradnice_tajemne_ovoce, (10, 10))
    print_map(mapa)