# -*- conding: utf-8 -*-
import
import sys
import

SCREEN =pygame.Rect(0, 0, 400, 640)
FPS = 60
CROW_      = [500, 800]
CROW_Y_RANGE = [50, 600]
CROW_            = [-100, 100]
CROW_TURN_MAX = 10
DIFFICULT_MAX = 3
SPARROW_  = 120
SPARROW_START_  = 240
SPARROW_UP_END_Y = 0
SPARROW_DOWN_END_Y = 640
CLIMB_          = 300
GRAVITY = 850

def SparrowStartPos():
    global sparrowY, climbSpeed
    sparrowY = SPARROW_START_Y
    climbSpeed = 0

def CrowResetXY(i):
    crow     = CROW_X_POS[i]
    crow     =       .uniform(CROW_Y_RANGE[0], CROW_Y_RANGE[1])

def CrowStartPos():
    for i in range(0, len(CROW_X_POS)):
        CrowResetXY(i)

#ゲーム処理

screen = pygame.display.set_mode(SCREEN.size)
pygame.display.set_caption("Sparrow")
clock = pygame.time.Clock()
sysfont = pygame.font.SysFont(None, 40)
elapsedTime = 0
difficult = 0
deltaTime = 0.0
playing = False
seFlap = pygame.mixer.Sound('flap.mp3')
seHunted = pygame.mixer.Sound('hunted.mp3')




crowTurn = [0, 0]


crowSpr = pygame.image.load('crow.png').convert_alpha()
crowRect = crowSpr.get_rect()
sparrowSpr = [pygame.image.load('sparrowd.png').convert_alpha()]
sparrowSpr.append(pygame.image.load('sparrowu.png').convert_alpha())
sparrowRect = sparrowSpr[0].get_rect()
sparrowRect = sparrowSpr[0].get_rect()
sparrowRect.center = (SPARROW_X, sparrowY)

bldgSpr = pygame.image.load('building.png').convert_alpha()
bldgRect = bldgSpr.get_rect()

while (True):
    
    pygame.draw.rect(screen, 'gray92', pygame.Rect(0, 600, 480, 40))

    for i in range(2):#移動するビルを複数描画する   
        bldgRect.center = (200 - ((elapsedTime + i * 4) % 8 - 4) * 80, 540)
        screen.blit(bldgSpr, bldgRect)
    
    if playing:
        difficult = min(difficult + 0.2 * deltaTime, DIFFICULT_MAX)
        for i in range(0, len(CROW_X_POS)):
            crowX[i] -= 100.0 * deltaTime
            if difficult >= DIFFICULT_MAX:
                if crowTurn[i] > 0:
                    crowTurn[i] -= deltaTime
                    if crowTurn[i] < 0:
                        crowSpeed[i] *= -1
            if crowX[i] < -50:
                crowX[i] += 600
                                 .uniform(CROW_Y_RANGE[0], CROW_Y_RANGE[1])
                                     .uniform(CROW_SPEED_RANGE[0], CROW_SPEED_RANGE[1]) * difficult
                crowTurn[i] = random.uniform(2, CROW_TURN_MAX)
            
            crowY[i] += crowSpeed[i] * deltaTime
            if crowY[i] <= 0 or crowY[i] >= 640:
                crowSpeed[i] *= -1
            crowRect.center = (crowX[i], crowY[i])
            screen.blit(crowSpr, crowRect)

            if pygame.Rect.colliderect(sparrowRect, crowRect):
                SparrowStartPos()
                seHunted.play()
                playing = False

        elapsedTime += deltaTime
        
        climbSpeed += GRAVITY / FPS
        if sparrowY <= SPARROW_UP_END_Y or sparrowY >= SPARROW_DOWN_END_Y:
            playing = False
    else : #ゲームオーバーなら
        
        screen.blit(sysfont.render('Push Enter to Start', False, (0, 255, 0)), (80, 200))
    
    clock.tick(FPS)
    deltaTime = clock.get_time() / 1000.0
    screen.blit(sysfont.render('TIME:' + str(int(elapsedTime)), False, (0, 0, 0)), (160, 0))

    sparrowRect.center = (SPARROW_X, sparrowY)
    anmBody = 0 if climbSpeed >= 0 else 1
    screen.blit(sparrowSpr[anmBody], sparrowRect)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if                             and playing:
                climbSpeed = - CLIMB_SPEED_MAX
                seFlap.play()
            elif event.key == pygame.K_RETURN and playing == False:
                elapsedTime = 0
                difficult = 0
                CrowStartPos()
                playing = True
            elif event.key == pygame.K_ESCAPE:
                pygame.quit(); sys.exit()
        elif 
            
 