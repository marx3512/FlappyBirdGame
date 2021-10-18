import pygame

player = pygame.image.load("images/Player.png")
pistol = pygame.image.load("images/Pistol.png")
target = pygame.image.load("images/Target.png")
tubeDown = pygame.image.load("images/Tube(down).png")
tubeUp = pygame.image.load("images/Tube(up).png")
door = pygame.image.load("images/Door.png")

white = (255, 255, 255)


def StartGame(screen):
    screen.fill(white)
    screen.blit(player, (0, 250))
    screen.blit(tubeDown, (310, 350))
    screen.blit(tubeUp, (280, -450))
