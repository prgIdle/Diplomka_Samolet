import pygame, Buttons, Pobeda, nachalo_menu
from pygame.locals import *
from time import sleep
from random import randint
import sys

pygame.init()

screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
FPS = 60

#Игра___________________________________________________________
def game1():
    class Samolet:
        def __init__(self, color, px, py, direct, keyList):
            objects.append(self)
            self.type = 'Samolet'

            self.color = color
            self.rect = pygame.Rect(px, py, 32, 32)
            self.direct = direct
            self.samoletSpeed = 4

            self.shotTimer = 0
            self.shotDelay = 30
            self.bulletSpeed = 5
            self.bulletDamage = 1

            self.keyLEFT = keyList[0]
            self.keyRIGHT = keyList[1]
            self.keyUP = keyList[2]
            self.keyDOWN = keyList[3]
            self.keySHOT = keyList[4]

        def update(self):
            if keys[self.keyLEFT]:
                self.rect.x -= self.samoletSpeed
            elif keys[self.keyRIGHT]:
                self.rect.x += self.samoletSpeed
            elif keys[self.keyUP]:
                self.rect.y -= self.samoletSpeed
            elif keys[self.keyDOWN]:
                self.rect.y += self.samoletSpeed

            if keys[self.keySHOT] and self.shotTimer == 0:
                dx = self.direct * self.bulletSpeed
                Bullet(self, self.rect.centerx, self.rect.centery, dx, self.bulletDamage)
                self.shotTimer = self.shotDelay

            if self.shotTimer > 0: self.shotTimer -= 1
            
        def draw(self):
            pygame.draw.rect(screen, self.color, self.rect)

            x = self.rect.centerx + self.direct * 30
            y = self.rect.centery
            pygame.draw.line(screen, 'white', self.rect.center, (x, y), 4)


    class Vrag:
        vragi=0
        def __init__(self, color, px, py, direct):
            objects.append(self)
            self.type = 'Vrag'

            self.color = color
            self.rect = pygame.Rect(px, py, 32, 32)
            self.direct = direct
            self.vragSpeed = 1
            self.hp=1
            self.__class__.vragi+=1
            print(self.__class__.vragi)

        def update(self):
            self.rect.x -= self.vragSpeed
        
        def draw(self):
            pygame.draw.rect(screen, self.color, self.rect)

        def damage(self, value):
            self.hp -= value
            if self.hp <= 0:
                objects.remove(self)
                self.__class__.vragi-=1
            if self.__class__.vragi==0:
                Pobeda.Button_Example()
    class Bullet:
        def __init__(self, parent, px, py, dx, damage):
            bullets.append(self)
            self.parent = parent
            self.px, self.py = px, py
            self.dx = dx
            self.damage = damage

        def update(self):
            self.px += self.dx

            if self.px < 0 or self.px > 1920 or self.py < 0 or self.py > 1080:
                bullets.remove(self)
            else:
                for obj in objects:
                    if obj != self.parent and obj.rect.collidepoint(self.px, self.py):
                        obj.damage(self.damage)
                        bullets.remove(self)
                        break

        def draw(self):
            pygame.draw.circle(screen, 'yellow', (self.px, self.py), 2)
    bullets = [] 
    objects = []
    Samolet('blue', 100, 275, 1, (pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s, pygame.K_SPACE))
    Vrag('red', randint(900, 1920), 275, -1)
    Vrag('red', randint(900, 1920), 308, -1)
    Vrag('red', randint(900, 1920), 350, -1)
    Vrag('red', randint(900, 1920), 295, -1)
    Vrag('red', randint(900, 1920), 480, -1)

    class Background(pygame.sprite.Sprite):
        def __init__(self, image_file, location):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load(image_file)
            self.rect = self.image.get_rect()
            self.rect.left, self.rect.top = location

    BackGround = Background('background_image_1.jpg', [0,0])

    play = True
    while play:
        screen.fill([255, 255, 255])
        screen.blit(BackGround.image, BackGround.rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False

        keys = pygame.key.get_pressed()
    
        for bullet in bullets: bullet.update()
        for obj in objects: obj.update()

        for bullet in bullets: bullet.draw()
        for obj in objects: obj.draw()
    
        pygame.display.update()
        clock.tick(60)
    
    pygame.quit()
#Игра_____________________________________________________________________
nachalo_menu.Button_Example()


