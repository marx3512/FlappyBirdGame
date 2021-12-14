import pygame, random, os, math

from pygame.event import post

try:
    pygame.init()
except:
    print("Não deu certo")

def MoveAssetsAndRect():
    global posPipeX, posPipeY, posDoorX, posDoorY, posTargetX, posTargetY, TargetYRandom, TargetYCalculation
    if stop == False:
        posPipeX -= 1
        posDoorX -= 1

        playerRect.update(0, posPlayerY, 51, 50)
        tubeDownRect.update(posPipeX, posPipeY, 94, 570)
        tubeUpRect.update(posPipeX, posPipeY - 710, 94, 570)
        doorRect.update(posDoorX, posPipeY - 132, 96, 138)

        if posPipeX < -80:
            posPipeX = 510
            posDoorX = 510
            posPipeY = random.randint(200, 600)

def ChangeMenu():
    mx, my = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed() == (1, 0, 0):
        if 85 <= mx and mx <= 210 and 400 <= my and my <= 520:
            return "Start"
        elif 160 <= mx and mx <= 285 and 545 <= my and my <= 670:
            return "Exit"
        elif 255 <= mx and mx <= 388 and 400 <= my and my <= 525:
            return "Tutorial"
        elif 17 <= mx and mx <= 100 and 610 <= my and my <= 680:
            return "ReturnMenu"

    elif pygame.mouse.get_pressed() == (0, 0, 0,):
        return False

def CheckInputMouse():
    global posTargetX, posDoorX
    mx, my = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed() == (1,0,0):
        if targetRect.collidepoint(mx, my):
            posTargetX = -100
            posDoorX = -100

def CheckCollisions():
    if pygame.Rect.colliderect(playerRect,tubeDownRect):
        return "Acertai tuboDown"
    elif pygame.Rect.colliderect(playerRect,tubeUpRect):
        return "Acertei tuboUp"
    elif pygame.Rect.colliderect(playerRect,doorRect):
        return "Acertei door"
    else:
        return "Acertei nada"

def CheckStyleTargetAndMove(cond):
    global posTargetX, posTargetY, TargetYCalculation, TargetYRandom, TimerResTarget, target, targetRect
    targetRect.update(posTargetX, TargetYCalculation, 50, 60)

    if posPipeX <= -80:
        posTargetX = 490
        TargetYRandom = random.randint(100, 600)
        TargetYCalculation = (posTargetY - TargetYRandom)*(-1)
    
    if cond == 0:
        posTargetX -= 1
    if cond == 1 or cond == 3:
        if cond == 1:
            posTargetX -= 1
        TimerResTarget -= 0.2
        if TimerResTarget <= 0:
            TargetYRandom = random.randint(100, 600)
            TargetYCalculation = (posTargetY - TargetYRandom)*(-1)
            targetRect.update(posTargetX, TargetYCalculation, 50, 60)
            TimerResTarget = 12
    if cond == 2 or cond == 3:
        posTargetX -=1
        target = pygame.transform.scale(target, (30, 30))
        TargetYCalculation = (posTargetY - TargetYRandom)*(-1)
        screen.blit(target, (posTargetX + 20, TargetYCalculation + 50))
        targetRect.update(posTargetX + 20, TargetYCalculation + 50, 30, 30)
    while pygame.Rect.colliderect(targetRect, doorRect):
        TargetYRandom = random.randint(100, 600)
        TargetYCalculation = (posTargetY - TargetYRandom)*(-1)
        targetRect.update(posTargetX, TargetYCalculation, 50, 60)

def CheckScore(score):
    global condStyleTarget
    if score >= 0 and score <= 200:
        condStyleTarget = 0
    elif score >= 201 and score <= 400:
        condStyleTarget = 1
    elif score >= 401 and score <= 600:
        condStyleTarget = 2
    elif score >= 601 and score <= 800:
        condStyleTarget = 3 

def CalculationAnglePistol( ):
    mx, my = pygame.mouse.get_pos()
    relationX, relationY = mx - 28, my - posPlayerY
    angle = (180/math.pi) * -math.atan2(relationY, relationX)

    return int(angle)

def CreateAssets(posBirdY, cond):
    screen.fill((255, 255, 255))
    screen.blit(player, (0, posBirdY))
    screen.blit(pygame.transform.rotate(pistol,CalculationAnglePistol()), (28,posBirdY + 13))
    screen.blit(tubeDown, (posPipeX, posPipeY))
    screen.blit(tubeUp, (posPipeX, posPipeY - 700))
    screen.blit(door, (posDoorX, posPipeY - 132))
    if cond != 2 and cond != 3:
        screen.blit(target, (posTargetX, (posTargetY - TargetYRandom)*(-1)))
    screen.blit(scoreScreen, (posTableScoreX, posTableScoreY))

def CreateText(msg, color, tam, x, y):
    font = pygame.font.SysFont(None, tam)
    texto1 = font.render(msg, True, color)
    screen.blit(texto1, [x, y])

def managerScoreScreen(cond):
    global posScoreX, posScoreY, posTableScoreX, posTableScoreY
    if cond != "Acertei nada":
        posScoreX, posScoreY = 200, 260
        posTableScoreX, posTableScoreY = 140, 230
        mx, my = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed() == (1, 0, 0):
            if 160 <= mx and mx <= 240 and 300 <= my and my <= 370:
                return "Restart"
            elif 260 <= mx and mx <= 330 and 300 <= my and my <= 370:
                return "Sair"

def ResetGame():
    global posPlayerY, posPipeX, posPipeY, posDoorX, posDoorY, posTargetX, posTargetY, TargetYRandom, TargetYCalculation, score
    global gravity, playerMoviment, death, createPipe, stop, exit, posScoreX, posScoreY, posTableScoreX, posTableScoreY
    score = 0
    posPlayerY = 250
    gravity = 0.10
    playerMoviment = 0
    death = False
    posPipeX, posPipeY = 570, 250
    posDoorX, posDoorY = 570, 215
    posTargetX, posTargetY = 550, 30
    posScoreX, posScoreY = 0, 0
    posTableScoreX, posTableScoreY = -100, -300
    TargetYRandom = 0
    TargetYCalculation = 0
    createPipe = False
    stop = False
    exit = True

os.chdir(os.path.dirname(__file__))

#files
menuImg = pygame.image.load(os.path.join('images', 'Menu_screen.jpg'))
TutorialImg = pygame.image.load(os.path.join('images', 'TutorialImage.png'))
player = pygame.image.load(os.path.join('images', 'Player(ed).png'))
playerRect = player.get_rect()
pistol = pygame.image.load(os.path.join('images', 'Pistol(ed).png'))
target = pygame.image.load(os.path.join('images', 'Target(ed).png'))
targetRect = target.get_rect()
tubeDown = pygame.image.load(os.path.join('images', 'Tube(down)(ed).png'))
tubeDownRect = tubeDown.get_rect()
tubeUp = pygame.image.load(os.path.join('images', 'Tube(up)(ed).png'))
tubeUpRect = tubeUp.get_rect()
door = pygame.image.load(os.path.join('images', 'Door(ed).png'))
doorRect = door.get_rect()
scoreScreen = pygame.image.load(os.path.join('images', 'scoreScreen(ed).png'))

# variable
score = 0
posPlayerY = 250
gravity = 0.10
playerMoviment = 0
death = False
posPipeX, posPipeY = 570, 250
posDoorX, posDoorY = 570, 215
posTargetX, posTargetY = 550, 30
posScoreX, posScoreY = 0, 0
posTableScoreX, posTableScoreY = -100, -300
posTutorialX,posTutorialY = -500, -500
TargetYRandom = 0
TargetYCalculation = 0
TimerResTarget = 12
condStyleTarget = 0
createPipe = False
stop = False
exit = True
currentScreen = "Menu"
clock = pygame.time.Clock()
screen = pygame.display.set_mode((500, 700))

pygame.display.set_caption("Flappy Bob")

screen.blit(menuImg, (0, 0))

while exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            exit = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and currentScreen == "Game":
                playerMoviment = 0
                playerMoviment -= 3.2
    if ChangeMenu() == "Exit" and currentScreen == "Menu":
        exit = False
    elif ChangeMenu() == "Start" and currentScreen == "Menu":
        currentScreen = "Game"
    elif ChangeMenu() == "Tutorial" and currentScreen == "Menu":
        currentScreen = "Tutorial"
        screen.blit(TutorialImg, (0, 0))
    elif ChangeMenu() == "ReturnMenu" and currentScreen == "Tutorial":
        currentScreen = "Menu"
        screen.blit(menuImg, (0, 0))

    if currentScreen == "Game":
        if stop == False:
            score += 0.1
            if posPlayerY <= 0:
                posPlayerY = 0
            elif posPlayerY > 0 and posPlayerY < 630:
                gravity = 0.10
            elif posPlayerY >= 630:
                posPlayerY = 630
                gravity = 0
            playerMoviment += gravity
            posPlayerY += playerMoviment
        CheckScore(score)
        CreateAssets(posPlayerY, condStyleTarget)
        CreateText("Score: " + str(round(score,0)), (0,0,0), 30, posScoreX, posScoreY)
        CheckInputMouse()
        MoveAssetsAndRect()
        CheckStyleTargetAndMove(condStyleTarget)
        if CheckCollisions() != "Acertei nada":
            stop = True
            cond = managerScoreScreen(CheckCollisions())
            if cond == "Sair":
                exit = False
            elif cond == "Restart":
                ResetGame()
            
    pygame.display.update()
    clock.tick(120)
