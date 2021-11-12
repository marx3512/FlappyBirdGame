import pygame, random

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
        posTargetX -= 1

        targetRect.update(posTargetX, TargetYCalculation, 50, 60)
        playerRect.update(0, posPlayerY, 51, 50)
        tubeDownRect.update(posPipeX, posPipeY, 94, 570)
        tubeUpRect.update(posPipeX, posPipeY - 710, 94, 570)
        doorRect.update(posDoorX, posPipeY - 132, 96, 138)

        if posPipeX < -80:
            posPipeX = 510
            posDoorX = 510
            posTargetX = 490
            posPipeY = random.randint(200, 600)
            TargetYRandom = random.randint(100, 600)
            TargetYCalculation = (posTargetY - TargetYRandom)*(-1)

def ChangeMenu():
    mx, my = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed() == (1, 0, 0):
        if 180 <= mx and mx <= 300 and 380 <= my and my <= 490:
            return "Start"
        elif 180 <= mx and mx <= 300 and 535 <= my and my <= 660:
            return "Exit"

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

def CreateAssets(posBirdY):
    screen.fill((255, 255, 255))
    screen.blit(player, (0, posBirdY))
    screen.blit(tubeDown, (posPipeX, posPipeY))
    screen.blit(tubeUp, (posPipeX, posPipeY - 700))
    screen.blit(door, (posDoorX, posPipeY - 132))
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

#files
menuImg = pygame.image.load("images\Menu_screen.jpg")
player = pygame.image.load("images/Player(ed).png")
playerRect = player.get_rect()
pistol = pygame.image.load("images/Pistol.png")
target = pygame.image.load("images/Target(ed).png")
targetRect = target.get_rect()
tubeDown = pygame.image.load("images/Tube(down)(ed).png")
tubeDownRect = tubeDown.get_rect()
tubeUp = pygame.image.load("images/Tube(up)(ed).png")
tubeUpRect = tubeUp.get_rect()
door = pygame.image.load("images/Door(ed).png")
doorRect = door.get_rect()
scoreScreen = pygame.image.load("images/scoreScreen(ed).png")

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
TargetYRandom = 0
TargetYCalculation = 0
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
    elif ChangeMenu() == "Start":
        currentScreen = "Game"
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
        CreateAssets(posPlayerY)
        CreateText("Score: " + str(round(score,0)), (0,0,0), 30, posScoreX, posScoreY)
        CheckInputMouse()
        MoveAssetsAndRect()
        if CheckCollisions() != "Acertei nada":
            stop = True
            cond = managerScoreScreen(CheckCollisions())
            if cond == "Sair":
                exit = False
            elif cond == "Restart":
                ResetGame()
    pygame.display.update()
    clock.tick(120)
