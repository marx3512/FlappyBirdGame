import pygame, random

try:
    pygame.init()
except:
    print("Não deu certo")


def MoveAssets():
    global posPipeX, posPipeY, posDoorX, posDoorY, posTargetX, posTargetY, TargetYRandom
    posPipeX -= 1
    posDoorX -= 1
    posTargetX -= 1
    if posPipeX < -80:
        posPipeX = 510
        posDoorX = 510
        posTargetX = 490
        posPipeY = random.randint(200, 600)
        TargetYRandom = random.randint(100, 600)

def ChangeMenu():
    mx, my = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed() == (1, 0, 0):
        if 180 <= mx and mx <= 300 and 380 <= my and my <= 490:
            return "Start"
        elif 180 <= mx and mx <= 300 and 535 <= my and my <= 660:
            return "Exit"

    elif pygame.mouse.get_pressed() == (0, 0, 0,):
        return False

# def CheckInputMouse():
#   mx, my = pygame.mouse.get_pos()
#    if pygame.mouse.get_pressed() == (1,0,0):
#       if posTargetX <= mx and mx <= (posTargetX - 200) and posTargetY <= my and my

def CreateAssets(posBirdY):
    screen.fill((255, 255, 255))
    screen.blit(player, (0, posBirdY))
    screen.blit(tubeDown, (posPipeX, posPipeY))
    screen.blit(tubeUp, (posPipeX, posPipeY - 700))
    screen.blit(door, (posDoorX, posPipeY - 132))
    screen.blit(target, (posTargetX, (posTargetY - TargetYRandom)*(-1)))


#files
menuImg = pygame.image.load("images\Menu_screen.jpg")
player = pygame.image.load("images/Player(ed).png")
pistol = pygame.image.load("images/Pistol.png")
target = pygame.image.load("images/Target(ed).png")
tubeDown = pygame.image.load("images/Tube(down)(ed).png")
tubeUp = pygame.image.load("images/Tube(up)(ed).png")
door = pygame.image.load("images/Door(ed).png")

# variable
posPlayerY = 250
gravity = 0.10
playerMoviment = 0
posPipeX, posPipeY = 310, 250
posDoorX, posDoorY = 310, 215
posTargetX, posTargetY = 290, 30
TargetYRandom = 0
createPipe = False
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
                playerMoviment -= 5
    if ChangeMenu() == "Exit" and currentScreen == "Menu":
        exit = False
    elif ChangeMenu() == "Start":
        currentScreen = "Game"
    if currentScreen == "Game":
        CreateAssets(posPlayerY)
        playerMoviment += gravity
        posPlayerY += playerMoviment
        #CreateAssets()
        MoveAssets()
    pygame.display.update()
    clock.tick(120)
