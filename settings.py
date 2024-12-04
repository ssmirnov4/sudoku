import pygame

width = 540
height = 600
cellSize = width // 9
screen = pygame.display.set_mode((width, height))

white = (255, 255, 255)
black = (0, 0, 0)
grey = (200, 200, 200)
blue = (100, 149, 237)
red = (255, 69, 0)
green = (0, 128, 0)

font = None
def initFonts():
    global font
    font = pygame.font.Font(None, 60)