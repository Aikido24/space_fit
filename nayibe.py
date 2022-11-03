import pygame as pg
from sys import exit
#zona de variables
pg.init()
size=(800,600)
screen=pg.display.set_mode(size)
clock=pg.time.Clock()
#variables player
nave_player=pg.image.load("./imagenes/nave_player.png").convert_alpha()
rectangulo_player=nave_player.get_rect(midbottom=(80,600))
speed_playerx=0
#movimiento player
def move_player():
    global rectangulo_player
    global speed_playerx
    print (rectangulo_player.right)
    if rectangulo_player.left>690:
        speed_playerx=0
        rectangulo_player.left=690
    if rectangulo_player.right<120:
        speed_playerx=0
        rectangulo_player.right=120
    rectangulo_player.x+=speed_playerx
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
                speed_playerx=-3
            if event.key==pg.K_RIGHT:
                speed_playerx=3
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
    move_player()
    #zona de dibujo
    drawling()
    pg.display.update()
    clock.tick(60)