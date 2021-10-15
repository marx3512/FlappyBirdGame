import pygame
import Menu as menu

def StartGame():
    screen_width, screen_height = 500, 700
    exit = True

    screen = pygame.display.set_mode((screen_width, screen_height))

    pygame.display.set_caption("Flappy bird")


    while exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = False
        
        check = menu.ChangeMenu()
        if check == False:
            menu.StarMenu(screen)
        pygame.display.update()
    pygame.quit()
