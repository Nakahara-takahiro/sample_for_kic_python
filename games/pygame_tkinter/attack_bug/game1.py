# -*- conding:utf-8 -*-
import pygame
from pygame.locals import *
import sys
import random
import math

(WIDTH, HEIGHT) = (640, 400)
(CENTERX, CENTERY) = (WIDTH/2, HEIGHT/2)
SCREEN = pygame.Rect(0, 0, WIDTH, HEIGHT)
FPS = 60
BENEFICIAL = 2
BUGTYPE = 4
SUICIDE = 10
LIFETIME = 60
BUGLENMIN = 450
BUGLENMAX = 650
BUGSPEEDMIN = 100
BUGSPEEDMAX = 200
BUGRADCENTER = 1.0
SPEEDMODUSPEED = 100
RADMODURADIUS = 1
SPEEDMODURAD = 12
RADMODURAD = 12
BUGDROPTIME = 1

class Bug():
    def __init__(self):
        self.kill = False
        self.tim = 0
        self.type = random.randrange(BUGTYPE)
        self.len = random.uniform(BUGLENMIN, BUGLENMAX)
        self.speed = random.uniform(BUGSPEEDMIN, BUGSPEEDMAX)
        self.rad = random.uniform(0, math.pi * 2.0)
        self.dir = 0
        self.x = - math.cos(self.rad) * self.len + CENTERX
        self.y = - math.sin(self.rad) + self.len + CENTERY
        self.rad += random.uniform(-BUGRADCENTER, BUGRADCENTER)
        self.speedModuRad = random.uniform(0, SPEEDMODURAD)
        self.speedModuSpeed = random.uniform(0, SPEEDMODUSPEED)
        self.radModuRad = random.uniform(0, RADMODURAD)
        self.radModuRadius = random.uniform(0, RADMODURADIUS)
    def update(self, tim):
        self.tim += tim
        tm = self.tim
        if tm >= SUICIDE:
            self.kill = True
        rd = self.rad + (self.radModuRadius * math.sin(tm * self.radModuRad))
        sp = self.speed * ((100 -self.speedModuSpeed * math.sin(tm * self.speedModuRad))/100)
        self.x += math.cos(rd) * sp * tim
        self.y += math.sin(rd) * sp * tim
        self.dir = -90 - rd * 180 / math.pi

#ゲームの処理
pygame.init()
screen = pygame.display.set_mode(SCREEN.size)
pygame.display.set_caption('Mosquite')
clock = pygame.time.Clock()
sysfont = pygame.font.SysFont(None, 40)
deltaTime = elapsedTime = lifeTime = hit = miss = 0
attack = playing = False
(px, py) = (0, 0)
bug = []
seHit = pygame.mixer.Sound('hit.mp3')
seMiss = pygame.mixer.Sound('miss.mp3')
swatterSpr = pygame.image.load('smasher.png').convert_alpha()
swatterRect = swatterSpr.get_rect()
bugSpr = [pygame.image.load('bug01.png').convert_alpha()]
bugSpr.append(pygame.image.load('bug02.png').convert_alpha())
bugSpr.append(pygame.image.load('bug03.png').convert_alpha())
bugSpr.append(pygame.image.load('bug04.png').convert_alpha())
while(True):
    screen.fill('gray')
    if playing:
        elapsedTime += deltaTime
        if(elapsedTime >= BUGDROPTIME):
            elapsedTime -= BUGDROPTIME
            bug.append(Bug())
        lifeTime -= deltaTime
        if lifeTime <= 0:
            lifetime = 0
            playing = False
            bug = []
    else:
        screen.blit(sysfont.render('Push R-Click to Start', False, (0,255,0)), (190,200))
    screen.blit(sysfont.render('TIME:'+str(int(lifeTime)), False, 'blue'), (20, 0))
    screen.blit(sysfont.render('HIT:'+str(int(hit)), False, ' green'), (260,0))
    screen.blit(sysfont.render('MISS:'+str(int(miss)), False, 'red'), (460, 0))
    clock.tick(FPS)
    deltaTime = clock.get_time() / 1000.0
    for b in reversed(bug):
        if b.kill:
            bug.remove(b)
            bug.append(Bug())
        else:
            b.update(deltaTime)
            rotSpr = pygame.transform.rotate(bugSpr[b.type], b.dir)
            rotRect = rotSpr.get_rect()
            rotRect.center = (b.x, b.y)
            screen.blit(rotSpr, rotRect)
            if attack & pygame.Rect.colliderect(swatterRect, rotRect):
                attack = False
                if b.type < BENEFICIAL:
                    hit += 1
                    seHit.play()
                else:
                    miss += 1
                    seMiss.play()
                bug.remove(b)
                bug.append(Bug())
    attack = False
    swatterRect.center = (px, py)
    screen.blit(swatterSpr, swatterRect)
    pygame.display.update()

    for event in pygame.event.get():
        if(event.type == KEYDOWN and event.key == K_ESCAPE) or event.type == QUIT:
            pygame.quit(); sys.exit()
        elif event.type == MOUSEMOTION:
            px, py = event.pos
        if event.type == MOUSEBUTTONDOWN:
            if playing and event.button == 1:
                attack = True
            elif playing == False and event.button == 3:
                playing = True
                lifeTime = LIFETIME
                elapsedTime = hit = miss = 0
                bug.append(Bug())