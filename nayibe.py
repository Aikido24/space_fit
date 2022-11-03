import pygame as pg
from sys import exit
#zona de variables
pg.init()
size=(800,600)
screen=pg.display.set_mode(size)
clock=pg.time.Clock()
#funcion de eventos
def events():
    for event in pg.event.get():
        if event.type==pg.QUIT:
            pg.quit()
            exit()

#bucle principal
while True:
    events()
    screen.fill("White")

    pg.display.update()
    clock.tick(60)