import pygame
import GameManager as GameConfig

try:
    pygame.init()
except:
    print("Não deu certo")

GameConfig.StartGame()