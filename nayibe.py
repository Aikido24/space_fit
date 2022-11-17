import pygame as pg
from sys import exit
import random

#zona de variables
pg.init()
size=(800,600)
screen=pg.display.set_mode(size)
clock=pg.time.Clock()

#musica


#variables enemigos
imagen_enemigo1=pg.image.load("./imagenes/marciano 2.png").convert_alpha()
enemigo1_posicion=[]
nave_destrucion=[]
direcion_enemigo=[]
decenso_enemigo=[]
enemigo_posicion_top = []
#fondo
fondo=pg.image.load("./imagenes/FONDO/fondo1.png").convert()
posicion_fondo=(0,0)
fondo2=pg.image.load("./imagenes/FONDO/fondo2.png").convert_alpha()
posicion_fondo2=(0,0)
#fondo particulas
fondo_particulas=pg.image.load("./imagenes/particulas.png").convert_alpha()
posicion_particulas=fondo_particulas.get_rect(midtop=(410,0))
posicion_particulas2=fondo_particulas.get_rect(midbottom=(410,0))

#variables player
nave_player= []
nave_player.append(pg.image.load("./imagenes/NAVE/NAVE_1.png").convert_alpha())
nave_player.append(pg.image.load("./imagenes/NAVE/NAVE_2.png").convert_alpha())
nave_player.append(pg.image.load("./imagenes/NAVE/NAVE_3.png").convert_alpha())
nave_player.append(pg.image.load("./imagenes/NAVE/NAVE_4.png").convert_alpha())
rectangulo_player=nave_player[1].get_rect(midbottom=(80,600))
animacion_nave=0
speed_playerx=0
speed_playery=0
speed_nave=7
LEFT= False
RIGHT=False
UP=False
DOWN=False

#disparos player

disparos=[]
imagen_bala=pg.image.load("./imagenes/BALAS.png").convert_alpha()
posicion_bala=imagen_bala.get_rect(midbottom=(100,100))

#movimiento player

def move_player():
    global rectangulo_player
    global speed_playerx
    global speed_playery
    global LEFT , RIGHT , UP , DOWN

    if LEFT:
        speed_playerx=-7
    if RIGHT:
        speed_playerx=7
    if not(LEFT or RIGHT):
        speed_playerx=0

    if UP:
        speed_playery=-7
    if DOWN:
        speed_playery=7
    
    if not(UP or DOWN):
        speed_playery=0

    if rectangulo_player.left>=690:
        #speed_playerx=0
        rectangulo_player.left=688
    if rectangulo_player.right<=120:
        #speed_playerx=0
        rectangulo_player.right=122
    if rectangulo_player.top<=0:
        #speed_playery=0
        rectangulo_player.top=2
    if rectangulo_player.bottom>=600:
        #speed_playery=0
        rectangulo_player.bottom=592
    rectangulo_player.x+=speed_playerx
    rectangulo_player.y+=speed_playery
    

#funcion de eventos
generador_enemigos=pg.USEREVENT+1
pg.time.set_timer(generador_enemigos,2000)
disparos_tiempo=pg.USEREVENT+2
pg.time.set_timer(disparos_tiempo,500)
boton_disparo=False

def events():
    global speed_playerx
    global speed_playery
    global imagen_bala
    global disparos
    global rectangulo_player 
    global enemigo1_posicion,imagen_enemigo1
    global nave_destrucion
    global direcion_enemigo,decenso_enemigo,enemigo_posicion_top 
    global LEFT , RIGHT , UP , DOWN
    global boton_disparo

    for event in pg.event.get():
        if event.type==pg.QUIT:
            pg.quit()
            exit()
        #eventos de teclado
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_LEFT:
               
                LEFT=True
            if event.key==pg.K_RIGHT:
                
                RIGHT=True
            if event.key==pg.K_UP:
                
                UP=True
            if event.key==pg.K_DOWN:
                
                DOWN=True
            if event.key==pg.K_SPACE:
                boton_disparo=True

        if event.type==pg.KEYUP:
            
            if event.key==pg.K_LEFT:
                
                LEFT=False
            if event.key==pg.K_RIGHT:
                
                RIGHT=False
            if event.key==pg.K_UP:
                
                UP=False
            if event.key==pg.K_DOWN:
                
                DOWN=False
            if event.key==pg.K_SPACE:
                boton_disparo=False

        #creacion enemigos
        if event.type==generador_enemigos:
            direcion_enemigo.append(6)
            decenso_enemigo.append(0)
            enemigo_posicion_top.append(0)
            nave_destrucion.append(True)
            enemigo1_posicion.append(imagen_enemigo1.get_rect(midbottom=(80,0)))
        if event.type==disparos_tiempo:
            if boton_disparo:
                disparos.append(imagen_bala.get_rect(midbottom=rectangulo_player.midtop))

#movimiento fondo
def movimiento_fondo():
    global posicion_particulas
    global posicion_particulas2
    posicion_particulas.bottom+=5
    posicion_particulas2.bottom+=5
    if posicion_particulas.top>=600:
        posicion_particulas.bottom=0
    if posicion_particulas2.top>=600:
        posicion_particulas2.bottom=0

#movimiento enemigo
def movimiento_enemigo1():
    global enemigo1_posicion
    global imagen_enemigo1
    global direcion_enemigo
    global decenso_enemigo
    global enemigo_posicion_top
    for i in range (len(enemigo1_posicion)):

        if enemigo1_posicion[i].left>750:
            direcion_enemigo[i]=-6
            enemigo_posicion_top[i]+=20
        if enemigo1_posicion[i].right<50:
            direcion_enemigo[i]=6
            enemigo_posicion_top[i]+=20
        if enemigo1_posicion[i].top != enemigo_posicion_top[i]:
            enemigo1_posicion[i].top+=2
        #decenso_enemigo+=0.007
        #enemigo1_posicion.top+= int(decenso_enemigo)
        enemigo1_posicion[i].left+=direcion_enemigo[i]
        #print(enemigo1_posicion.top)

#funcion de dibujo
def disparos_draw():
    global disparos
    global imagen_bala
    global enemigo1_posicion
    global nave_destrucion
    if len(disparos)!=0:
        eliminar=False
        for i in range(len(disparos)):
            disparos[i].top-=5 
            screen.blit(imagen_bala,disparos[i])
        for i in range(len(disparos)):   
            for j in range(len(enemigo1_posicion)):
                if enemigo1_posicion[j].colliderect(disparos[i]):
                    nave_destrucion[j]=False
                    disparos.pop(i) 
                    eliminar=True
                    break
                
            if eliminar:
                eliminar=False
                break 
        for i in range(len(disparos)):        
            if disparos[i].bottom<-20:
                disparos.pop(i)
                break

def nave_draw():
    global nave_player
    global rectangulo_player
    global animacion_nave    
    screen.blit(nave_player[int(animacion_nave)],rectangulo_player)
    animacion_nave+=0.2
    if animacion_nave>= len(nave_player):
        animacion_nave = 0

def drawling():
    global fondo
    global posicion_fondo
    global fondo_particulas
    global posicion_particulas
    global posicion_particulas2
    global posicion_bala
    global imagen_bala
    global fondo2
    global posicion_fondo2
    screen.blit(fondo,posicion_fondo)
    screen.blit(fondo_particulas,posicion_particulas)
    screen.blit(fondo_particulas,posicion_particulas2)
    screen.blit(fondo2,posicion_fondo2)
    nave_draw()
    disparos_draw()

def dibujar_enemigo():
    global nave_destrucion,imagen_enemigo1,enemigo1_posicion
    for i in range (len(enemigo1_posicion)):
        if nave_destrucion[i]:
            screen.blit(imagen_enemigo1,enemigo1_posicion[i])
       
#fondo
            ################################
#musica
numero_cancion=0
canciones=["Out-Of-My-System","Ghost-Mary-On-A-Cross-_Official-Audio_"]

def play_music ():
    global numero_cancion,canciones
    if not (pg.mixer.music.get_busy()):
        pg.mixer.music.load(f"./musica/{canciones[numero_cancion]}.mp3")
        pg.mixer.music.play()
        numero_cancion+=1
        if numero_cancion >= len(canciones):
            numero_cancion=0



#bucle principal
while True:
    events()
    screen.fill("White")
    move_player()
    #zona de dibujo
    movimiento_fondo()
    drawling()
    dibujar_enemigo()
    movimiento_enemigo1()
    pg.display.update()
    print(speed_playerx)
    clock.tick(60)
    events()
    for i in nave_destrucion:
        if not i :
            nave_destrucion.pop(i)
            enemigo1_posicion.pop(i) 
            direcion_enemigo.pop(i)
            decenso_enemigo.pop(i)
            enemigo_posicion_top.pop(i)
            break
    play_music()