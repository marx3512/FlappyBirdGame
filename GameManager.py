import pygame
import Menu as menu
import Game as game


def StartGame():
    clock = pygame.time.Clock()
    screen_width, screen_height = 500, 700
    currentScreen = "Menu"
    exit = True
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
        if currentScreen == "Game":
            game.StartGame(screen)
            game.GameUpdate()
        pygame.display.update()
        clock.tick(120)
    pygame.quit()
