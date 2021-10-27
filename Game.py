import pygame
import random

player = pygame.image.load("images/Player(ed).png")
pistol = pygame.image.load("images/Pistol.png")
target = pygame.image.load("images/Target(ed).png")
tubeDown = pygame.image.load("images/Tube(down)(ed).png")
tubeUp = pygame.image.load("images/Tube(up)(ed).png")
door = pygame.image.load("images/Door(ed).png")

white = (255, 255, 255)

timer = 100
heightPipe = 350
horizontalPosPipe = 310
pipeDown = 0


def MovePipe(pipe):
    pipe -= 100


def StartGame(screen):
    screen.fill(white)
    screen.blit(player, (0, 250))
    pipeDown = screen.blit(tubeDown, (horizontalPosPipe, heightPipe))
    screen.blit(tubeUp, (horizontalPosPipe, -heightPipe))
    screen.blit(door, (310, 215))
    screen.blit(target, (290, 30))


def GameUpdate():
    global timer
    timer -= 1
    # print(timer)

    if(timer <= 0):
        timer = 100
    MovePipe(horizontalPosPipe)
