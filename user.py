
from os import kill
from pickle import TRUE
import pygame,random

black = (255,255,255)
blanco = (0,0,0)

consolas = pygame.font.match_font('consolas')
times = pygame.font.match_font('times')
arial = pygame.font.match_font('arial')
courier = pygame.font.match_font('courier')

#Fondo de Pantalla
class Fondo(pygame.sprite.Sprite):
    def __init__(self,imagen):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("fondo.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

#Jugador 
class Nave (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("nave.png").convert_alpha()
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.center = (400,550)
        self.velocidad_x = 0
        self.velocidad_y = 0

    def update(self):
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y

        #Limita Marguen Izquierdo
        if self.rect.left <= 0:
            self.rect.left = 0
        #Limita Margen Derecho
        if self.rect.right >= 800:
            self.rect.right = 800
        #limita Margen Superior
        if self.rect.top <= 0:
            self.rect.top = 0
        #Limita Margen Inferior
        if self.rect.bottom >= 600:
            self.rect.bottom = 600
        #teclas de movimiento 
        key = pygame.key.get_pressed() #Aqui se obtiene la tecla presionada
        if key[pygame.K_a]:
            self.velocidad_x = -5 #Movimiento a la izquierda
        if key[pygame.K_d]:
            self.velocidad_x = 5 #Movimiento a la derecha
        if key[pygame.K_w]:
            self.velocidad_y = -5 #Movimiento hacia arriba
        if key[pygame.K_s]:
            self.velocidad_y = 5 #Movimiento hacia abajo
        if key[pygame.K_SPACE]:
            player.disparo()
        self.rect.y += self.velocidad_y
        self.rect.x += self.velocidad_x
        self.velocidad_x = 0
        self.velocidad_y = 0
    def disparo(self):
        bala = Disparos(self.rect.centerx,self.rect.top)
        balas.add(bala)

#Proyectiles
class Disparos(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("disparo.png").convert_alpha(),(10, 40))
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x

    def update(self):
        key = pygame.key.get_pressed()
        self.rect.y -= 3
        if self.rect.bottom < 0:
            self.kill()
        
#Enemigo
class Enemigo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.img_a = random.randrange(3)
        if self.img_a == 0:
            self.image = pygame.transform.scale(pygame.image.load("meteorito.png").convert_alpha(),(40, 40))
            self.radius = 20
        if self.img_a == 1:
            self.image = pygame.transform.scale(pygame.image.load("meteorito.png").convert_alpha(),(30, 30))
            self.radius = 15
        if self.img_a == 2:
            self.image = pygame.transform.scale(pygame.image.load("meteorito.png").convert_alpha(),(25, 25))
            self.radius = 12
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(800 - self.rect.width)
        self.rect.y = -self.rect.width
        self.velocidad_y = random.randrange(1, 7)
    def update(self):
        self.rect.y += self.velocidad_y
        if self.rect.top > 600:
            self.rect.x = random.randrange(800 - self.rect.width)
            self.rect.y = -self.rect.width
            self.velocidad_y = random.randrange(1, 7)


#Inicio de pygame
pygame.init()
#seleccionar tamaño de la ventana
x= 800
y= 600
screen = pygame.display.set_mode((x,y))
clock = pygame.time.Clock()
puntuacion = 0

def Texto(pantalla,fuente,texto,color,dimensiones,x,y):
    tipo_letra = pygame.font.Font(fuente,dimensiones)
    superficie = tipo_letra.render(texto,False,color)
    rectangulo = superficie.get_rect()
    rectangulo.center = (x,y)
    pantalla.blit(superficie,rectangulo)
    

sprites = pygame.sprite.Group()
enemigos = pygame.sprite.Group() 
balas = pygame.sprite.Group()


#Jugador añadido a la sprite "sprites"
player = Nave()
sprites.add(player)

#Enemigos añadidos a la sprite "enemigos"
meteor = Enemigo()
enemigos.add(meteor)

for i in range (10):
    meteor = Enemigo()
    enemigos.add(meteor)

#Titulo de la ventana e imagen 
pygame.display.set_caption('Bienvenidos a mi Juego')
delante = pygame.image.load('nave de.png')
pygame.display.set_icon(delante)

#Cargar imagen para fondo
fondo = pygame.image.load('fondo.png').convert()

#Jugador
nave = pygame.image.load('nave.png')

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            sys = exit()
    screen.blit(fondo,(0,0))
    sprites.draw(screen)
    enemigos.draw(screen)
    balas.draw(screen)
    sprites.update()
    enemigos.update()
    balas.update()
    Texto(screen,consolas,str(puntuacion).zfill(1),black,40,700,50)
    colision_n = pygame.sprite.spritecollide(player, enemigos, True)
    if colision_n:
        print("Colision de la nave")
        puntuacion -= 100
        run = False
        print("Tuviste una puntuacion de: ",puntuacion)
    colision_b = pygame.sprite.groupcollide(enemigos,balas,False,True)
    if colision_b:
        print ("Colision al meteorito")
        puntuacion += 5
    pygame.display.update()
    clock.tick(60)
    pygame.display.flip()
pygame.quit()