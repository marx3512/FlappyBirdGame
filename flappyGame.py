import pygame

try:
    pygame.init()
except:
    print("Não deu certo")


def ChangeMenu():
    mx, my = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed() == (1, 0, 0):
        if 180 <= mx and mx <= 300 and 380 <= my and my <= 490:
            return "Start"
        elif 180 <= mx and mx <= 300 and 535 <= my and my <= 660:
            return "Exit"

    elif pygame.mouse.get_pressed() == (0, 0, 0,):
        return False


def StartGame():
    screen.fill((255, 255, 255))
    screen.blit(player, (0, 250))
    screen.blit(tubeDown, (310, 350))
    screen.blit(tubeUp, (310, -350))
    screen.blit(door, (310, 215))
    screen.blit(target, (290, 30))


#files
menuImg = pygame.image.load("images\Menu_screen.jpg")
player = pygame.image.load("images/Player(ed).png")
pistol = pygame.image.load("images/Pistol.png")
target = pygame.image.load("images/Target(ed).png")
tubeDown = pygame.image.load("images/Tube(down)(ed).png")
tubeUp = pygame.image.load("images/Tube(up)(ed).png")
door = pygame.image.load("images/Door(ed).png")

# variable
exit = True
currentScreen = "Menu"
screen = pygame.display.set_mode((500, 700))


pygame.display.set_caption("Flappy Bob")

screen.blit(menuImg, (0, 0))


while exit:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            exit = False
    if ChangeMenu() == "Exit" and currentScreen == "Menu":
        exit = False
    elif ChangeMenu() == "Start":
        currentScreen = "Game"
    if currentScreen == "Game":
        StartGame()
    pygame.display.update()
