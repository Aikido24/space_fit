import pygame as pg
from sys import exit
#zona de variables
pg.init()
size=(800,600)
screen=pg.display.set_mode(size)
clock=pg.time.Clock()
#variables player
nave_player=pg.image.load("./imagenes/nave_player.png").convert_alpha()
rectangulo_player=nave_player.get_rect(midbottom=(80,300))
speed_playerx=0
#funcion de eventos
def events():
    global speed_playerx
    for event in pg.event.get():
        if event.type==pg.QUIT:
            pg.quit()
            exit()
        #eventos de teclado
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_LEFT:
                speed_playerx=3
            if event.key==pg.K_RIGHT:
                speed_playerx=-3
        if event.type==pg.KEYUP:
            if event.key==pg.K_LEFT:
                speed_playerx=0
            if event.key==pg.K_RIGHT:
                speed_playerx=0
            
#funcion de dibujo
def drawling():
    global nave_player
    global rectangulo_player
    screen.blit(nave_player,rectangulo_player)
#bucle principal
while True:
    events()
    screen.fill("White")
    #zona de dibujo
    drawling()
    pg.display.update()
    clock.tick(60)