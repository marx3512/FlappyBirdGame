import pygame

image = pygame.image.load("images\Menu_screen.jpg")



def StarMenu(screen):
    screen.blit(image, (0, 0))

def ChangeMenu():
    posMouse = pygame.mouse.get_pos()
    return False
