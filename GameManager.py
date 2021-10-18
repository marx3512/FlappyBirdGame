import pygame
import Menu as menu
import Game as game

def StartGame():
    screen_width, screen_height = 500, 700
    exit = True
    currentScreen = "Menu"
    screen = pygame.display.set_mode((screen_width, screen_height))

    pygame.display.set_caption("Flappy bird")

    menu.StarMenu(screen)
    
    while exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = False
        if menu.ChangeMenu() == "Exit" and currentScreen == "Menu":
            exit = False
        elif menu.ChangeMenu() == "Start":
            currentScreen = "Game"
            game.StartGame(screen)
        pygame.display.update()
    pygame.quit()
