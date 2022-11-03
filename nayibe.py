import pygame as pg
from sys import exit
#zona de variables
pg.init()
size=(800,600)
screen=pg.display.set_mode(size)
clock=pg.time.Clock()
#musica
cancion1=pg.mixer.Sound("./musica/Out-Of-My-System.mp3")

#fondo
fondo=pg.image.load("./imagenes/fondo.png").convert()
posicion_fondo=(0,0)
#variables player
nave_player=pg.image.load("./imagenes/nave_player.png").convert_alpha()
rectangulo_player=nave_player.get_rect(midbottom=(80,600))
speed_playerx=0
speed_playery=0
#movimiento player
def move_player():
    global rectangulo_player
    global speed_playerx
    global speed_playery
    if rectangulo_player.left>690:
        speed_playerx=0
        rectangulo_player.left=690
    if rectangulo_player.right<120:
        speed_playerx=0
        rectangulo_player.right=120
    
    if rectangulo_player.top<0:
        speed_playery=0
        rectangulo_player.top=0
    if rectangulo_player.bottom>600:
        speed_playery=0
        rectangulo_player.bottom=600
    rectangulo_player.x+=speed_playerx
    rectangulo_player.y+=speed_playery
#funcion de eventos
def events():
    global speed_playerx
    global speed_playery
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
            if event.key==pg.K_UP:
                speed_playery=-3
            if event.key==pg.K_DOWN:
                speed_playery=3
        if event.type==pg.KEYUP:
            if event.key==pg.K_LEFT:
                speed_playerx=0
            if event.key==pg.K_RIGHT:
                speed_playerx=0
            if event.key==pg.K_UP:
                speed_playery=0
            if event.key==pg.K_DOWN:
                speed_playery=0
            
#funcion de dibujo
def drawling():
    global nave_player
    global rectangulo_player
    global fondo
    global posicion_fondo
    screen.blit(fondo,posicion_fondo)
    screen.blit(nave_player,rectangulo_player)
cancion1.play()
#bucle principal
while True:
    events()
    screen.fill("White")
    move_player()
    #zona de dibujo
    drawling()
    pg.display.update()
    clock.tick(60)