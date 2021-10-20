import pygame

player = pygame.image.load("images/Player(ed).png")
pistol = pygame.image.load("images/Pistol.png")
target = pygame.image.load("images/Target(ed).png")
tubeDown = pygame.image.load("images/Tube(down)(ed).png")
tubeUp = pygame.image.load("images/Tube(up)(ed).png")
door = pygame.image.load("images/Door(ed).png")

white = (255, 255, 255)


def StartGame(screen):
    screen.fill(white)
    screen.blit(player, (0, 250))
    screen.blit(tubeDown, (310, 350))
    screen.blit(tubeUp, (310, -350))
    screen.blit(door, (310, 215))
    screen.blit(target, (290, 30))
