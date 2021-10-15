import pygame

image = pygame.image.load("images\Menu_screen.jpg")



def StarMenu(screen):
    screen.blit(image, (0, 0))

def ChangeMenu():
    clicking = False
    mx, my = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed() == (1, 0, 0):
        if 180 <= mx and mx <= 300 and 380 <= my and my <= 490:
            print("Apertado")
            return True

    elif pygame.mouse.get_pressed() == (0,0,0,):
        return False
